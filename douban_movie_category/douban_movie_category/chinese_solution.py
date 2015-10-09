import jieba

def cut_word(sentence,mode=1):
	sentence=unicode(sentence)
	if mode==1:
		sentence=sentence.replace(" ","")
		words=jieba.cut(sentence,cut_all=True)
		for word in list(words):
	                print unicode(word)

		return list(words)
	else:
		words=jieba.cut(sentence,cut_all=True)
		for word in list(words):
	                print unicode(word)

		return list(words)
	
	for word in list(words):
		print unicode(word)
	
