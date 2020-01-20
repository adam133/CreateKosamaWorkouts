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


def add_row(processed_rows, values, baserow):
    if baserow:
        processed_rows.append({"time": values[0],
                               "text": values[1]})
    else:
        item_number = len(processed_rows) - 1
        processed_rows[item_number]["text"] = processed_rows[item_number]["text"] + ' \n ' + values[1]


def process_rows(sheet):
    processed_rows = []
    for r in range(sheet.nrows):
        baserow = False
        types = sheet.row_types(r)
        values = sheet.row_values(r)
        if types[0] == 2:
            baserow = True
        if baserow or len(processed_rows) > 0:
            add_row(processed_rows, values, baserow)

    return processed_rows


def export_workout(wo, name):
    with open('workouts/' + name + '.txt', 'w', encoding='utf-8') as f:
        json.dump(wo, f, ensure_ascii=False, indent=2)


def main():
    config = get_config()
    files = get_files(config["filepath"])
    for file in files[0:config["FilesToRead"]]:
        xl = open_xlf(xlfile=file)
        for s in range(len(xl.sheets())):
            sheet = open_sheet(xl, s)
            print(f"Processing: {sheet.name}")
            print(f"Rows: {sheet.nrows}")

            processed_rows = process_rows(sheet)

            workout = {"workout": processed_rows}
            export_workout(wo=workout, name=sheet.name)


if __name__ == "__main__":
    main()
