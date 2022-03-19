#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 09:59:46 2018

@author: Ming JIN
"""
from snownlp import sentiment

sentiment.train('C:\\Users\\moban\\Documents\\Cassis\\weibo-search\\step4_sentiments\\train_model\\negative_dict.txt', 'C:\\Users\\moban\\Documents\\Cassis\\weibo-search\\step4_sentiments\\train_model\\positive_dict.txt')
sentiment.save('C:\\Users\\moban\\Documents\\Cassis\\weibo-search\\step4_sentiments\\train_model\\sentiment.marshal')