"""
Key Information Extraction from Product Titles

Author: 
Rui Zhao rzhao001@e.ntu.edu.sg
"""
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
import re
from google import google
import time
import random


def product_extract(list_words, template_products):
	"""extract the idx behind product name.
    # Arguments
        list_words: the input english word.
        template_products: the seed collection of products
	"""	
	low_ver = [word.lower() for word in list_words]

	indice_for = [i for i in range(len(low_ver)) if low_ver[i]=='for'] 
	indice_with = [i for i in range(len(low_ver)) if low_ver[i]=='with']

	product_indices = []
	if len(indice_for)>0 and indice_for[0]>0:
		product_indices.append(indice_for[0] - 1)
	if len(indice_with)>0 and indice_with[0]>0:
		product_indices.append(indice_with[0] - 1)
	
	words_all = set(list_words)
	sharedwords = words_all.intersection(template_products)

	#matching words in seed collection
	if len(sharedwords)>0:
		for word in sharedwords:
			sub_indces = [ i for i, word_tar in enumerate(list_words) if word_tar == word ]
			product_indices = product_indices + sub_indces
	
	##no rule is activated, return the last normal englis words (not captalized, normal)
	if len(product_indices) == 0:
		for idx in reversed(range(len(list_words))):
			if list_words[idx].isalpha() and not list_words[idx].isupper():
				return idx
	##rule is activated, select the one word that hits the most ruls. Else, the last word in these extracted word
	##is selected. 
	if len(product_indices) > 0:
		product_indices_all = list(set(product_indices))
	
		if len(product_indices_all) == 1:
			return product_indices_all[0]
		else:
			max_value = 1
			final_indice = max(product_indices_all)
			for i in product_indices_all:
				if product_indices.count(i)>max_value:
					max_value = product_indices.count(i)
				final_indice = i
			return final_indice

def brand_extract(list_words):
	"""extract the idx behind brand name.
    the third-party google search API is adopted. If it is banned, it will print information
    # Arguments
        list_words: the input english word.
	"""
	time_stop = random.randint(1, 10)
	time.sleep(time_stop)
	query = list_words[0]
	if query.isalpha():
			num_page = 1
			search_results = google.search(query, num_page)
			try:
				query_results = search_results[0]
				web_name = search_results[0].name
				link_name = search_results[0].link
				infor_words = re.compile('\w+').findall(link_name)
				names_web = [name.lower() for name in web_name.split(' ')]
				judge_name = 'Dictionary'  not in web_name and 'Wikipedia' not in web_name
				if (names_web[0] == query.lower() or query.lower() in infor_words) and judge_name:  
					return 0
				else:
					return None
			except:
				print 'google API is banned'
				return None
	else:
		return None


def descrprop_extract(list_words):
	"""extract the idx behind words such as for or with.
    # Arguments
        list_words: the input english word.
	"""
	idx_descr = [i for i, value in enumerate(list_words) if value.lower() in ['for', 'with'] ]

	if len(idx_descr)>0:
		return idx_descr[0]
	else:
		return None