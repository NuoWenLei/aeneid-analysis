import wordcloud, os, json
from wordcloud import WordCloud
from tqdm import tqdm
import matplotlib.pyplot as plt

def main():

	for fp in tqdm(os.listdir("tfidf_features")):

		with open(f"tfidf_features/{fp}", "r") as tfidf_json:
			freq_dict = json.load(tfidf_json)

		wc = WordCloud()

		wc.generate_from_frequencies(freq_dict)

		plt.figure(figsize = (14, 7))

		plt.imshow(wc, interpolation = "bilinear")

		plt.savefig(f"tfidf_wordclouds/{fp.split('.')[0]}.png", format = "png")

if __name__ == "__main__":
	main()

