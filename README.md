# Black Rock Take Home Exercises

# This project is a streamlit built web app containing the main exercises and extra credit excerises.

## Table of contents

- [Prerequisites]
- [Installation]
- [Usage]
- [Assumptions]
- [FileStructure]
- [AdditionalNotes]

### Prerequisites

- Python 3 installed on your system.

## Installaltion

1. ** Activate the virtual environment **

- navigate to the project directory where the virtual environment is stored.
- activate virtual environment.
- Example (Windows):

  ```
  # Activate the virtual environment
  .\env\Scripts\activate
  ```

- Example (Unix/macOS):

  ```
  # Activate the virtual environment
  source env/bin/activate
  ```

2. ** Install Dependencies **

- pip install -r requirements.txt

## Usage

- Run `streamlit main.py` in terminal to start the application.
- Navigate to `http://localhost:8501` in your web browser.

## Assumptions

1. Data Assumptions:

- Input file will always be of type excel format (.xlsx). Validation for this was implemented if the user tries to upload other file types the user will be presented with a error message to upload xlsx files only.
- The input data will always contain three columns: portfolio_name, security_id, and weight.
- The security id column contains unqiue values.
- extra credit exercise task 3 to calculate the beta value of BlackRock Stock against the market the S&P 500 was used.
- input data was already normalise but logic was still implemented to normalise data and tested on un - normalised data.
- For calculating moving average in extra credit task 1 it was assumed there are 1260 trading days in 5 years

2. Technical Assumptions

- Menu to be implemented to present the Main Exercises for the take home exercises and the extra credit exercises on seperate pages allowing the user to navigate between the two.
- The application will be built using Python and Streamlit framework.
- Pandas + Numpy will be required to hand data manipulation.
- OS library for file path manipulation.
- application is hosted locally for development and testing purposes.

3. User Interface Assumptions:

   - Users are familiar with uploading files using the provided file uploader widget.
   - Users understand the purpose of the application, which is to validate and normalize investment data.
   - Users can interpret the validation messages and take appropriate actions based on them.

4. Functional Assumptions:

   - The application notifies the user if they have entered a file type other than .xlsx
   - The application normalizes the weights for each portfolio so that they sum up to 100%.
   - The application retrieves asset_class and investment_type information based on the security_id.
   - If any empty values are found in the input data, the application notifies the user and allows manual correction.
   - The manual correction involves downloading the Excel file, filling in the empty values, and re-uploading it for validation.
   - The application validates the input data to ensure that investment_type and asset_class values are valid.
   - If the input data passes validation, the application displays a success message; otherwise, it displays an error message.
   - Users will continously use the same file uploaded widget, post manual ammendments.
     - Possibility of making widget dissapear post upload explored, avoided as it complicated the process.
   - Task 1 of extra credit task calculating moving average will need to be displayed using a chart and compared with the closing price. This chart will be created usign matplotlib
   - Task 3 of extra credit task, yfinance library needs to be used to retrieve data for last 5 years for S&P 500.

5. Deployment Assumptions:
   - Deployment requires setting up environment variables and ensuring dependencies are installed.
   - Users can access the deployed application through a web browser.

## FileStructure

- **env/**: contains the virtual environment to create this project
- **testing_files/**: contains input files to test all the scenarios
- **app.py**: contains the main exercises for the streamlit application. Define the file uploader, data processing and validation
- **Extra_Credit_Task.py**: contains the extra credit exercises, defines the calculations and visualisation
- **main.py**: defines the menu of the streamlit application, consisting logic to navigate between the main exercises and extra credit tasks.
- **README.md**: This file provides instructions and information about the project.
- **requirements.txt**: Lists all the Python dependencies required to run the application.

## AdditionalNotes

- Hope you enjoy this project :)
