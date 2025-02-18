import streamlit as st
import pandas as pd
import io
import os


# Defined values for investment_type and asset_class
investment_types = [
    "Single Line Stock", "Single Line Bond", "Alpha Seeking Mutual Fund",
    "Index Mutual Fund", "ETP", "Index", "Derivative", "Cash",
    "Alternative Fund", "Other"
]

asset_classes = [
    "Alternative", "Fixed Income", "Commodity", "Equity",
    "Multi Asset", "Cash", "Money Market", "Other"
]


def normalise(col):
    """
    defining normalise function
    """
    sum = col.sum()
    return round((col / sum) * 100, 1)


def security_lookup(df):
    """
    look up function to retireve the asset_class and investment_type for given security_id
    """

    # read in static file
    db_replica = pd.read_excel('exercises/db_replica_example.xlsx')

    if len(df.columns) == 3:

        df = df.merge(db_replica[['og_id', 'asset_class', 'investment_type']],
                      how='left', left_on='security_id', right_on='og_id')
        return df[['portfolio_name', 'security_id', 'weight', 'asset_class', 'investment_type']]

    else:
        return df


def notify_incomplete_data(df):
    """
    identify empty asset_class and investment_type values and return the security id
    """

    # get security ids which had null assets_class/investment_type
    null_asset_class = df[df['asset_class'].isnull()]['security_id'].tolist()
    null_investment_type = df[df['investment_type'].isnull(
    )]['security_id'].tolist()

    if null_asset_class:
        st.error(
            f"Security IDs which had asset_class empty: {null_asset_class}")

    if null_investment_type:
        st.error(
            f"Security IDs which had investment_type empty: {null_investment_type}")

    st.error("Manual cleaning is neccessary, Download Excel File and populate empty values and re-upload.")


def download_file(df):
    """
    reusable function to convert a dataframe to a excel workbook at any point
    """
    # Add a button to download the DataFrame as an Excel file
    # Convert DataFrame to Excel
    # in memory stream to write bytes to
    excel_data = io.BytesIO()

    # writing contents of the dataframe to the BytesIO stream created
    # writing to BytesIO to create a workbook without having to write the file to disk
    df.to_excel(excel_data, index=False)

    # moves position to the start of the stream
    excel_data.seek(0)

    # Create a downloadable link
    st.download_button(label="Download Excel File", data=excel_data, file_name='data.xlsx',
                       mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')


def validate_data(df):
    """
    Check to see all values manualy corrected are valid inputs
    """

    validation_issues = []

    # Check if investment_type and asset_class are in specified lists
    for idx, row in df.iterrows():
        if row['investment_type'] not in investment_types:
            validation_issues.append(
                f"Invalid investment_type '{row['investment_type']}' for security ID {row['security_id']}")
        if row['asset_class'] not in asset_classes:
            validation_issues.append(
                f"Invalid asset_class '{row['asset_class']}' for security ID {row['security_id']}")

    if validation_issues:
        # Notify user of validation issues
        st.write("The file contains the following validation issues:")
        for issue in validation_issues:
            st.error(issue)

        return "invalid"
    else:
        return "valid"


def main():
    # set page titles
    # st.title('Black Rock Take Home Exercise')
    st.title('Main Exercise')

    # bool to track if the user has uploaded a file
    is_file_uploaded = False

    # creating a place holder for the file holder
    uploader_placeholder = st.empty()

    # no file is uploaded then present the file uploader
    if not is_file_uploaded:
        # create file uploader widget
        file_upload = uploader_placeholder.file_uploader(label='Upload File')
        is_file_uploaded = True

    # only read in file if file has been uploaded
    if file_upload is not None and is_file_uploaded:

        # extract the file type from the file path
        file_extension = os.path.splitext(file_upload.name)[-1]

        # present user with error message if the user does not upload a file of XLSX format
        if file_extension != '.xlsx':

            st.error("Error: Please upload a file in XLSX format.")

        else:
            # read uploaded file and display first rows
            df_file_uploaded = pd.read_excel(file_upload)

            # normalise data so that the weights for each column sum to 100
            df_file_uploaded['weight'] = df_file_uploaded.groupby(
                'portfolio_name')['weight'].transform(normalise)

            # retrieve asset_class and investment_type for each security id
            df_file_uploaded = security_lookup(df_file_uploaded)

            st.write(df_file_uploaded)

            # returns true if there is atleast one empty value
            if df_file_uploaded.isnull().any().any():

                notify_incomplete_data(df_file_uploaded)
                download_file(df_file_uploaded)

            else:
                # Validate the data
                validation_result = validate_data(df_file_uploaded)

                if validation_result == "valid":
                    st.success("The file has passed validation.")
                else:
                    st.error(
                        "The file did not pass validation. Please download and make the necessary adjustments and re-upload.")
                    download_file(df_file_uploaded)


if __name__ == '__main__':
    main()
