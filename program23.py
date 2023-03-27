words = input("Enter a comma-separated sequence of words: ")

word_list = words.split(',')

word_list.sort()

sorted_words = ','.join(word_list)

print("Sorted words: ", sorted_words)
