def words_in_text(text):
    word_list = text.split()
    num_words = len(word_list)
    print(f"Found {num_words} total words")


def count_characters_in_text(text):
    character_dict = {}
    for char in text:
        if char.lower() in character_dict:
            character_dict[char.lower()] += 1
        else:
            character_dict[char.lower()] = 1

    return character_dict


def sort_on(dict):
    return int(dict["num"])

def get_character_count_list(char_dict):
    sorted_dict_list = []
    for char in char_dict:
        new_dict = {"char": f"{char}", "num": f"{char_dict[char]}"}
        sorted_dict_list.append(new_dict)
    
    sorted_dict_list.sort(reverse=True, key=sort_on)

    return sorted_dict_list
