def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    char_counts = {}

    for char in text:
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1

    return char_counts

def sort_characters(char_counts):
    sorted_list = []

    for char, count in char_counts.items():
        sorted_list.append({"char": char, "num": count})

    sorted_list.sort(reverse=True, key=lambda d: d["num"])
    return sorted_list
