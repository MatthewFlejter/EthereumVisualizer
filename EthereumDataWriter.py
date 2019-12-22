#!/usr/local/bin/python3.7
# Script to fetch Ethereum pricing data and log it to a CSV File
# Author: Matthew Flejter
# Data Last Modified: 12/21/2019

# Imports
import requests as req
import argparse
import os
import sys
from CsvWriter import CsvWriter

# initiate the parser
parser = argparse.ArgumentParser()

# Variable to store the cryptocompare api token in
api_key = ''

# Read the api token from the arguments
parser.add_argument("--token", help="Set the API token")
args = parser.parse_args()
if args.token:
    api_key = args.token
else:
    print('No API token specified... Exiting...')
    sys.exit(0)

# URI to get data
uri = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms=ETH&tsyms=BTC,USD,EUR&api_key=' + api_key

# Path to csv file to log data; by default place this in the current working directory
csv_path = os.getcwd() + 'EthereumPrice.csv'

# Fetch data
r = req.get(url=uri, params={})
if (r.status_code != 200):
    print("Error retrieving data from CryptoCompare endpoint... Exiting...")
data = r.json()

# Write pricing data to csv file
writer = CsvWriter(csv_path)
writer.write(data['ETH'])
