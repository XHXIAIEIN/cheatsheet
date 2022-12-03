# https://stackoverflow.com/a/61394616/20672242

from xlsxwriter import Workbook

def create_xlsx_file(file_path: str, headers: dict, items: list):
    with Workbook(file_path) as workbook:
        worksheet = workbook.add_worksheet()
        worksheet.write_row(row=0, col=0, data=headers.values())
        header_keys = list(headers.keys())
        for index, item in enumerate(items):
            row = map(lambda field_id: item.get(field_id, ''), header_keys)
            worksheet.write_row(row=index + 1, col=0, data=row)


headers = {
    'id': 'User Id',
    'name': 'Name',
    'rating': 'Rating',
}

items = [
    {'id': 1, 'name': "Ilir Meta", 'rating': 0.06},
    {'id': 2, 'name': "Abdelmadjid Tebboune", 'rating': 4.0},
    {'id': 3, 'name': "Alexander Lukashenko", 'rating': 3.1},
    {'id': 4, 'name': "Miguel Díaz-Canel", 'rating': 0.32}
]

create_xlsx_file("file.xlsx", headers, items)
