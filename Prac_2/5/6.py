import re
from collections import defaultdict

def load_dictionary(file_path):
    # Загружаем словарь из файла и сохраняем в defaultdict
    dictionary = defaultdict(list)
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Разбиваем строку на слово и частоту встречаемости
            match = re.match(r'(\S+)\s+(\d+)', line)
            if match:
                word, frequency = match.groups()
                dictionary[word].append(int(frequency))
    return dictionary

def levenshtein_distance(s1, s2):
    # Функция для вычисления расстояния Левенштейна между двумя строками
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)

    for i, c1 in enumerate(s1):
        current_row = [i + 1]

        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)

            current_row.append(min(insertions, deletions, substitutions))

        previous_row = current_row

    return previous_row[-1]

def spell(input_text, dictionary_path='words.txt'):
    # Загрузка словаря
    dictionary = load_dictionary(dictionary_path)

    def get_candidates(word, max_distance):
        # Возвращает кандидатов из словаря с расстоянием Левенштейна не более max_distance
        candidates = []
        for dict_word in dictionary.keys():
            distance = levenshtein_distance(word, dict_word)
            if distance <= max_distance:
                candidates.extend([(dict_word, freq) for freq in dictionary[dict_word]])
        return candidates

    corrected_text = []
    for word in input_text.split():
        if word in dictionary:
            # Слово найдено в словаре, оставляем его без изменений
            corrected_text.append(word)
        else:
            candidates_1 = get_candidates(word, 1)
            if candidates_1:
                # Найдены слова с расстоянием Левенштейна равным 1
                most_popular_1 = max(candidates_1, key=lambda x: x[1])[0]
                corrected_text.append(most_popular_1)
            else:
                candidates_2 = get_candidates(word, 2)
                if candidates_2:
                    # Найдены слова с расстоянием Левенштейна равным 2
                    most_popular_2 = max(candidates_2, key=lambda x: x[1])[0]
                    corrected_text.append(most_popular_2)
                else:
                    # Слово не найдено в словаре, оставляем его без изменений
                    corrected_text.append(word)

    return ' '.join(corrected_text)

# Пример использования
input_text = 'помоему я напесал усё правильна'
result = spell(input_text)
print(result)
