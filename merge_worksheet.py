#!/usr/bin/python

import os
import sys
import pandas
import argparse
from xls2xlsx import XLS2XLSX

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

parser = argparse.ArgumentParser(
    description = 'Merge two or more xlsx file(s) into one file',
    epilog = 'Rail Cargo Group software copyright'
)
parser.add_argument('-s', '--source', help='The source folder of xls(x) files.', default='.')
parser.add_argument('-o', '--output', help='The output folder of xlsx file.', default='.')
parser.add_argument('-n', '--name', help='The name of xlsx file.', default='merge_files')
args = parser.parse_args()

source_file = os.path.join(BASE_DIR, args.source)
destination_file = os.path.join(BASE_DIR, args.output)

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
df.to_excel(os.path.join(destination_file, args.name + '.xlsx'))
