#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class Card():  #定义Card类
	def __init__(self, suit, rank):#构造函数
		self.suit = suit
		self.rank = rank
		
	suit_name = ("fangkuai^","meihua*","hongtao@","heitao&")# 类属性
	rank_name = ("A",2,3,4,5,6,7,8,9,10,"J","Q","K")
	
	def __str__(self):
		suit = Card.suit_name[self.suit - 1]
		rank = self.rank_name[self.rank - 1]
		return "{:>5} of {:8}".format(rank, suit
		

def chose():
	while True:
		__import__("time").sleep(1.5)
		suit = random.randint(0, 4)
		rank = random.randint(0, 13)
		t = Card(suit,rank)
		yield t
		
t2 = chose()
for i in "123456":
	try:
		print("第%s张牌>>>>>>>>>>>>>>>>>>>>>>>>>>>"%i)
		print(next(t2))
	except:
		pass

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
