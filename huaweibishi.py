import os
# import sys
# import xlrd
# import xlwt
# import re
import sys, getopt


opts, args = getopt.getopt(sys.argv[1:], "i:k:d:")
input_file=""
output_file=""
for op, value in opts:
  if op == "-i":
      filename = value
  if op == "-k":
      kept_name = value
  # if op == "-d":
  #     del_name = value


def decimalToAny(num,n):
   baseStr = {10:"a",11:"b",12:"c",13:"d",14:"e",15:"f",16:"g",17:"h",18:"i",19:"j"}
   new_num_str = ""
   while num != 0:
       remainder = num % n
       if 20 > remainder > 9:
           remainder_string = baseStr[remainder]
       elif remainder >=20:
           remainder_string = "("+str(remainder)+")"
       else:
           remainder_string = str(remainder)
       new_num_str = remainder_string+new_num_str
       num = num / n
   return new_num_str



decimalToAny(num,n)