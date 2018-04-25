
import os
import csv

result_file = open('E:\\test.dat', 'wb')


string = []
for i in range (1,138493):
    result_file.write(str(i) +  ' 5 1 1 6\n')

result_file.close()