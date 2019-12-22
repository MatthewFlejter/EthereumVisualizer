#!/usr/local/bin/python3.7
# Script to graph Ethereum price data that is read in from an existing csv file
# Author: Matthew Flejter
# Data Last Modified: 12/21/2019

# Imports
from CsvProcessor import CsvProcessor
import matplotlib.pyplot as plt
import pandas as pd
import os


# Defining variables and constants
csv_path = os.getcwd() + '/EthereumPrice.csv'
csv_processor = CsvProcessor(csv_path)

# Reading the data from the csv file
data = csv_processor.read()
x_data = []
y_data = []
for dat in data:
    x_data.append(dat['DateTime'])
    y_data.append(dat['USD'])

# Create data frame
df = pd.DataFrame({'Date': x_data, 'Price (USD)': y_data})

# Setting up plot specs
plt.plot('Date', 'Price (USD)', data=df)
plt.show()
