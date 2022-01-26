import csv
import pandas as pd
import os

with open('final.csv', newline="") as f:
  reader = csv.reader(f)
  data = list(reader)
  headers = data[0]

data.pop(0)

print(data[0])

for i in data:
  g = 6.674e-11 * float(i[3]) *  1.989e+30 / (float(i[4]) * float(i[4]) *  6.957e+8 *  6.957e+8)
  i.append(g)

headers.append("Gravity")

print(data[0])
print(headers)
