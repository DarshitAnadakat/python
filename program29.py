input_str = input("Enter a string: ")

words = input_str.split()

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

sorted_keys = sorted(freq.keys())

for key in sorted_keys:
    print(key, ":", freq[key])
