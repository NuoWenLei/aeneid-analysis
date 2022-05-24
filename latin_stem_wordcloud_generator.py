import wordcloud, os, json
from nltk import word_tokenize
from wordcloud import WordCloud
from tqdm import tqdm
import matplotlib.pyplot as plt

def main():
	all_w_freq = {}
	total_words = 0
	for fp in tqdm(os.listdir("latin_books_stem_encoded")):
		curr_w_freq = {}
		with open(f"latin_books_stem_encoded/{fp}", "r") as json_read:
			word_list = json.load(json_read)

		total_words += len(word_list)
		for w in word_list:
			if len(w) < 4:
				continue
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

		plt.savefig(f"latin_stem_wordclouds/{fp.split('.')[0]}.png", format = "png")

	for w in all_w_freq.keys():
			all_w_freq[w] = float(all_w_freq[w]) / float(total_words)

	wc = WordCloud()

	wc.generate_from_frequencies(all_w_freq)

	plt.figure(figsize = (14, 7))

	plt.imshow(wc, interpolation = "bilinear")

	plt.savefig("latin_stem_wordclouds/overall_wordcloud.png", format = "png")


	

if __name__ == "__main__":
	main()

