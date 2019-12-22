#!/usr/local/bin/python3.7
# Class to write general data to a csv file
# Author: Matthew Flejter
# Data Last Modified: 12/21/2019

# imports
import csv
from os import path


class CsvWriter:

    def __init__(self, path):
        self.path = path

    # Write data to csv file and create it if it does not exist already.
    # Data is a single plane dictionary object
    def write(self, data):
        if self.path == None or self.path == '':
            return

        # Determine if the file will be created for the first time or appended to
        option = self.__getFileOption__()

        # Fields for the header row
        fieldnames = data.keys()

        with open(self.path, option) as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if (option == 'w'):
                writer.writeheader()

            writer.writerow(data)

    # Determine if the file should be created and written to or simply appended to
    def __getFileOption__(self):
        if self.path == None or self.path == '' or not path.exists(self.path):
            return 'w'
        else:
            return 'a'
