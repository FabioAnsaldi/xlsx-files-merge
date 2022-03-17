#!/usr/bin/python

import os
import sys
import pandas
from xls2xlsx import XLS2XLSX

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

source = sys.argv[1] if len(sys.argv) > 1 else '.'
destination = sys.argv[2] if len(sys.argv) > 2 else '.'

source_file = os.path.join(BASE_DIR, source)
destination_file = os.path.join(BASE_DIR, destination)

if not os.path.exists(destination_file):
    os.makedirs(destination_file)

## Transforms xls to xlsx file
files = os.listdir(source_file)
for file in files:
    if file.endswith('.xls'):
        file_path = os.path.join(source_file, file)
        x2x = XLS2XLSX(file_path)
        x2x.to_xlsx(file_path.replace('.xls', '.xlsx'))

## Gets the first sheet of a given file
files = os.listdir(source_file)
df = pandas.DataFrame()
for file in files:
    if file.endswith('.xlsx'):
        file_path = os.path.join(source_file, file)
        df = df.append(pandas.read_excel(file_path), ignore_index=True)
df.head()
df.to_excel(os.path.join(destination_file, 'merge_files.xlsx'))
