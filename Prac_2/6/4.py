def train_language_model(text, prefix_length):
    model = {}
    for i in range(len(text) - prefix_length):
        prefix = text[i:i+prefix_length]
        next_char = text[i+prefix_length]
        if prefix not in model:
            model[prefix] = {}
        if next_char not in model[prefix]:
            model[prefix][next_char] = 0
        model[prefix][next_char] += 1
    return model

text = "Na dvore trava, na trave drova"
prefix_length = 2
language_model = train_language_model(text, prefix_length)

for prefix, next_chars in language_model.items():
    print(f"{prefix}: {next_chars}")
