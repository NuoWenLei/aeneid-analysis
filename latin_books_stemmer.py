import os, lookup, json
from tqdm import tqdm
from nltk import word_tokenize

def to_list(txt):
	word_list = []
	for line in txt.split("\n"):
		word_list.extend([w for w in word_tokenize(line) if len(w) >= 4])
	
	return word_list

def main():
	for fp in tqdm(os.listdir("latin_aeneid_books")):
		with open(f"latin_aeneid_books/{fp}", "r") as txt_read:
			txt = txt_read.read()

		word_list = to_list(txt)

		stem_list = []

		for w in word_list:
			matches = lookup.match_word(w)

			if len(matches) == 0:
				continue

			if len(matches[0][2]["stem1"]) != 0:
				stem_list.append(matches[0][2]["stem1"])
		
		with open(f"latin_books_stem_encoded/{fp.split('.')[0]}.json", "w") as json_stem:
			json.dump(stem_list, json_stem)

if __name__ == "__main__":
	main()
