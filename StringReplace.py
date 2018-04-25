# coding=utf-8

import pandas as pd

# import re
# strinfo = re.compile('word')
# a = 'Hello word!'
# b = strinfo.sub('python',a)
# print b



# #替换字符串
# import os
# os.chdir('E:');
# if not os.path.exists('nodes_12features.csv'): # 看一下这个文件是否存在
#     exit(-1)                         #不存在就退出
# lines = open('nodes_12features.csv').readlines()  #打开文件，读入每一行
# fp = open('nodes_12features.csv', 'w')
# for s in lines:
# # replace是替换，write是写入
# #在这步前先把M评级手动用筛选改为R
#     fp.write( s.replace('APPROVED','PASSED').replace('UNRATED','NOT RATED').replace('Not Rated','NOT RATED').replace('TV-14','R').replace('TV-MA','NC-17').replace('TV-PG','PG-13').replace('GP','PG').replace('TV-G','G'));
# #之后填补空缺为UNKNOWN，但记得把RATED中的空缺改为NOT RATED
# fp.close() ; # 关闭文件

# fp.write( s.replace('APPROVED','PASSED').replace('UNRATED','NOT RATED').replace('Not Rated','NOT RATED').replace('TV-14','R').replace('TV-MA','NC-17').replace('TV-PG','PG-13'));




# #替换字符串并选取部分列输出，1M
# import os
# os.chdir('E:');
# df = pd.read_csv('ratings.dat',sep = r'::',header = None, names = ['col0','col1','col2','col3'],engine = 'python');
# df = df[['col1','col0','col2']];
# df['col2'] = 1;
# df.to_csv('ratings_final1.csv',header = None, index = False ,sep = ' ');

# #替换字符串并选取部分列输出并交换这两列,20M
# import os
# os.chdir('E:');
# df = pd.read_csv('ratings.dat',sep = '::',header = None, names = ['col0','col1','col2','col3'],engine = 'python');
# df = df[['col1','col0','col2']];
# df['col2'] = 1;
# df.to_csv('ratings_final.csv',header = None, index = False ,sep = ' ');



#
# #加表头标题同时空格转逗号
# import os
# os.chdir('E:');
# df = pd.read_csv('E:\\beha_1st.count.s_c10',sep = ' ');
# df.to_csv('edges1M.csv',header = ['row','col','weight'],index = False ,sep = ',');

# #空格转逗号
# import os
# os.chdir('E:');
# df = pd.read_csv('E:\\beha_1st.count.s_c10');
# df.to_csv('edges1M.csv',header = [['row','col','weight']],index = False ,sep = '，');

# #逗号转空格
# import os
# os.chdir('E:');
# df = pd.read_csv('20Mnodes_num (2).csv',sep = ',');
# df = df.replace(',',' ')
# df.to_csv('20Mnodes_num (3).csv',index = False ,sep = ' ');





# #去除重复
# import os
# os.chdir('E:');
# df = pd.read_csv('20Mnodes_num_comma_deleted.csv',sep = ' ');
# print 'oiginal len:',len(df['id'])
# print 'without duplicate len:',len(set(df['id']))
# df.drop_duplicates(subset=['id'], keep='first',inplace=True)
# print 'after len:',len(df['id'])
# df.to_csv('10nodes_num_duplicate.csv',index = False ,sep = ' ');


# #逗号转空格replace版
# import os
# os.chdir('E:');
# df = open('nodes_12features_num.csv');
# df_content = df.read()
# df_content = df_content.replace(',',' ')
# with open('20Mnodes_num4.csv', 'w') as tg:
#     tg.write(df_content);

#空格转逗号replace版
import os
os.chdir('E:');
df = open('full.csv');
df_content = df.read()
df_content = df_content.replace(' ',',')
with open('full1.csv', 'w') as tg:
    tg.write(df_content);

# #空格转逗号
# import os
# os.chdir('E:');
# df = pd.read_csv('ratings_final.csv',sep = ' ');
# df.to_csv('ratings_final.csv',header = False,index = False ,sep = ',');


# #统一电影评级
# import os
# os.chdir('E:');
# if not os.path.exists('result_process_modified.csv'): # 看一下这个文件是否存在
#     exit(-1)                         #不存在就退出
#
# awards = pd.read_csv('result_process_modified.csv')
# new = awards[['id','Rated']];
# new = new.replace('APPROVED','PASSED').replace('UNRATED','NOT RATED').replace('Not Rated','NOT RATED').replace('TV-14','R').replace('TV-MA','NC-17').replace('TV-PG','PG-13').replace('M','R').replace('TV-G','G').replace('GP','PG').replace('Unrated','NOT RATED').replace('S','PG-13').replace('TV-Y7','G').fillna('NOT RATED');
# awards[['id','Rated']] = new;
# new1 = awards[['Rated','Language','Title','Country','Writer','imdbRating','Director','Actors','Year','Genre','Awards','Runtime','imdbVotes','id']]  #imDB待定
# new1 = new1.fillna('UNKNOWN')
# awards[['Rated','Language','Title','Country','Writer','imdbRating','Director','Actors','Year','Genre','Awards','Runtime','imdbVotes','id']] = new1
# awards.to_csv('result_process_modified.csv',index = False);

# #统一电影评级
# import os
# os.chdir('E:');
# if not os.path.exists('hehehehe.csv'): # 看一下这个文件是否存在
#     exit(-1)                         #不存在就退出
#
# awards = pd.read_csv('hehehehe.csv')
# new = awards
# new = new.replace('nan','None')
# new = new.fillna('None')
# awards= new;
# awards.to_csv('hehehehe.csv',index = False);


################################################################
# #coding:utf-8
# import re
# import sys
# import os
#
# f = pd.read_csv('out_attr12_num_half_edges.csv')
# # new = f[['id','Rated']];
#
# # f=open('out_attr12_num_half_edges.csv','r+')
# # line=f.readlines()
# f1=open('new.csv','w+')
# # f2=open('ticonf.det.txt','w')
#
# print "Now I will to delete ---+"
# print f.columns(1)
# try:
#     for j in range(0,3301):
#         if re.match(r'^*community*$|^*degree*$|^*weightedDegree*$|^*hub*$|^*role*$', f.iloc[0,j]):
#             f.pop(j)
#             # del line[i]
#             print "delete column",j
#         else:
#             print "Writing",j
#             f1.write(f[0,j])
# except IndexError:
#     print "pass"
#
#################################################################################################
# # #去除和保留node measures
# import os
# import xlrd
# import xlwt
# import re
# os.chdir('E:');
# if not os.path.exists('out_attr12_num_half_edges.csv'): # 看一下这个文件是否存在
#     exit(-1)
#     #不存在就退出
# import csv
# def del_cvs_col(fname, newfname, idxs, delimiter=','):
#     with open(fname) as csvin, open(newfname, 'wb') as csvout:
#         reader = csv.reader(csvin, delimiter=delimiter)
#         writer = csv.writer(csvout, delimiter=delimiter)
#         rows = (tuple(item for idx, item in enumerate(row) if idx not in idxs) for row in reader)
#         writer.writerows(rows)
#
# def kept_cvs_col(fname, newfname, idxs, delimiter=','):
#     with open(fname) as csvin, open(newfname, 'wb') as csvout:
#         reader = csv.reader(csvin, delimiter=delimiter)
#         writer = csv.writer(csvout, delimiter=delimiter)
#         rows = (tuple(item for idx, item in enumerate(row) if idx in idxs) for row in reader)
#         writer.writerows(rows)
#
# # filename = 'out_attr12_num_newNetwork.csv'
# filename = 'out_attr_type_12_num_newNetwork.csv'
#
#
#
# lines = [line.split(',') for line in open(filename)]
# df = [[str(x) for x in line] for line in lines[0:1]]
# print type(df)
#
# col = []
# list = []
# column = {}
# for i in range(0,3301):
#     # column[i] = [col[i] for col in reader]
#     if  ('weightedDegree') in df[0][i]:
#         list.append(i)
#     if ('community' ) in df[0][i]:
#         list.append(i)
#     if ('degree' ) in df[0][i]:
#         list.append(i)
#     if ('hub' ) in df[0][i]:
#         list.append(i)
#     if ('role') in df[0][i]:
#         list.append(i)
# print list,'finished!'
# del_cvs_col(filename, 'deleted_nodemeasures_type.csv', list)
# kept_cvs_col(filename, 'kept_nodemeasures_type.csv', list)
############################################################################


##############################################################################################
# #去除空行(暂不好用)
# def delblankline(infile, outfile):
#     infp = open(infile, "r")
#     outfp = open(outfile, "w")
#     lines = infp.readlines()
#     for li in lines:
#         if li.split():
#             outfp.writelines(li)
#     infp.close()
#     outfp.close()
#
# delblankline("deleted_nodemeasures.csv","2.csv")


#################################################################################################

# import os
# import pandas as pd
#
#
# os.chdir('E:')
# if not os.path.exists('20Mnodes.csv'):
#     exit(-1)
# colname = ['id','Rated','Language','Title','Country','Writer','imdbRating','Director','Actors','Year','Genre','Nomination','WinOscar','WinOther','Runtime','imdbVotes']
# nodes = pd.read_csv('20Mnodes.csv',names = colname)
# length = len(nodes['id'])
#
# movie10M = pd.read_csv('movies.dat', sep ='::',names = ['movieId','title','genres'],engine = 'python')
# print(movie10M['movieId'])
# # new =
# print 'nodeid:',nodes['id']
# list = movie10M['movieId'].tolist()
# print 'list:',list
# # nodes = nodes[nodes['id'].isin(list)]
# # print nodes
#
#
# newDF = pd.DataFrame(columns=colname)
# for k in range(0,length):
#     print nodes['id'][k]
#     if nodes['id'][k] in str(list):
#         print 'yes!'
#         newDF = newDF.append
#         print nodes[colname][k]
# print newDF
##########################################
##Extract 10M nodes
# import os
# os.chdir('E:')
# colname = ['id','Rated','Language','Country','Writer','Director','Actors','Genre','Nomination','WinOscar','WinOther']
# file1 = pd.read_csv('movies.dat', sep ='::',names = ['id','title','genres'],engine = 'python')
# file2 = pd.read_csv('20Mnodes_num_comma_deleted.csv',names = colname, sep =' ')
#
#
# # file1 = f1.sort_values(by='id')
# # file2 = f2.sort_values(by='id')
#
# # file1 = f1['id']
# # file2 = f2['id']
#
# # attr1 = file1.columns.values
# # attr2 = file2.columns.values
#
# # print 'attr1:', attr1
# # print 'attr2:', attr2
# # test = file1.join(file2)
# # test = pd.concat([file1,file2], axis = 1, join='outer')
#
# need_append_list = []
# other_append_list = []
# # if file1['id'].equals(file2['id']):
# #     need_append_list.append(a)
# #     # pass
#
# # for a in attr1:
# #     if a not in attr2:
# #         other_append_list.append(a)
# #
# # for a in attr1:
# #     if a in attr2:
# #         need_append_list.append(a)
# #
#
#
# # find ids which are in left & not in right
# need_append_list = [str(i) for i in file1['id'].values if str(i) in file2['id'].values]
# print 'file1id:',file1['id']
# # find ids which are not in left & in right
# other_append_list = [str(i) for i in file1['id'].values if str(i) not in file2['id'].values]
# print 'file2id:',file2['id']
# print 'need:',need_append_list
# print 'other',other_append_list
#
# file3 = pd.DataFrame()
# length = len(file2['id'])
# # keep the rows matches to file1
# for i in need_append_list:
#     # print file2['id'][int(i)]
#     for k in range(0,length):
#         if file2['id'][k] == str(i):
#             # file2.drop(k)
#             # file3.loc[:,k] = file2['id'][k]
#             # file3[:, k] = file2[:,k]
#             file3 = file2[file2['id'].isin(need_append_list)]    #Select the lines which supports the list
#             print k
#
#
#
#     # file2 = file2[file2.id == str(i)]
# # print file2
# #
# # # add the rows in left & not in right
# # index = file2.size
# # for i in xrange(len(ret1)):
# #     file2.loc[index] = ''
# #     index += 1
# #
# # # add attr not in left & in right
# # for l in need_append_list:
# #     file1[l] = file2[l]
# #
# file3.to_csv('test.csv', index=False, name = False)


#根据某列内容决定输出到不同文件夹，输出txt名称为行id
# # os.chdir('E:')
# if not os.path.exists('1.csv'):
#     exit(-1)
# colname = ['ID','class','text']
# nodes = pd.read_csv('1.csv',names = colname, header=None ,sep = ',',engine = 'python')
# length = len(nodes['ID'])
# print length
#
#
# newDF = pd.DataFrame(columns=['text'])
# for k in range(0,length):
#     print(nodes['ID'][k])
#     # print(nodes['class'][k])
#     if nodes['class'][k] == 0:
#         print('class 0')
#         newDF = nodes['text'][k]
#         print(nodes['text'][k])
#         # print(type(newDF))
#         text_file = open('./0/' + nodes['ID'][k] + '.txt', "w")
#         text_file.write(nodes['text'][k])
#         text_file.close()
#     if nodes['class'][k] == 1:
#         print('class 1')
#         newDF = nodes['text'][k]
#         print(nodes['text'][k])
#         # print(type(newDF))
#         text_file = open('./1/' + nodes['ID'][k] + '.txt', "w")
#         text_file.write(nodes['text'][k])
#         text_file.close()
#
# # print(text_file)



#################################################################
#转Json file to CSV file
# import csv
# import json
# import pandas as pd
# """
# x = [
# {
#   "usage": {
#     "text_units": 1,
#     "text_characters": 37,
#     "features": 1
#   },
#   "language": "en",
#   "emotion": {
#     "targets": [
#       {
#         "text": "apples",
#         "emotion": {
#           "sadness": 0.028574,
#           "joy": 0.859042,
#           "fear": 0.02752,
#           "disgust": 0.017519,
#           "anger": 0.012855
#         }
#       },
#       {
#         "text": "oranges",
#         "emotion": {
#           "sadness": 0.514253,
#           "joy": 0.078317,
#           "fear": 0.074223,
#           "disgust": 0.058103,
#           "anger": 0.126859
#         }
#       }
#     ],
#     "document": {
#       "emotion": {
#         "sadness": 0.32665,
#         "joy": 0.563273,
#         "fear": 0.033387,
#         "disgust": 0.022637,
#         "anger": 0.041796
#       }
#     }
#   }
# }
# ]
# """
#
# #Load the original data
# colname = ['ID','class','text']
# nodes = pd.read_csv('idea2.csv',names = colname, header=None ,sep = ',',engine = 'python')
# length = len(nodes['ID'])
#
# #Load the json data
# x = json.loads(open("test.json", "r").read())
# f = csv.writer(open("test.csv", "wb+"))
#
# # Write CSV Header, If you dont need that, remove this line
# f.writerow(["ID","class","text","sadness", "joy", "fear", "disgust", "anger"])
#
# for x in x:
#     f.writerow([nodes['ID'][0],
#                 nodes['class'][0],
#                 nodes['text'][0],
#                 x["emotion"]["document"]["emotion"]["sadness"],
#                 x["emotion"]["document"]["emotion"]["joy"],
#                 x["emotion"]["document"]["emotion"]["fear"],
#                 x["emotion"]["document"]["emotion"]["disgust"],
#                 x["emotion"]["document"]["emotion"]["anger"]])


#############################################################################
# #Watson API循环发送数据请求（一列）
# import json as json_import
# import platform
# import os
# import requests
# import sys
# from requests.structures import CaseInsensitiveDict
# import dateutil.parser as date_parser
#
# try:
#     from http.cookiejar import CookieJar  # Python 3
# except ImportError:
#     from cookielib import CookieJar  # Python 2
#
# import json
# from watson_developer_cloud import NaturalLanguageUnderstandingV1
# # import natural_language_understanding_v1
# from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions
# # from natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions
#
# text_file = open('jFile.json', "w")
# #Load the original data
# colname = ['ID','class','text']
# nodes = pd.read_csv('idea2.csv',names = colname, header=None ,sep = ',',engine = 'python')
# length = len(nodes['ID'])
# #Start interating through the file
# for k in range(0,length):
#   natural_language_understanding = NaturalLanguageUnderstandingV1(
#     url='https://gateway.watsonplatform.net/natural-language-understanding/api',
#     username='75ef35e3-069e-44fe-b5d2-5f5f339d96a6', password='QDjWRR1WTGII', version='2017-02-27')
#   response = natural_language_understanding.analyze(
#     text=nodes['text'][k],
#     features=Features(
#       entities=EntitiesOptions(
#         emotion=True,
#         sentiment=True,
#         limit=2),
#       keywords=KeywordsOptions(
#         emotion=True,
#         sentiment=True,
#         limit=2)))
#
#   print(json.dumps(response, indent=2))
#   text_file.write('[')
#   text_file.write(json.dumps(response, indent=2))
#   text_file.write(']')
#
# text_file.close()


################################################################################
# 将多个txt文件中的内容合并到一个txt file中
# import glob
# import re
#
# # For y folder
# # 采用glob模块匹配出目标文件夹下的所有txt后缀名的文件
# txt_filenames = glob.glob(r'./txt output_final/y/*.txt')
# print( txt_filenames)
#
# # 将每个txt文件中的信息放在一行中，并存储到目标文件中
# fileout = open(r'./txt output_final/y/y_all.txt','w+') # 注意：AllDiary.txt需要是已经创建过的文件
# for i in range(len(txt_filenames)):
#     txt_file = open(txt_filenames[i], 'r') # 可以转码成txt_filenames[i].decode('utf-8')，也可以不转码
#     buf = txt_file.read()  # the context of txt file saved to buf
#     content = buf.replace("\n", " ").strip()
#     p = content
#     fileout.write(p)
#     fileout.write('\n\n')
#     txt_file.close()
# fileout.close()

################################################################################
# 将csv文件中的一列extract到多个txt文件中
# import csv
# import sys
# import pandas as pd
# import re
# import string

# Extract csv column to txt files.
# print(sys.getdefaultencoding())
# csv_file = "./mypersonality_final_classifiedByClass_onlyColumn.csv"
#
# def _removeNonAscii(s): return "".join(i for i in s if ord(i)<128)
#
# content=pd.read_csv(csv_file,encoding='cp1252')    # This is special character friendly!!
# i =0
# printable = set(string.printable)
# for row in content.values:
#     filter(lambda x: x in printable, row)
#     if i <= 2442:
#         file_title = './txt output/y{}.txt'.format(i)
#         filter(lambda x: x in printable, row)
#         # s = row.encode('ascii', errors='ignore')
#         row.tofile(file_title, sep=",", format="%s")
#     else:
#         file_title = './txt output/n{}.txt'.format(i-2443)
#         filter(lambda x: x in printable, row)
#         # s = row.encode('ascii', errors='ignore')
#         row.tofile(file_title, sep=",", format="%s")
#     i += 1