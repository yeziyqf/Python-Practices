import pandas as pd

# import os
# os.chdir('E:');
# df = pd.read_csv('ratings_final.csv',sep = ' ');
# print df.max()



import os
os.chdir('E:');
df = pd.read_csv('edges.dat',sep = ' ',header = None, names = ['col0','col1','col2'],engine = 'python');
# df['col2'] =
length = len(df['col2'])
counters = {}
for i in range(0,length):
    # column[i] = [col[i] for col in reader]
    if  df['col2'][i] in counters:
        counters[df['col2'][i]] +=1
    else
        counters[df['col2'][i]] = 1
print counters,'finished!'