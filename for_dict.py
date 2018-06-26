#!/usr/bin/env python

dict = {

'Name': 'Vallabh',
'Age': '27',
'Place': 'Rcr',
'Sex': 'Male'
}

print(dict)

for i in dict:
   print(i)
   
for k, v in dict.items():
   print("Key: {0}, Value: {1}".format(k,v))
   print("{0}, {1}".format(k,v))
