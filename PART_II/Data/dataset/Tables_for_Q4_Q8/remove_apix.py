import csv

with open('device.csv', "r+",encoding="utf-8") as csv_file:
    content = csv_file.read()
    
with open('device.csv', "w+",encoding="utf-8") as csv_file:
    csv_file.write(content.replace('"', ''))
    