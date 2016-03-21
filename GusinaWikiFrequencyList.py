# -*- coding: utf-8 -*-
'''

Author: Hazova N.
[Gusina Wiki Frequency List]

'''
'''

Для работы программы необходимо наличие папки "dumps" в рабочей директории с загруженными дампами в формате %%name%%.xml 

'''
'''

Для выполнения задания был выбран дамп на языке папьяменто. Папьяме́нто (papiamento или papiamentu) — креольский язык,
родной язык населения Арубы, Кюрасао и Бонэйр. Число говорящих — около 329 тыс. человек. 
По происхождению лексика папьяменто является смесью нидерландского (около 25 % словаря), 
испанского, португальского и сефардского (около 60 %), при участии английского, аравакского и африканских языков. 
Сейчас сильное влияние оказывает английский, которым (как и нидерландским) владеет значительная часть населения, 
а также венесуэльский испанский (особенно на Арубе).

В связи со сложной орфографией в начале словаря возможны незначительные появления отдельных символов 

'''

import os, re, sys

def Wiki(file, D_name):

	main_path = "/home/haniani/Документы/Study/Программирование/Википедия/"
	input_File = main_path + D_name + file
	output_File = main_path + D_name + "WikiOutput/"
	Python2 = "/usr/bin/python2" + " "
	Extractor = main_path + "WikiExtractor.py" + " "
	inputinput = " " + input_File
	outputoutput = "-o" + " " + output_File
	os.system(Python2 + Extractor + outputoutput + inputinput)

def dump_processing():

	file = input("Укажите в кавычках название файла и его расширение: ")
	D_name = "dumps/"    
	Wiki(file, D_name)

if __name__ == "__main__":
	dump_processing()    

def cleaning():

	globalpath = "/home/haniani/Документы/Study/Программирование/Википедия/dumps/WikiOutput/AA/"
	print("Создание файла с очищенным текстом после WikiExtractor...")
	clean_result = open("cleanresult.txt", "w")

	for file in os.listdir(globalpath):
		oldfile = open(globalpath + file, "r")
		newfile = oldfile.readlines()
		
		for line in newfile:
			clean1 = re.sub(r"\<(.+)\>", "", line)
			clean2 = re.sub(r"\n", "", clean1)
			obrabotka = clean_result.writelines(str(clean2) + "\n")

	clean_result.close()

def frequance():

	cleaning()

	allSentences = []
	alli = []
	cr2 = open("text_for_dict.txt", "w")
	alo = re.compile("\n", re.M)
	text = open("cleanresult.txt", "r")
	for line in text:
		if line != "\n":
			alli.append(line.split(" "))
	for x in alli:
		for i in x:
			cr2.write(str(i + " ")) 

	cr2.close()
	os.remove("cleanresult.txt")


def freqdic():

	frequance()

	freqlow = open("/home/haniani/Документы/Study/Программирование/Википедия/text_for_dict.txt", "r")

	txt = freqlow.read()
	freqlow.close

	p = re.compile("([A-Za-zÑÁÉÍÓÚÜñáéíóúü]+)")
	res=p.findall(txt)

	dict1 = {}
	for key in res:
		key = key.lower()
		if key in dict1:
			value = dict1[key]
			dict1[key]=value+1
		else:
			dict1[key]=1

	sortforkeys = sorted(dict1, key=lambda x: int(dict1[x]), reverse=True)

	print("Создание частотного словаря...")
	savefile = open("dictionary+freq.tsv", "w")

	for key in sortforkeys:
		s = str("{0}\t{1}\n").format(key,dict1[key])
		savefile.write(s)
		savefile.close

freqdic()
print('Завершение работы {:V')
sys.exit

