
# CSV to Excel Sheet Generator

This project is a command-line tool designed to transform multiple CSV files into a single Excel file with multiple sheets. Each sheet represents data from a specific CSV file, allowing users to select columns they wish to include.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Additional Information](#additional-information)

## Introduction

Welcome to the CSV to Excel Sheet Generator! This tool allows you to process numerous CSV files, extracting user-selected columns from each and consolidating them into a single Excel workbook. Designed for simplicity and flexibility, it ensures an easy and efficient way to manage your CSV data.

## Features

- Converts multiple CSV files into an Excel file with multiple sheets.
- Users can select specific columns from each CSV file.
- Handles invalid column selections gracefully with input validation.
- Outputs the final data into an Excel workbook with sheets named after the original CSV files.

## Installation

### Requirements

Before running the application, ensure you have the following installed:

- Python 3.x
- pandas
- xlsxwriter

### Setup

Clone the repository:

```sh
git clone https://github.com/AHSANooo/csv-to-excel-sheets-generator-and-specific-fields-extractor-from-multiple-csvs-to-excel-sheets.git
cd csv-to-excel-sheets-generator-and-specific-fields-extractor-from-multiple-csvs-to-excel-sheets 
```
### Install required packages:

```sh
pip install -r requirements.txt
```

Ensure your CSV files are placed in the data/input directory and specify the output file path in config/settings.py.
### How to Use

Run the application:
```sh
python main.py
```

The program will prompt you to select columns from each CSV file. It then generates an Excel file named merged_output.xlsx in the data/output directory, with each sheet corresponding to an input CSV file.
Additional Information

The application is built with modularity in mind, allowing easy updates and extensions. It includes robust input validation to handle user errors effectively.

Feel free to explore and customize the tool to fit your specific needs!

### Customization Tips

- **Repository URL**: Replace `https://github.com/AHSANooo//csv-to-excel-sheets-generator-and-specific-fields-extractor-from-multiple-csvs-to-excel-sheets.git` with your actual repository URL.
- **File Paths and Configurations**: Adjust paths and configuration details according to your project's setup.
