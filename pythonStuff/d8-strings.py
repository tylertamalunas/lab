# string work
# prints:
# number of chars in sentence
# number of words
# all uppercase sentence
# uses .split() and .upper()

sent = input("Write a sentence:\n")

# uppercase
print("Here it is in all uppercase:")
print(sent.upper())

# print char number
char_count = 0
for c in sent:
    char_count += 1
print(f"There are {char_count} characters in the sentence.")

# print number of words
split_sent = sent.split()
word_count = 0
for word in split_sent:
    word_count += 1
print(f"There are {word_count} words in the sentence.")



print(len(sent))
