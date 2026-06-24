import openpyxl


def get_excel_data(sheet_name):

    workbook = openpyxl.load_workbook(
        "testData/testdata.xlsx"
    )

    sheet = workbook[sheet_name]

    data_list = []

    for row in sheet.iter_rows(min_row=2, values_only=True):

        # Remove trailing None values
        row_data = list(row)

        while row_data and row_data[-1] is None:
            row_data.pop()

        data_list.append(tuple(row_data))

    workbook.close()

    return data_list