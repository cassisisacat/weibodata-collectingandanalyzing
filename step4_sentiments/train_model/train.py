#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 09:59:46 2018

@author: Ming JIN
"""
from snownlp import sentiment

sentiment.train('路径\negative_dict.txt', '路径\positive_dict.txt')
sentiment.save('路径\sentiment.marshal')
