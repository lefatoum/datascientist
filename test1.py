import pandas as pdn
import numpy as np
import os

list1 = pdn.read_csv("datas/allemployeescy2019_feb19_20final-all.csv", encoding= 'latin-1')

print(list1.columns.values)
