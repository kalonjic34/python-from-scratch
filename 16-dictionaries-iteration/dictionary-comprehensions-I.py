languages = ["Python", "JavaScript", "Ruby"]


lengths = {language: len(language) for language in languages}
lengths = {language: len(language) for language in languages if "t" in language}
print(lengths)

word = "supercalifragilisticexialidocious"

letter_counts = {letter: word.count(letter) for letter in word if letter > "j"}
print(letter_counts)
