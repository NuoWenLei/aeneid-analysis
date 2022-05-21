import wordcloud, os, json, nltk, ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download('stopwords')
from wordcloud import WordCloud
from nltk.corpus import stopwords
from tqdm import tqdm
import matplotlib.pyplot as plt

def main():
	all_syn_freq = {}
	total_words = 0
	stops = stopwords.words('english')
	personal_stops = ["take", "make", "give", "break", "hold", "see", "run", "bear", "head", "draw", "call", "get"]
	for fp in tqdm(os.listdir("books_synonym_encoded")):
		curr_syn_freq = {}
		with open(f"books_synonym_encoded/{fp}", "r") as json_read:
			syns = json.load(json_read)

		total_words += len(syns)
		for w in syns:
			if w in stops or w in personal_stops:
				continue
			if w not in curr_syn_freq.keys(): 
				curr_syn_freq[w] = 1
			else:
				curr_syn_freq[w] += 1
			
			if w not in all_syn_freq.keys():
				all_syn_freq[w] = 1
			else:
				all_syn_freq[w] += 1

		for w in curr_syn_freq.keys():
			curr_syn_freq[w] = float(curr_syn_freq[w]) / float(len(syns))

		wc = WordCloud()

		wc.generate_from_frequencies(curr_syn_freq)

		plt.figure(figsize = (14, 7))

		plt.imshow(wc, interpolation = "bilinear")

		plt.savefig(f"wordclouds/{fp.split('.')[0]}.png", format = "png")

	for w in all_syn_freq.keys():
			all_syn_freq[w] = float(all_syn_freq[w]) / float(total_words)

	wc = WordCloud()

	wc.generate_from_frequencies(all_syn_freq)

	plt.figure(figsize = (14, 7))

	plt.imshow(wc, interpolation = "bilinear")

	plt.savefig("wordclouds/overall_wordcloud.png", format = "png")


	

if __name__ == "__main__":
	main()

