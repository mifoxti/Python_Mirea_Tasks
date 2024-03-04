# Input: some long text
# Output: table with parts of sentences like:
# |       1        |          2        |         3         |         4       |
# |       I am     |    a student      |  of the Univercity| in the Moscow   |
# | My brother is  |  a  car driver    |  and love         |  mazeratti      |
# |     You are    | vegetables seller |  in the market    |  near the house |
# to construct sentences from parts of sentences like:
# I am a car driver in the market in the Moscow
# My brother is a student of the Univercity and love mazeratti
# You are a student of the Univercity near the house

def choose_prefixes(sentences):
    global COUNT_OF_LINES
    # Split sentences into words
    words = [sentence.split() for sentence in sentences]
    # Analyze prefixes frequency
    prefixes = {}
    for sentence in words:
        prefix = ''
        for i in range(len(sentence)):
            prefix += sentence[i] + ' '
            if prefix in prefixes:
                prefixes[prefix] += 1
            else:
                prefixes[prefix] = 1

    # If one prefix is a part of another prefix with the same frequency, delete it
    to_delete = []

    for prefix in list(prefixes.keys()):
        for prefix2 in list(prefixes.keys()):
            if prefix != prefix2 and prefix in prefix2 and prefixes[prefix] == \
                    prefixes[prefix2]:
                to_delete.append(prefix)

    # Leave only unique prefixes
    to_delete = list(set(to_delete))
    for prefix in to_delete:
        del prefixes[prefix]

    # Sort prefixes by frequency
    sorted_prefixes = sorted(prefixes.items(), key=lambda x: x[1],
                             reverse=True)

    # Choose COUNT_OF_LINES most frequent prefixes
    prefs = []
    for i in range(COUNT_OF_LINES):
        prefs.append(sorted_prefixes[i][0])

    # From sentences delete sentences which does not contain any of the chosen prefixes
    new_sentences = []
    for i in range(len(sentences)):
        for j in prefs:
            if j in sentences[i]:
                new_sentences.append(sentences[i].replace(j, ''))
                break

    return prefs, new_sentences


FILENAME = "text.txt"
COUNT_OF_LINES = 6
parts = [[] for i in range(COUNT_OF_LINES)]

file = open(FILENAME, 'r', encoding='utf-8')
text = file.read()
file.close()

# Split text into sentences
sentences = text.split('.')

while (sentences != []):
    result = choose_prefixes(sentences)
    for i, j in enumerate(result[0]):
        parts[i].append(j)
    sentences = result[1]

# Find max length of parts
max_len = 0
for i in range(COUNT_OF_LINES):
    if len(max(parts[i], key=len)) > max_len:
        max_len = len(max(parts[i], key=len))

# Write parts into file as a table
file = open("table.txt", 'w', encoding='utf-8')
file.write('|')
for i in range(parts[0].__len__()):
    file.write(' ' + str(i + 1) + ' ' * (max_len - len(str(i + 1))) + ' |')
file.write('\n')
for i in range(COUNT_OF_LINES):
    file.write('|')
    for j in range(len(parts[i])):
        file.write(' ' + parts[i][j] + ' ' * (max_len - len(parts[i][j])) + ' |')
    file.write('\n')
file.close()
