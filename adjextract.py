# encoding='utf-8'


import jieba
import string
import sys
import os
import csv
import jieba.posseg as pseg

jieba.enable_paddle()

jieba.load_userdict("路径/dict_baidu_utf8.txt")
jieba.load_userdict("路径/dict_pangu.txt")
jieba.load_userdict("路径/dict_sougou_utf8.txt")
jieba.load_userdict("路径/dict_tencent_utf8.txt")
jieba.load_userdict("路径/SogouLabDic.txt")

stopwords = {}.fromkeys([ line.rstrip() for line in open('路径/Stopword.txt',encoding='utf-8' )])
with open('.csv',encoding='utf-8')as csvfile:
        reader=csv.reader(csvfile)
        column=[row[4] for row in reader]

index_weibo = len(column)



def get_data(index_weibo):
   
    
    result=[]

    #seg = jieba.lcut(column[index_weibo],cut_all=False)
    words=pseg.cut(column[index_weibo],use_paddle=True)

    for i,flag in words:
        if i not in stopwords:
          if flag=="a":
            h=""
            h=i+flag
            #print(h)
            result.append(h)
    
    #fo=open('/content/drive/MyDrive/characteranalyse/character_full.dat','a+',encoding='utf-8')
    header=['name']
    with open('/content/drive/MyDrive/characteranalyse/character_full.csv','a+',encoding='utf-8-sig',newline='') as file_obj:
      writer=csv.writer(file_obj)
      writer.writerow(header)
      for p in result:
        writer.writerow([p])
    #for j in result:
     #   fo.write(j)
      #  fo.write(' ')
    
    #fo.write('\r\n')
    #fo.close()
        
    

if __name__=='__main__':

    total_weibo= index_weibo
    print("进程开始...")
    for index_weibo in range(1,total_weibo):
        
        get_data(index_weibo)
       
        
    print("Done!")
