def main():

	with open("latin_aeneid_raw.txt", "r") as read_aeneid:
		txt = read_aeneid.read()

	books = txt.replace("PUBLI VERGILI MARONIS\nAENEIDOS\n", "").split("\n\n\n")
	print(books[0][:100])
	print(books[-3][:100])

	for i, book in enumerate(books):
		with open(f"latin_aeneid_books/book_{i + 1}.txt", "w") as write_aeneid:
			write_aeneid.write("\n".join(book.split("\n")[2:]).lower())

if __name__ == "__main__":
	main()