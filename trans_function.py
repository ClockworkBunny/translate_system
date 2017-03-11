# -*- coding: utf-8 -*-
def trans_word(word, dict_mapping):
	"""based on bing translator api, map english word to thai word
    Only word that contain only letters and is not capitalized will be mapped
    the others will be kept as the same.
    # Arguments
        word: the input english word.
        key: the key to access bing translator API
	"""
	if word.isalpha() and not word.isupper():
		return dict_mapping(word)
	else:
		return word



def trans_title(list_words,idx_product,dict_mapping, idx_brand=None, idx_descr=None):
	"""map each word in the input title to thai word and arrange them in order.
    # Arguments
        list_words: the tokenzied product title which is a list
        idx_product: the index of the product title in list_words
        idx_brand: the index of the brand name in list_words
        idx_descr: the index of the descrpition preposition in list_words
        			here the preposition is defined as "for" or "with". 
        The idx_brand and idx_descr could be none.

	# Example
    Consider a product title: Sony Walkman Digital Player 
        - list_words = ['Sony', 'Walkman', 'Digital', 'Player']
        - idx_product = 3, idx_brand = 0, idx_descr = None
    ```python
    	list_words = ['Sony', 'Walkman', 'Digital', 'Player']
        thai_title = trans_title(list_words, 3, 0)
    ```
	"""	

	translated_sen = []
	translated_idx = []
	th_descr_words = []
	
	if idx_descr is not None:
		if idx_descr>0:
			des_idx = range(idx_descr, len(list_words))
			if idx_product in des_idx:
				des_idx.remove(idx_product)
			if idx_brand in des_idx:
				des_idx.remove(idx_product)
			translated_idx = translated_idx + des_idx
			descr_words = [list_words[i] for i in des_idx]
			for word in descr_words:
				th_descr_words.append(trans_word(word, dict_mapping))
	if idx_brand is not None:
		translated_idx.append(idx_brand)
		translated_sen.append(list_words[idx_brand])
	translated_sen.append(trans_word(list_words[idx_product], dict_mapping))
	indices = [i for i, x in enumerate(list_words) if x == list_words[idx_product]]
	if len(indices)>1:
		translated_idx = translated_idx+indices
		rest_idx = [idx for idx in range(len(list_words)) if idx not in translated_idx]	
		th_product = trans_word(list_words[idx_product], dict_mapping)
		#ranking_idx
		right_idx = [idx for idx in rest_idx if idx<indices[0]]
		left_idx = [idx for idx in rest_idx if idx>indices[-1]]
		middle_idx = [idx for idx in rest_idx if idx>indices[0] and idx<indices[-1] and idx not in indices and list_words[idx] != 'and']
		if len(right_idx)>0 and len(middle_idx)==0:
			for idx in right_idx:  
				translated_sen.append(trans_word(list_words[idx], dict_mapping))
		if len(middle_idx)>0:
			dist_pro = []
			all_idx = middle_idx
			for idx in middle_idx:
				dist_middle = [i-idx for i in indices[1:] if i-idx>0]
				dist_pro.append(min(dist_middle))			
			if len(right_idx) >0:
				dist_right = [indices[0]-i for i in right_idx]
				dist_pro = dist_pro + dist_right
				all_idx = all_idx + right_idx
			idx_sorted = sorted(range(len(dist_pro)), key=dist_pro.__getitem__)
			new_idx = [all_idx[i] for i in idx_sorted]
			for idx in new_idx:
				translated_sen.append(trans_word(list_words[idx], dict_mapping))

		if len(left_idx)>0:
			for idx in left_idx:
				translated_sen.append(trans_word(list_words[idx], dict_mapping))
	else:
		translated_idx.append(idx_product)
		rest_idx = [idx for idx in range(len(list_words)) if idx not in translated_idx]
		#ranking idx
		right_idx = [idx for idx in rest_idx if idx<idx_product]
		left_idx = [idx for idx in rest_idx if idx>idx_product]
		
		
		if len(right_idx)>0:
			for idx in right_idx:
				translated_sen.append(trans_word(list_words[idx],dict_mapping))

		if len(left_idx)>0:
			for idx in left_idx:
				translated_sen.append(trans_word(list_words[idx], dict_mapping))
	if idx_descr is not None and idx_descr>0: 
			translated_sen = translated_sen  + th_descr_words
	return translated_sen
