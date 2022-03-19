import jieba

from jieba import analyse

tfidf = analyse.extract_tags

for line in open("C:\\Users\\moban\\Documents\\Cassis\\weibo-search\\weibo\\data_full.dat",encoding='utf-8'):
    
    text = line

    keywords = tfidf(text,allowPOS=('ns','nr','nt','nz','nl','n', 'vn','vd','vg','v','vf','a','an','i'))

    result=[]

    for keyword in keywords:
        
        result.append(keyword)

    #print(result)
    fo = open("C:\\Users\\moban\\Documents\\Cassis\\weibo-search\\weibo\\data_keywords.dat", "a+",encoding='utf-8')
    
    for j in result:
          
        fo.write(j)
        fo.write(' ')
     
    fo.write('\r\n')
    fo.close()

print("Keywords Extraction Done!")


