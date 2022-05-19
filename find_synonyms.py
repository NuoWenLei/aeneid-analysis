import nltk, os, json, ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download('wordnet')
from tqdm import tqdm
from nltk.corpus import wordnet as wn

def find_synonyms(word):
	synonyms = [word]
	for syn in wn.synsets(word):
		for l in syn.lemmas():
			if "_" not in l.name():
				synonyms.append(l.name().lower())

	return synonyms

def main():
	for fp in tqdm(os.listdir("aeneid_books")):
		all_syn_words = []
		with open(f"aeneid_books/{fp}", "r") as aeneid_read:
			txt = aeneid_read.read()

		splitted_words = [line.split(" ") for line in txt.split("\n")]

		words = [w for sublist in splitted_words for w in sublist]

		for w in words:
			if len(w.strip()) == 0:
				continue
			all_syn_words.extend(find_synonyms(w))
	
		with open(f"books_synonym_encoded/{fp.split('.')[0]}.json", "w") as json_syns:
			json.dump(all_syn_words, json_syns)

if __name__ == "__main__":
	main()

