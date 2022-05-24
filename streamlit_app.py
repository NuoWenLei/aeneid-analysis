import streamlit as st, pandas as pd, json

NUM_BOOKS = 12

new_topic_dict = {}

with open("aeneid_books_topic_modeling/topic_dictionary.json", "r") as topic_json:
	topic_dict = json.load(topic_json)

for k in topic_dict:
	new_topic_dict[f"Topic {k}"] = [i[0] for i in topic_dict[k]]

all_topics = []

for topic in range(NUM_BOOKS):
	with open(f"aeneid_books_topic_modeling/topics_{topic + 1}.json", "r") as topic_json_num:
		topic_data = dict([(i, f"{v:.5f}") for i,v in json.load(topic_json_num)])
	all_topics.append(topic_data)

st.title("Aeneid Text Analysis")

st.text("This analysis uses TF-IDF (Term Frequency Inverse Document Frequency)\nand LDA Topic Modeling techniques to analyze the Aeneid in English and Latin.\n\nVisualizations are generated with Wordcloud.")

analysis_opt = st.radio("Choose Analysis Option: ", [
	"Latin Wordcloud",
	"Latin Stem Wordcloud",
	"English Wordcloud",
	"English Topic Modeling"
])

book_num = st.selectbox("Choose Book: ", [(i + 1) for i in range(NUM_BOOKS)])

if (analysis_opt is not None) and (book_num is not None):
	if analysis_opt == "English Topic Modeling":
		st.text("Topic Index (each column include words similar to a certain topic number)")
		st.dataframe(pd.DataFrame(new_topic_dict))
		st.text("Book-Specific Topics: ")
		st.json(all_topics[book_num - 1])

	if analysis_opt == "English Wordcloud":
		st.text(f"English Wordcloud for Book {book_num}")
		st.image(f"wordclouds/book_{book_num - 1}.png")
		st.text(f"English Wordcloud for Book {book_num} with TF-IDF as frequency")
		st.image(f"tfidf_wordclouds/book_{book_num}.png")

	if analysis_opt == "Latin Wordcloud":
		st.text(f"Latin Wordcloud for Book {book_num}")
		st.image(f"latin_wordclouds/book_{book_num}.png")
		st.text(f"Latin Wordcloud for Book {book_num} with TF-IDF as frequency")
		st.image(f"latin_tfidf_wordclouds/book_{book_num}.png")

	if analysis_opt == "Latin Stem Wordcloud":
		st.text(f"Latin Stem Wordcloud for Book {book_num}")
		st.image(f"latin_stem_wordclouds/book_{book_num}.png")
		st.text(f"Latin Stem Wordcloud for Book {book_num} with TF-IDF as frequency")
		st.image(f"latin_stem_tfidf_wordclouds/book_{book_num}.png")
