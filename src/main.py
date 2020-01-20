import sys
import os
import xlrd
import json


def get_config():
    with open('config.json') as json_config_file:
        return json.load(json_config_file)


def get_files(path):
    files = os.listdir(path)
    return_list = []
    for file in files:
        return_list.append(path + '/' + file)
    return return_list


def open_xlf(xlfile):
    return xlrd.open_workbook(filename=xlfile)


def open_sheet(xlf, sheet_num):
    return xlf.sheet_by_index(sheet_num)


def main():
    config = get_config()
    files = get_files(config["filepath"])
    for file in files[0:config["FilesToRead"]]:
        xl = open_xlf(xlfile=file)
        sheet = open_sheet(xl, 1)
        print(f"Processing: {sheet.name}")
        print(f"Rows: {sheet.nrows}")

        for r in sheet.get_rows():
            print(r)

if __name__ == "__main__":
    main()
