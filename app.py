import json
from flask import Flask, redirect, request, url_for, render_template, session, flash

app = Flask(__name__)

app.secret_key = b'\x10\xbf\xdb\xe7\x01\xe2B\xed\xf6\xf0\xd8l'

NUM_BOOKS = 12

analysis_options = [
	["latin_wordcloud", "Latin Wordcloud"],
	["latin_stem_wordcloud", "Latin Stem Wordcloud"],
	["english_wordcloud", "English Wordcloud"],
	["english_topic_modeling", "English Topic Modeling"],
]

analysis_option_dict = {
	"latin_wordcloud": [["latin_wordclouds", "latin_tfidf_wordclouds"], "Latin Wordcloud"],
	"latin_stem_wordcloud": [["latin_stem_wordclouds", "latin_stem_tfidf_wordclouds"], "Latin Stem Wordcloud"],
	"english_wordcloud": [["wordclouds", "tfidf_wordclouds"], "English Wordcloud"],
	"english_topic_modeling": [["aeneid_books_topic_modeling"], "English Topic Modeling"],
}

@app.route("/", methods = ["GET"])
def index():
	return render_template("index.html",
	book_numbers = [i + 1 for i in range(NUM_BOOKS)],
	analysis_options = analysis_options
	)

if __name__ == "__main__":
	app.run()