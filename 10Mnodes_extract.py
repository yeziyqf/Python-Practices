import pandas as pd
import os

os.chdir('E:')
read_file1 = 'movies.dat'
read_file2 = '20Mnodes_num_comma_deleted.csv'
colname = ['id','Rated','Language','Country','Writer','Director','Actors','Genre','Nomination','WinOscar','WinOther']
movname = ['id','title','genres']
file1 = pd.read_csv(read_file1, sep ='::',names = movname ,engine = 'python')
file2 = pd.read_csv(read_file2,names = colname, sep =' ')


# file1 = f1.sort_values(by='id')
# file2 = f2.sort_values(by='id')

# file1 = f1['id']
# file2 = f2['id']

# attr1 = file1.columns.values
# attr2 = file2.columns.values

# print 'attr1:', attr1
# print 'attr2:', attr2
# test = file1.join(file2)
# test = pd.concat([file1,file2], axis = 1, join='outer')

need_append_list = []
other_append_list = []
todelete_list = []
# if file1['id'].equals(file2['id']):
#     need_append_list.append(a)
#     # pass

# for a in attr1:
#     if a not in attr2:
#         other_append_list.append(a)
#
# for a in attr1:
#     if a in attr2:
#         need_append_list.append(a)
#
from pandas import Series,DataFrame
from pandas import DataFrame as df
def row_del(df, num_percent, label_len = 0):
	#print list(df.count(axis=1))
	col_num = len(list(list(df.values)[1])) - label_len
	if col_num<0:
		print 'Error'
	#print int(col_num*num_percent)
	return df.dropna(axis=0, how='any', thresh=int(col_num*num_percent))

# find ids which are in left & not in right
need_append_list = [str(i) for i in file1['id'].values if str(i) in file2['id'].values]
need_append_list.remove("id")
print 'file1id:',file1['id']
# find ids which are not in left & in right
other_append_list = [str(i) for i in file1['id'].values if str(i) not in file2['id'].values]
print 'file2id:',file2['id']
todelete_list = [str(m) for m in file2['id'].values if str(m) not in file1['id'].values]
print 'need:',need_append_list
print 'other',other_append_list
print 'todelete:',todelete_list

print'typefile2',type(file2)
file3 = pd.DataFrame()
length = len(file2['id'])

# for k in todelete_list:
#     # file2.drop(int(k))
#     file2<-file2[int(k),]
#     # file2 = file2[c(-k),]
#     # file2 =df[file2(-3, -8, -9, -24),]
#     # file2 = file2[file2.id==need_append_list]
#     print k

# row_del(file2,todelete_list)

def should_delete(i,todelete_list):
    # if i.in(todelete_list):
    if todelete_list.__contains__(i):
        return True
k=0
id_judge = file2['id'][k]
with open(read_file2) as fp_in:
    with open('extract.csv', 'w') as fp_out:
        for line in fp_in:
            if should_delete(str(id_judge),todelete_list):
                pass
                print 'num of line:',k, ' id:',id_judge
            else:
                # fp_out.writelines(line for i, line in enumerate(fp_in))
                fp_out.write(line)
                print 'write:',line
            k = k + 1
            id_judge= file2['id'][k]
            # fp_out.writelines(line for i, line in enumerate(fp_in) if i != k)

# print should_delete(str(25),todelete_list)

# if (str(i) for i in file2['id'].values if str(i) in need_append_list):
#







# # keep the rows matches to file1
# for i in need_append_list:
#     # print file2['id'][int(i)]
#     for k in range(0,length):
#         if file2['id'][k] == str(i):
#             # file2.drop(k)
#             # file3.loc[:,k] = file2['id'][k]
#             # file3[:, k] = file2[:,k]
#             file3 = file2[file2['id'].isin(need_append_list)]  #Select the lines which supports the list
#             # if file2[file2['id'].isin(need_append_list)]:
#
#             print k




    # file2 = file2[file2.id == str(i)]
# print file2
#
# # add the rows in left & not in right
# index = file2.size
# for i in xrange(len(ret1)):
#     file2.loc[index] = ''
#     index += 1
#
# # add attr not in left & in right
# for l in need_append_list:
#     file1[l] = file2[l]



# print file2
# file2.to_csv('test1.csv', index=False, name = False)