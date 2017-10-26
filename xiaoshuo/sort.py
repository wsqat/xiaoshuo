# -*- coding: utf-8 -*-
import csv
import pandas as pd
import numpy as np
import sys
reload(sys)
# sys.setdefaultencoding('utf-8')
sys.setdefaultencoding('utf_8_sig')

# 生成cvs文件, 过滤数据, 清洗数据 
# del_cvs_row('20171023.csv', 'rank_click_month_after.csv')
# hotRowNum = 0
def pure_cvs_row(fname, newfname, delimiter=',',key='month'):
    with open(fname) as csvin, open(newfname, 'w') as csvout:
        reader = csv.reader(csvin, delimiter=delimiter)
        # print reader
        # rows = [row for row in reader]
        rows = []
        writer = csv.writer(csvout, delimiter=delimiter)
        for row in reader:
            row_len = len(row)
            if row_len == 9:
                # print row_len
                # print row[0]
                # 加权处理，增加热门作者
                # global hotRowNum
                # hotRowNum += 1
                # if hotRowNum == 1:
                    # row[8] = 'month'
                # else:
                # 	# row[8] = str(float(row[6])*0.5 + float(float(row[7])*0.3) + float(row[8])*0.2)
                # 	# row[8] = float(row[6])*0.5 + 
                	# row[8] = float(row[6])*0.7 + float(row[7])*0.3
                rows.append(row)
        writer.writerows(rows)
    # if key == 'author':
    # 	sort_by_key(newfname,"rank_"+key+".csv",'author')
    # else:
    sort_by_key(newfname,"rank_"+key+".csv",key)

# 生成cvs文件 key按照什么排序
def sort_by_key(fname,newfname,key):
    # df = pd.read_csv('novels.csv',header=0,usecols=[0,1,6,7,8])
    # df = pd.read_csv('rank_click_month_after.csv',header=0,usecols=[0,1,6,7,8],low_memory=False)
    df = pd.read_csv(fname,header=0,usecols=[0,1,6,7,8],low_memory=False)
    lc = pd.DataFrame(df)
    lc = lc.dropna(axis=0)
    # lc = lc[lc['month']!=u'热血传奇']
    # df[(True-df['appID'].isin([278,382]))] 
    # lc=lc.drop_duplicates(['userName'])
    # new = lc.sort_values(by=['month'],ascending=True)
    # new = new.tail(20)
    if key == 'author':
    	# lc = lc.iloc[:,[1,3]]
        lc = lc.groupby(by=['author'])['collects'].sum()
        lc = lc.to_frame()
        new = lc.sort_values(by=['collects'],ascending=False)
        new = new.head(20)
        # print new
        new.to_csv('热门小说作者排行榜.csv', sep=',', encoding='utf-8-sig')
        return 
    else:
        new = lc.sort_values(by=[''+key+''],ascending=False)
    new = new.head(20)
    new.to_csv(newfname, sep=',', encoding='utf-8-sig')
    
    if key == 'month':
        newfname2 = "本月点击排行榜.csv"
    elif key == 'reviews':
        newfname2 = "历史点击排行榜.csv"
    elif key == 'collects':
        newfname2 = "历史收藏排行榜.csv"
    # else:
    #    newfname2 = "热门小说作者排行榜.csv"

    del_cvs_col(newfname, newfname2, [0])

# 生成cvs文件, 删除指定列数
# del_cvs_col('rank_click_month.csv', '本月点击排行榜.csv', [0])
def del_cvs_col(fname, newfname, idxs, delimiter=','):
    with open(fname) as csvin, open(newfname, 'w') as csvout:
        reader = csv.reader(csvin, delimiter=delimiter)
        writer = csv.writer(csvout, delimiter=delimiter)
        rows = (tuple(item for idx, item in enumerate(row) if idx not in idxs) for row in reader)
        writer.writerows(rows)


# 生成cvs文件, 加权处理，增加
# del_cvs_col('rank_click_month.csv', '本月点击排行榜.csv', [0])
# def del_cvs_col(fname, newfname, idxs, delimiter=','):
#     with open(fname) as csvin, open(newfname, 'w') as csvout:
#         reader = csv.reader(csvin, delimiter=delimiter)
#         writer = csv.writer(csvout, delimiter=delimiter)
#         rows = (tuple(item for idx, item in enumerate(row) if idx not in idxs) for row in reader)
#         writer.writerows(rows)


if __name__ == '__main__':
    
    # 本月点击排行榜
    pure_cvs_row('20171023.csv', 'pure_data.csv', delimiter=',', key='month')
    # 历史点击排行榜
    # pure_cvs_row('20171023.csv', 'pure_data.csv', delimiter=',', key='reviews')
    # 历史收藏榜
    # pure_cvs_row('20171023.csv', 'pure_data.csv', delimiter=',', key='collects')
    # 热门作者
    # pure_cvs_row('20171023.csv', 'pure_data.csv', delimiter=',', key='author')

# import matplotlib.pyplot as plt
# plt.rcdefaults()
# present = new.set_index('novel_name')
# present[:20].plot(kind='barh')
# # plt.figure(figsize=(12,9))
# plt.title(u'热门小说本月点击排行榜', fontsize=16)
# plt.xlabel(u'热门小说本月点击量', fontsize=16)
# plt.ylabel(u'热门小说名称', fontsize=16)
# plt.show()

# 历史点击排行榜，
# lc2 = pd.DataFrame(df)
# lc2 = lc2.iloc[:,[0,3]]
# new2 = lc2.sort_values(by=['reviews'],ascending=True)
# new2 = new2.tail(20)
# present = new2.set_index('novel_name')
# present[:20].plot(kind='barh')
# plt.title(u'热门小说历史点击排行榜', fontsize=16)
# plt.xlabel(u'热门小说历史点击量', fontsize=16)
# plt.ylabel(u'热门小说名称', fontsize=16)
# plt.show()

# 历史收藏榜，
# lc3 = pd.DataFrame(df)
# lc3 = lc3.iloc[:,[0,2]]
# new3 = lc3.sort_values(by=['collects'],ascending=True)
# new3 = new3.tail(20)
# present = new3.set_index('novel_name')
# present[:20].plot(kind='barh')
# plt.title(u'热门小说历史收藏榜', fontsize=16)
# plt.xlabel(u'热门小说历史收藏量', fontsize=16)
# plt.ylabel(u'热门小说名称', fontsize=16)
# plt.show()

# 热门作者，
# lc4 = pd.DataFrame(df)
# lc4 = lc4.iloc[:,[1,3]]
# lc4 = lc4.groupby(by=['author'])['reviews'].sum()
# # 生成的数据类型是Series,如果进一步需要将其转换为dataframe,可以调用Series中的to_frame()方法.
# lc4 = lc4.to_frame()
# new4 = lc4.sort_values(by=['reviews'],ascending=False)
# new4 = new4.head(20)
# print new4
# present = new4.set_index('author')
# present[:20].plot(kind='barh')
# plt.title(u'热门小说作者排行榜', fontsize=16)
# plt.xlabel(u'热门小说作者点击量', fontsize=16)
# plt.ylabel(u'热门小说作者', fontsize=16)
# plt.show()

