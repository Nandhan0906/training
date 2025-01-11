#Write a Python Program to calculate the frequency of each word in a given text.Print the words and their corresponding counts.

text = "This is a sample text. This text is used to demonstrate the word frequency calculation."

words = text.lower().split()

word_frequency = {}

for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")