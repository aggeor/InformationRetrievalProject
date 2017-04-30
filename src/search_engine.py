import os
import re


#file parser
def process_files():
	file_to_terms = {}
	for root, dirs, files in os.walk(os.getcwd()):
		for file in files:
			#parse = open('stopwords.txt')
			#stopwords=parse.read().split()
			#parse.close()
			if file=='search_engine.py' or file=='search_engine.exe':
				continue
			pattern = re.compile('[\W_]+')
			file_to_terms[file] = open(os.path.join(root,file), 'r').read().lower();
		
			file_to_terms[file] = pattern.sub(' ',file_to_terms[file])
			re.sub(r'[\W_]+','', file_to_terms[file])
			file_to_terms[file] = file_to_terms[file].split()
			#file_to_terms[file] = [w for w in file_to_terms[file] if w not in stopwords]
	return file_to_terms

#Indexer for each file
#input = [word1, word2, ...]
#output = {word1: [pos1, pos2], word2: [pos2, pos434], ...}
def index_one_file(termlist):
	fileIndex = {}
	for index, word in enumerate(termlist):
		if word in fileIndex.keys():
			fileIndex[word].append(index)
		else:
			fileIndex[word] = [index]
	return fileIndex

#input = {filename: [word1, word2, ...], ...}
#res = {filename: {word: [pos1, pos2, ...]}, ...}
def make_indices(termlists):
	total = {}
	for filename in termlists.keys():
		total[filename] = index_one_file(termlists[filename])
	return total	

#Inverted Index with posting lists and position inside the file
#input = {filename: {word: [pos1, pos2, ...], ... }}
#res = {word: {filename: [pos1, pos2]}, ...}, ...}
def fullIndex(regdex):
	total_index = {}
	for filename in regdex.keys():
		for word in regdex[filename].keys():
			if word in total_index.keys():
				if filename in total_index[word].keys():
					total_index[word][filename].extend(regdex[filename][word][:])
				else:
					total_index[word][filename] = regdex[filename][word]
			else:
				total_index[word] = {filename: regdex[filename][word]}
	return total_index	

#One word query returns the documents this word belongs to
def one_word_query(word, invertedIndex):
	pattern = re.compile('[\W_]+')
	word = pattern.sub(' ',word)
	if word in invertedIndex.keys():
		return [filename for filename in invertedIndex[word].keys()]
	else:
		return []
#free_text_query_union returns all the documents that the words in the 
#query belong to
def free_text_query_union(string):
	pattern = re.compile('[\W_]+')
	string = pattern.sub(' ',string)
	result = []
	for word in string.split():
		result += one_word_query(word,invertedIndex)
	return list(set(result))
#free_text_query_intersection returns only the documents that all words
#appear in
def free_text_query_intersection(string):
	pattern = re.compile('[\W_]+')
	string = pattern.sub(' ',string)
	result = []
	for word in string.split():	
			result = one_word_query(word,invertedIndex)
	return list(set(result))	

#phrase_query returns the documets that the whole phrase appears
def phrase_query(string, invertedIndex):
	pattern = re.compile('[\W_]+')
	string = pattern.sub(' ',string)
	listOfLists, result = [],[]
	for word in string.split():
		listOfLists.append(one_word_query(word,invertedIndex))
	setted = set(listOfLists[0]).intersection(*listOfLists)
	for filename in setted:
		temp = []
		for word in string.split():
			temp.append(invertedIndex[word][filename][:])
		for i in range(len(temp)):
			for ind in range(len(temp[i])):
				temp[i][ind] -= i
		if set(temp[0]).intersection(*temp):
			result.append(filename)
	return result
print("Building index in the current directory : \n \n"+os.getcwd())
print("\n")
p=process_files()
m=make_indices(p)
invertedIndex=fullIndex(m)
print("The index has been build")
print("\n")
while (True):
	query=input("What do you want me to search for?\n(To quit press enter) : ")
	if len(query.split())==1:
		print("\n")
		result=one_word_query(query,invertedIndex)
		if len(result)==0:
			print("The word '"+query+"' was not found in any file.\n")
		else:
			print("The word '"+query+"' was found in the following files : \n")
			for i in enumerate(result):
				print(i)
	elif len(query.split())>1:
		iput=input("Is this a phrase?(y/n)")
		
		if iput=="y":
			result=phrase_query(query,invertedIndex)
			print("\n")
			if len(result)==0:
				print("The phrase you are looking for was not found in any file.\n")
			else:
				print("The phrase '"+query+"' was found in the following files : \n")
				for i in enumerate(result):
					print(i)
		else:
			result=free_text_query_union(query)
			print("\n")
			if len(result)==0:
				print("No word in the query '"+query+"' was found in any of the files.")
			else:
				print("Here are all the documents that at least one of the words was found(Union):\n ")
				for i in enumerate(result):
					print(i)
			print("\n")
			result=free_text_query_intersection(query)
			if len(result)==0:
				print("No file contained all the words in the query '"+query+"'.")
			else:
				print("Here are all the documents that contained all of the words(Intersection):\n ")
				for i in enumerate(result):
					print(i)
	else:
		print("Bye bye!")
		break
	print("\n")	