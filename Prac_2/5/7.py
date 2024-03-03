import re
from collections import defaultdict

def load_dictionary(file_path):
    dictionary = defaultdict(list)
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            match = re.match(r'(\S+)\s+(\d+)', line)
            if match:
                word, frequency = match.groups()
                dictionary[word].append(int(frequency))
    return dictionary

def modified_levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return modified_levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)

    for i, c1 in enumerate(s1):
        current_row = [i + 1]

        for j, c2 in enumerate(s2):
            # Учет замен английских букв на русские
            substitution_cost = 0 if c1 == c2 else 1

            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + substitution_cost

            current_row.append(min(insertions, deletions, substitutions))

            # Учет перестановок пар соседних символов
            if i > 0 and j > 0 and c1 == s2[j - 1] and c2 == s1[i - 1]:
                transposition_cost = previous_row[j - 1]
                current_row[-1] = min(current_row[-1], transposition_cost)

        previous_row = current_row

    return previous_row[-1]

def spell(input_text, dictionary_path='words.txt'):
    dictionary = load_dictionary(dictionary_path)

    def get_candidates(word, max_distance):
        candidates = []
        for dict_word in dictionary.keys():
            distance = modified_levenshtein_distance(word, dict_word)
            if distance <= max_distance:
                candidates.extend([(dict_word, freq) for freq in dictionary[dict_word]])
        return candidates

    corrected_text = []
    for word in input_text.split():
        if word in dictionary:
            corrected_text.append(word)
        else:
            candidates_1 = get_candidates(word, 1)
            if candidates_1:
                most_popular_1 = max(candidates_1, key=lambda x: x[1])[0]
                corrected_text.append(most_popular_1)
            else:
                candidates_2 = get_candidates(word, 2)
                if candidates_2:
                    most_popular_2 = max(candidates_2, key=lambda x: x[1])[0]
                    corrected_text.append(most_popular_2)
                else:
                    corrected_text.append(word)

    return ' '.join(corrected_text)

# Пример использования
input_text = 'помоему я напесал усё правильна'
result = spell(input_text)
print(result)
