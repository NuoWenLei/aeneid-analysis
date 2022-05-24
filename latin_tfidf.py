import json, os
from nltk import word_tokenize
from tqdm import tqdm
from sklearn.feature_extraction.text import TfidfVectorizer

def to_list(txt):
	word_list = []
	for line in txt.split("\n"):
		word_list.extend([w for w in word_tokenize(line) if len(w) >= 4])
	
	return word_list

def filter_doc(tokens):
	cleaned_doc = []
	for w in tokens:
		if len(w) > 1:
			cleaned_doc.append(w)
	return " ".join(cleaned_doc)

def main():
	full_documents = []
	# paragraph_documents = []
	for fp in tqdm(os.listdir("latin_aeneid_books")):
		with open(f"latin_aeneid_books/{fp}", "r") as book_read:
			txt = book_read.read()
		full_documents.append(filter_doc(to_list(txt)))
		# paragraph_documents.extend(txt.split("\n\n"))
	
	doc_tfidf_vectorizer = TfidfVectorizer(ngram_range=(1,3), min_df=1, stop_words = None)
	doc_tfidf = doc_tfidf_vectorizer.fit_transform(full_documents)
	doc_feature_names = doc_tfidf_vectorizer.get_feature_names()
	doc_freq_dict_list = []

	for i in range(len(doc_tfidf.indptr) - 1):
		freq_dict = {}
		ind = doc_tfidf.indices[doc_tfidf.indptr[i]:doc_tfidf.indptr[i+1]]
		data = doc_tfidf.data[doc_tfidf.indptr[i]:doc_tfidf.indptr[i+1]]
		for i, d in zip(ind, data):
			freq_dict[doc_feature_names[i]] = float(d)
		
		doc_freq_dict_list.append(freq_dict)
	
	for i, freq in enumerate(doc_freq_dict_list):
		with open(f"tfidf_features_latin/book_{i + 1}.json", "w") as feature_json:
			json.dump(freq, feature_json)

if __name__ == "__main__":
	main()


	
	# paragraph_tfidf_vectorizer = TfidfVectorizer()
	# paragraph_tfidf = paragraph_tfidf_vectorizer.fit_transform(paragraph_documents)



	

		
		
