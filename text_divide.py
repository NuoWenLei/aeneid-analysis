import re
def main():
	with open("full_aeneid.txt", "r") as aeneid_read:
		txt = aeneid_read.read()
	
	sections = txt.split("""----------------------------------------------------------------------\n\nBOOK """)[1:]
	sections[-1] = sections[-1].split("THE END")[0]

	for i, section in enumerate(sections):
		with open(f"aeneid_books/aeneid_book_{i + 1}.txt", "w") as book_write:
			section_txt = "\n\n".join(section.split("\n\n")[1:-1]).lower()
			section_list = [c for c in section_txt]
			for match in re.finditer("'", section_txt):
				if section_txt[match.start() + 1] != "s":
					section_list[match.start()] = "e"
					if section_txt[match.start() - 4: match.start()] == "thro":
						section_list[match.start()] = "ugh"
		
			book_write.write("".join(section_list))
		

if __name__ == "__main__":
	main()


