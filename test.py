import openpyxl 

path = 'E:\\Work\\มวล\\ITD\\ปี 1\\เทอม 3\\Excel\\Week 2\\01_19_64100738.xlsx'
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active
row = 1
column = 1



# while True:
for x in range(49):
    cell_obj = sheet_obj.cell(row, column)
    if cell_obj.value is not None:
        print(cell_obj.value)
        column += 1
    else :
        print("Enter")
        row += 1
        column = 1

    

    

