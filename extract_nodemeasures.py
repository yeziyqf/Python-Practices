# #keep and extract node measures
import os
# import sys
# import xlrd
# import xlwt
# import re
import sys, getopt

# filename = 'out_attr12_num_newNetwork.csv'
# filename = 'out_20M_full.csv'
# filename = sys.argv[1]

opts, args = getopt.getopt(sys.argv[1:], "i:k:d:")
input_file=""
output_file=""
for op, value in opts:
  if op == "-i":
      filename = value    #filename is the name of the input file
  # if op == "-k":
  #     kept_name = value   #kept_name is the name of the file which keeps the original attr and original and new nodemeasures
  # if op == "-d":
  #     del_name = value    #del_name is the name of the file which deletes the original and new nodemeasures and keep the original attr and new features generated from the original attr
  #   # sys.exit()

if not os.path.exists(filename): # See whether the file exists
    exit(-1)
    #If not exists, terminated.
import csv
def del_cvs_col(fname, newfname, idxs, delimiter=' '):
    with open(fname) as csvin, open(newfname, 'wb') as csvout:
        reader = csv.reader(csvin, delimiter=delimiter)
        writer = csv.writer(csvout, delimiter=delimiter)
        rows = (tuple(item for idx, item in enumerate(row) if idx not in idxs) for row in reader)
        writer.writerows(rows)

def kept_cvs_col(fname, newfname, idxs, delimiter=' '):
    with open(fname) as csvin, open(newfname, 'wb') as csvout:
        reader = csv.reader(csvin, delimiter=delimiter)
        writer = csv.writer(csvout, delimiter=delimiter)
        rows = (tuple(item for idx, item in enumerate(row) if idx in idxs) for row in reader)
        writer.writerows(rows)


lines = [line.split(' ') for line in open(filename)]
df = [[str(x) for x in line] for line in lines[0:1]]
print type(df)

col = []
list_delsingle = []
list_keptsingle = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
list_keptsinglemulti = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19] #adding 20???
list_delsinglemulti = []
list_delmulti = []
column = {}
for i in range(len(df[0])):
    # column[i] = [col[i] for col in reader]
    if  ('weightedDegree') in df[0][i]:
        list_delsingle.append(i)
        list_delsinglemulti.append(i)
    if ('community' ) in df[0][i]:
        list_delsingle.append(i)
        list_delsinglemulti.append(i)
    if ('degree' ) in df[0][i]:
        list_delsingle.append(i)
        list_delsinglemulti.append(i)
    if ('hub' ) in df[0][i]:
        list_delsingle.append(i)
        list_delsinglemulti.append(i)
    if ('role') in df[0][i]:
        list_delsingle.append(i)
        list_delsinglemulti.append(i)
    if ('CLCC') in df[0][i]:
        list_delmulti.append(i)
        list_delsinglemulti.append(i)
    if ('CDC') in df[0][i]:
        list_delmulti.append(i)
        list_delsinglemulti.append(i)
    if ('MDC1') in df[0][i]:
        list_delmulti.append(i)
        list_delsinglemulti.append(i)
    if ('MDC2') in df[0][i]:
        list_delmulti.append(i)
        list_delsinglemulti.append(i)
    if ('MDC3') in df[0][i]:
        list_delmulti.append(i)
        list_delsinglemulti.append(i)
print 'list for delsingle:',list_delsingle,'finished!'
print 'list for keptsingle:',list_keptsingle ,'finished!'
print 'list for keptsinglemulti:',list_keptsinglemulti ,'finished!'
print 'list for delmulti:',list_delmulti ,'finished!'
del_cvs_col(filename, 'original_newfeature.csv', list_delsinglemulti)
kept_cvs_col(filename, 'original_Single.csv', list_keptsingle)
del_cvs_col(filename, 'original_single_newfeature.csv', list_delmulti)
kept_cvs_col(filename, 'original_Single_multi.csv', list_keptsinglemulti)