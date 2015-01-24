WORDS_TO_CAPITALIZE = ["Alice", "Ford", "Arthur", "Zaphod", "Trillian", "Hitch", "Hikers", "Guide", "England", "Prefect", "Arthur's", "Ford's", "Tricia", "Tricia's", "Alice's", "Zaphod's", "Dent's", "Dent"]

with_periods = []

for word in WORDS_TO_CAPITALIZE:
	with_periods.append(word + ".")

WORDS_TO_CAPITALIZE = WORDS_TO_CAPITALIZE + with_periods

