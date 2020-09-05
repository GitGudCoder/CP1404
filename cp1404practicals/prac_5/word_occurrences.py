placeholder_input_text = str(input("Please input a string to count occurrence of each word >>> "))
# Instantiate new dictionary for words
word_dict = {}
# Splits user string input into list of each word
words = (placeholder_input_text.split())
# Instantiate new list to store the length of each word
word_length = []

# Cycle through each word in the words list.
for word in words:
    # First appearance of each word counts places the word in the dictionary and counts it once
    if word not in word_dict.keys():
        word_dict[word] = 1
    # Else the counter for the occurrence of the word is incremented
    else:
        word_dict[word] += 1
    # The length of each word is added to the word_length list
    word_length.append(len(word))

# For each item (tuple) in the sorted dictionary, print the word and its occurrence count
for item in sorted(word_dict.items()):
    print(f"{item[0]:<{max(word_length) + 1}}{item[1]}")
