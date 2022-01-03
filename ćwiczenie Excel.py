from openpyxl import load_workbook

wb = load_workbook('E:\\ĆWICZENIE.XLSX')
ws = wb['Arkusz1']

for wiersz in ws.rows:
    for komorka in wiersz:
        print(komorka.value)