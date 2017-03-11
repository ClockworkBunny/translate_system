"""
main file to excute translation

Author: 
Rui Zhao rzhao001@e.ntu.edu.sg
"""
from mstranslator import Translator
from nltk import word_tokenize
import xlrd
from trans_function import trans_title
from rule_function import product_extract, brand_extract, descrprop_extract
import sys


if __name__=="__main__":    
		key_user = sys.argv[1]
		print key_user
		def dict_mapping(word, key=key_user):
				translator = Translator(key)
				return translator.translate(word, lang_from='en', lang_to='th')    
		
		file = open('resource\\product_names.txt', 'r')
		template_producets = file.readlines()
		template_producets = [word.rstrip() for word in template_producets]  #prduct templates collection


		xl_workbook = xlrd.open_workbook('Product MT - Data.xlsx')
		sheet_names = xl_workbook.sheet_names()
		xl_text = xl_workbook.sheet_by_name('Sample-Data')
		corpus_text = []
		for row_idx in range(1, 51):    
				corpus_text.append(xl_text.cell(row_idx, 1).value)
	
		text_file = open("Output.txt", "w")
		for sen in corpus_text:
				list_words = word_tokenize(sen)
				tt = product_extract(list_words,template_producets)
				idx_brand = brand_extract(list_words)
				idx_descr = descrprop_extract(list_words)
				thai_title = trans_title(list_words,tt,dict_mapping, idx_brand, idx_descr)

				for word in thai_title:
						text_file.write(word.encode('utf-8'))
						text_file.write(' ')
				text_file.write('\n')

		text_file.close()