import csv
from datetime import datetime

with open('other.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  # first line showing headers for each column
    data = []
    for row in csv_reader:
        #row = [Latitude, Longitude, Description, ZIP, Title, Timestamp, twp, Address, E]
        Latitude = float(row[0])
        Longitude = float(row[1])
        Description = row[2]
        if row[3]:
            ZIP = int(row[3])
        else:
            ZIP = ''
        Title = row[4]
        Timestamp = datetime.strptime(row[5], "%Y-%d-%m %H:%M:%S")
        twp = row[6]
        Address = row[7]
        E = int(row[8])
        data.append([Latitude, Longitude, Description,
                     ZIP, Title, Timestamp, twp, Address, E])

for i in range(len(data) - 1):
    current_row = data[i]
    current_long = row[0]
    current_lat = row[1]
    current_desc = row[2]
    current_zip = row[3]
    current_title = row[4]
    current_time = row[5]
    current_twp = row[6]
    current_address = row[7]
    current_e = row[8]
