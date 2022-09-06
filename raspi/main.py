import csv
import time
from getdata import getD

getD = getD()
field_name = getD.field_name()

data = []
for i in range(10):
    data.append(getD.dic())
    time.sleep(1)
    
print(data)
with open(r'./data/data.csv','a',encoding='utf-8', newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = field_name)
    writer.writeheader()
    writer.writerows(data)