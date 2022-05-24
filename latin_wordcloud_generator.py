import wordcloud, os, json
from nltk import word_tokenize
from wordcloud import WordCloud
from tqdm import tqdm
import matplotlib.pyplot as plt

def to_list(txt):
	word_list = []
	for line in txt.split("\n"):
		word_list.extend([w for w in word_tokenize(line) if len(w) >= 4])
	
	return word_list

def main():
	all_w_freq = {}
	total_words = 0
	for fp in tqdm(os.listdir("latin_aeneid_books")):
		curr_w_freq = {}
		with open(f"latin_aeneid_books/{fp}", "r") as txt_read:
			txt = txt_read.read()

		word_list = to_list(txt)

		total_words += len(word_list)
		for w in word_list:
			# if w in stopwords:
			# 	continue
			if w not in curr_w_freq.keys(): 
				curr_w_freq[w] = 1
			else:
				curr_w_freq[w] += 1
			
			if w not in all_w_freq.keys():
				all_w_freq[w] = 1
			else:
				all_w_freq[w] += 1

		for w in curr_w_freq.keys():
			curr_w_freq[w] = float(curr_w_freq[w]) / float(len(word_list))

		wc = WordCloud()

		wc.generate_from_frequencies(curr_w_freq)

		plt.figure(figsize = (14, 7))

		plt.imshow(wc, interpolation = "bilinear")

		plt.savefig(f"latin_wordclouds/{fp.split('.')[0]}.png", format = "png")

	for w in all_w_freq.keys():
			all_w_freq[w] = float(all_w_freq[w]) / float(total_words)

	wc = WordCloud()

	wc.generate_from_frequencies(all_w_freq)

	plt.figure(figsize = (14, 7))

	plt.imshow(wc, interpolation = "bilinear")

	plt.savefig("latin_wordclouds/overall_wordcloud.png", format = "png")


	

if __name__ == "__main__":
	main()

