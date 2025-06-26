def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def get_word_count_from_text(path_to_file):
    num_words = len(get_book_text(path_to_file).split())
    return f"Found {num_words} total words"

def get_each_character_count(path_to_file):
    character_count = {}
    lowercase_text = get_book_text(path_to_file).lower()
    lowercase_strings = lowercase_text.split()
    for string in lowercase_strings:
        for char in string:
            if char not in set(character_count):
                character_count[char] = 1
            else:
                character_count[char] += 1
    return character_count

def sort_on(items):
    return items["num"]

def sorted_list(character_count):
    final_sorted_dict = []
    for char in character_count:
        num = character_count[char]
        final_sorted_dict.append({"char": char, "num": num})
    final_sorted_dict.sort(reverse=True, key=sort_on)
    return final_sorted_dict