import gensim, os, re, json
import gensim.corpora as corpora
from nltk.corpus import stopwords
from gensim.utils import simple_preprocess
from tqdm import tqdm
from pprint import pprint

stop_words = stopwords.words('english')
stop_words.extend(["take", "make", "give", "break", "hold", "see", "run", "bear", "head", "draw", "call", "get", "thus", "thy", "said"])


def main():

	# Load data

	paragraphs = []
	books = []
	for fp in os.listdir("aeneid_books"):

		with open(f"aeneid_books/{fp}", "r") as aeneid_txt:
			txt = aeneid_txt.read()
			paragraphs.extend([re.sub('[,\.!?]', '', p.replace("\n", " ")) for p in txt.split("\n\n")])
		books.append(re.sub('[,\.!?]', '', txt.replace("\n", " ")))
	print(len(paragraphs))
	print("\n")
	data_words = list(sent_to_words(paragraphs))

	data_books = list(sent_to_words(books))
	# remove stop words
	data_words = remove_stopwords(data_words)

	data_books = remove_stopwords(data_books)

	id2word = corpora.Dictionary(data_words)

	texts = data_words

	corpus = [id2word.doc2bow(text) for text in texts]

	num_topics = 25

	lda_model = gensim.models.LdaMulticore(corpus=corpus,
                                       id2word=id2word,
                                       num_topics=num_topics)

	pprint(lda_model.print_topics())

	topics = [(i, [[id2word[term_id], float(val)] for term_id, val in lda_model.get_topic_terms(i, topn=15)]) for i in range(num_topics)]

	topic_dictionary = dict(topics)

	with open("aeneid_books_topic_modeling/topic_dictionary.json", "w") as topic_dict_json:
		json.dump(topic_dictionary, topic_dict_json)

	for i, b in enumerate(data_books):
		with open(f"aeneid_books_topic_modeling/topics_{i + 1}.json", "w") as topic_json:
			lda_res = lda_model[[id2word.doc2bow(b)]]
			json.dump([[int(l[0]), float(l[1])] for l in lda_res[0]], topic_json)

def sent_to_words(sentences):
    for sentence in sentences:
        # deacc=True removes punctuations
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))

def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc)) 
             if word not in stop_words] for doc in texts]

if __name__ == "__main__":
	main()