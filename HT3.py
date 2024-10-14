import re

text = """
homEwork: 
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# Split text into sentences
sentences = re.split(r'(?<=[.!?])\s+', text.strip())

# Normalize letter case for each sentence
normalized_sentences = []
for sentence in sentences:
    normalized_sentences.append(sentence.capitalize())

normalized_text = " ".join(normalized_sentences)

# Extract the last words of each sentence
last_words = []
for sentence in sentences:
    last_word = sentence.split()[-1].strip('.!?')
    last_words.append(last_word)

last_words_sentence = " ".join(last_words).capitalize() + "."
new_text = normalized_text + " " + last_words_sentence

# Fix "iZ" with "is"
corrected_text = re.sub(r'\bi[zZ]\b', 'is', new_text)

# Calculate the number of whitespace characters in the text
whitespace_count = 0
for char in corrected_text:
    if char.isspace():
        whitespace_count += 1

print(corrected_text)
print(f"\nNumber of whitespace characters: {whitespace_count}")