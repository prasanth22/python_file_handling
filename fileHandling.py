from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

def char_count(fname):
    with open(fname) as f:
        c = Counter()
        for x in f:
            c += Counter(x.strip())
            return c

fname = input("Enter file name: ")  # D:\examplefile.txt
num_words = 0
num_chars = 0
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
        num_chars += len(line)

print('Number of characters in text file :', num_chars)
print('Number of words in text file:',num_words)
print("Number of times each word repeats in the file :",word_count(fname))
print("Number of times each character repeats in the file :",char_count(fname))
