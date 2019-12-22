#!/usr/local/bin/python3.7
# Class to read and write general data from and to a csv file respectively
# Author: Matthew Flejter
# Data Last Modified: 12/21/2019

# imports
import csv
from os import path


class CsvProcessor:

    def __init__(self, path):
        self.path = path

    # Write data to csv file and create it if it does not exist already.
    # Data is a single plane dictionary object
    def write(self, data):
        if not self.__is_path_valid__:
            return

        # Determine if the file will be created for the first time or appended to
        option = self.__get_file_option__()

        # Fields for the header row
        fieldnames = data.keys()

        with open(self.path, option) as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if (option == 'w'):
                writer.writeheader()

            writer.writerow(data)

    # Read data from a csv file. Returns a list of dictionary objects
    def read(self):
        # Data to return
        data = []

        # Return nothing if the file path is invalid
        if not self.__is_path_valid__():
            return data

        # Process the csv
        with open(self.path, 'rt') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')

            line_count = 0
            columns = []
            for row in reader:
                curr_data = {}
                if (line_count == 0):
                    columns = row
                else:
                    # Loop through all data in the current row
                    data_index = 0
                    for dat in row:
                        curr_data[columns[data_index]] = dat
                        data_index += 1

                    # Add data to the data array
                    data.append(curr_data)

                # Increment line counter
                line_count += 1

        # Return csv data
        return data

    # Determine if the csv is getting created for the first time or if it is simply being appended to and
    # return the proper option accordingly
    def __get_file_option__(self):
        if self.path == None or self.path == '' or not path.exists(self.path):
            return 'w'
        else:
            return 'a'

    # Determine if the given file path is valid or not
    def __is_path_valid__(self):
        if self.path == None or self.path == '' or not path.exists(self.path) or not self.path.endswith('.csv'):
            return False
        return True
