import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np


def moving_avg(df, window):
    """
    Calculate the moving average
    """
    df['Moving Average'] = df['Close'].rolling(
        window=window, min_periods=1).mean()
    return df


def main():

    # Load in required stock data for Black Rock and S&P 500
    blk_data = yf.download('BLK', start='2019-05-05', end='2024-05-05')
    sp500_data = yf.download('^GSPC', start='2019-05-05', end='2024-05-05')

    st.title('Extra Credit Task')

    # Task 1
    st.write(
        '**Task 1: Calculate the yearly moving average price for the BLK stock.**')

    # Create Plot for Closing Price vs Moving Average
    blk_data = moving_avg(blk_data, 1260)
    fig = plt.figure(figsize=(16, 8))
    plt.title('Close Price History vs Simple Moving Average', fontsize=18)
    plt.plot(blk_data['Close'], color='blue',
             linestyle='-', label='Closing Price')
    plt.plot(blk_data['Moving Average'], color='red',
             linestyle='-', label='Moving Avg')
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Close Price', fontsize=18)
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)

    # assuming 1260 trading days in 5 years
    blk_data = moving_avg(blk_data, 1260)

    st.write(blk_data)
    st.pyplot(fig)

    # Task 2
    st.write('**Task 2: Determine the volatility of the stock.**')

    # Calulcate daily percent Change
    blk_data['Daily Returns'] = blk_data['Close'].pct_change()

    # Apply Standard Deviation on Daily Returns
    volatility = blk_data['Daily Returns'].std()

    st.write('Volatility of Black Rock Stock last 5 years: ',
             round(volatility * 100, 1), "%")

    # Calculate annualized volatility
    annualized_volatility = volatility * (252 ** 0.5)
    st.write("Annualized Volatility: ", round(
        annualized_volatility * 100, 1), "%")

    # Task 3
    st.write('**Task 3: Compute the Beta for the BLK stock.**')

    # Calulcate daily percentage change
    sp500_data['SP500 Returns'] = sp500_data['Close'].pct_change()

    # Concat BLK and S&P 500 daily percentage changes
    combined_data = pd.concat(
        [blk_data['Daily Returns'], sp500_data['SP500 Returns']], axis=1).dropna()

    # Calculate covariance matrix
    covariance_matrix = np.cov(
        combined_data['Daily Returns'], combined_data['SP500 Returns'])

    # Calculate beta
    stock_beta = covariance_matrix[0, 1] / covariance_matrix[1, 1]

    st.write("Beta for BLK compared to S&P 500:", round(stock_beta, 1))


if __name__ == '__main__':
    main()
