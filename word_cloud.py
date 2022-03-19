#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 15:06:18 2017
@author: Ming JIN
"""
import jieba.analyse
from PIL import Image, ImageSequence
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from wordcloud import WordCloud, ImageColorGenerator

# import matplotlib.mlab as mlab

font = FontProperties(fname="Songti.ttc")
bar_width = 0.5
lyric = ""

f = open("C:\\Users\\moban\\Documents\\Cassis\\Weibo-Analyst-master\\step3_word_cloud\\嬛帮果.dat", "r")
stopword = ["网页", "链接", "电视剧", "官方", "卫视", "播出", "热播", "视频", "粉丝团", "后宫"]


content = ""
with open("C:\\Users\\moban\\Documents\\Cassis\\Weibo-Analyst-master\\step3_word_cloud\\嬛帮果.dat", "r") as file:
    content = file.read()
    for word in stopword:
        content = content.replace(word, "")
with open("C:\\Users\\moban\\Documents\\Cassis\\Weibo-Analyst-master\\step3_word_cloud\\嬛帮果.dat", "w") as file:
    file.write(content)


# for i in f:
# lyric += i

lyric = content

result = jieba.analyse.textrank(lyric, topK=50, withWeight=True)

keywords = dict()
for i in result:
    keywords[i[0]] = i[1]
print(keywords)

image = Image.open("C:\\Users\\moban\\Documents\\Cassis\\Weibo-Analyst-master\\step3_word_cloud\\background.png")
graph = np.array(image)
wc = WordCloud(font_path="Songti.ttc", background_color="White", max_words=50, mask=graph)
wc.generate_from_frequencies(keywords)
image_color = ImageColorGenerator(graph)
plt.imshow(wc)
plt.imshow(wc.recolor(color_func=image_color))
plt.axis("off")
plt.show()
wc.to_file("output.png")

X = []
Y = []

for key in keywords:

    X.append(key)
    Y.append(keywords[key])

num = len(X)

fig = plt.figure(figsize=(28, 10))
plt.bar(range(num), Y, tick_label=X, width=bar_width)
# plt.xlabel("X-axis",fontproperties=font)
# plt.ylabel("Y-axis",fontproperties=font)
plt.xticks(rotation=50, fontproperties=font, fontsize=20)
plt.yticks(fontsize=20)
plt.title("words-frequency chart", fontproperties=font, fontsize=30)
plt.savefig("barChart.jpg", dpi=360)
plt.show()
