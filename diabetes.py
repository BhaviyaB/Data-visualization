import pandas as pd
import numpy as np

df = pd.DataFrame(pd.read_csv("diabetes.csv"))
writer = pd.ExcelWriter('diabetes.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', startrow=2)

book = writer.book
sheet = writer.sheets['Sheet1']
# Title
bold = book.add_format({'bold': True, 'size': 24})
sheet.write('A1', 'Diabetes', bold)

format1 = book.add_format({'font_color': '#E93423'})
sheet.conditional_format('B4:E8', {'type': 'cell', 'criteria': '<=', 'value': 0, 'format': format1})
# Bar Chart
chart = book.add_chart({'type': 'column'})
chart.add_series({'values': '=Sheet1!B4:B90', 'name': '=Sheet1!B3', 'categories': '=Sheet1!$A$4:$A$8'})
chart.add_series({'values': '=Sheet1!C4:C90', 'name': '=Sheet1!C3'})
chart.add_series({'values': '=Sheet1!D4:D90', 'name': '=Sheet1!D3'})
chart.add_series({'values': '=Sheet1!E4:E90', 'name': '=Sheet1!E3'})
sheet.insert_chart('K2', chart)
# Scatter Chart
chart = book.add_chart({'type': 'line'})
chart.add_series({'values': '=Sheet1!E4:E90', 'name': '=Sheet1!E3', 'categories': '=Sheet1!$A$4:$A$8'})
chart.add_series({'values': '=Sheet1!F4:F90', 'name': '=Sheet1!F3', 'categories': '=Sheet1!$A$4:$A$8'})
sheet.insert_chart('K20', chart)
# Line Chart
chart = book.add_chart({'type': 'scatter'})
chart.add_series({'values': '=Sheet1!F4:F90', 'name': '=Sheet1!F3', 'categories': '=Sheet1!$A$4:$A$8'})
chart.add_series({'values': '=Sheet1!G4:G90', 'name': '=Sheet1!C3','categories': '=Sheet1!$A$4:$A$8'})
chart.add_series({'values': '=Sheet1!H4:H90', 'name': '=Sheet1!D3'})
chart.add_series({'values': '=Sheet1!I4:I90', 'name': '=Sheet1!E3'}) 
sheet.insert_chart('S2', chart)
# Area Chart
chart = book.add_chart({'type': 'area'})
chart.add_series({'values': '=Sheet1!A4:F90', 'name': '=Sheet1!B3', 'categories': '=Sheet1!$A$4:$A$8'})
chart.add_series({'values': '=Sheet1!B4:G90', 'name': '=Sheet1!C3'})
chart.add_series({'values': '=Sheet1!H4:H90', 'name': '=Sheet1!D3'})
chart.add_series({'values': '=Sheet1!I4:I90', 'name': '=Sheet1!E3'})
sheet.insert_chart('S20', chart)
writer.save()

