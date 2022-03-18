# xlsx-files-merge
It merges all files into directory

## Table of Contents
- [Local Setup](#local-setup)
- [Get it](#get-it)
- [How to use it](#how-to-use-it)
- [Contributing](#contributing)

### Local Setup
You have to install on your local machine the listed softwares below:
1. Install [git](https://git-scm.com/) to manage Git repository.
2. Install [python](https://www.python.org/) the Python interpreter for script.

***You will need to install pandas and xls2xlsx libraries of python***
```shell
pip install pandas
pip install xls2xlsx
```

### Get it
First of all, clone the repository `xlsx-files-merge` into your local machine:

```shell
git clone https://github.com/FabioAnsaldi/xlsx-files-merge.git
```


### How to use it

Have a look at help informations by running:

```shell
merge_worksheet.py [-h]
```

You can run script file via terminal or Windows prompt:

```shell
python3 merge_worksheet.py
```
***It merges all xlsx (or xls) files of current folder and the outputted file in the same folder***

```shell
python3 merge_worksheet.py -s `source_dir` -o `output_dir` -n `my_file`
```
***It merges all files of the `source_dir` folder and the outputted file in the `output_dir` folder with `my_file_.xlsx` file name***

### Contributing
Feel free to make changes to the project files.
