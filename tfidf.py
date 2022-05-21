import json, os, nltk, ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download('stopwords')
nltk.download("averaged_perceptron_tagger")
from nltk import pos_tag, word_tokenize
from nltk.corpus import stopwords
from tqdm import tqdm
from sklearn.feature_extraction.text import TfidfVectorizer

def filter_doc(pos_tags, allowed_pos = ["NN", "JJ", "VB", "VBP", "NNP", "NNS", "RB", "RBR", "RBS", "VBD", "VBG", "VBN", "VBP", "VBZ"]):
	cleaned_doc = []
	for w, p in pos_tags:
		if p in allowed_pos:
			cleaned_doc.append(w)
	return " ".join(cleaned_doc)

def main():
	stops = stopwords.words('english')
	stops.extend(["take", "make", "give", "break", "hold", "see", "run", "bear", "head", "draw", "call", "get", "thus", "thy", "said"])

	full_documents = []
	# paragraph_documents = []
	for fp in tqdm(os.listdir("aeneid_books")):
		with open(f"aeneid_books/{fp}", "r") as book_read:
			txt = book_read.read()
		full_documents.append(filter_doc(pos_tag(word_tokenize(txt))))
		# paragraph_documents.extend(txt.split("\n\n"))
	
	doc_tfidf_vectorizer = TfidfVectorizer(ngram_range=(1,3), min_df=1, stop_words = stops)
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
		with open(f"tfidf_features/book_{i + 1}.json", "w") as feature_json:
			json.dump(freq, feature_json)

if __name__ == "__main__":
	main()


	
	# paragraph_tfidf_vectorizer = TfidfVectorizer()
	# paragraph_tfidf = paragraph_tfidf_vectorizer.fit_transform(paragraph_documents)



	

		
		
