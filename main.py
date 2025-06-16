from stats import words_in_text
from stats import count_characters_in_text
from stats import get_character_count_list
import sys

def get_book_text(book_filepath):
    with open(book_filepath) as f:
        book_contents = f.read()

    return book_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}")
        print("----------- Word Count ----------")
        book_text = get_book_text(book_path)
        words_in_text(book_text)
        char_dict = count_characters_in_text(book_text)
        count_list = get_character_count_list(char_dict)
        print("--------- Character Count -------")
        for char in count_list:
            if char["char"].isalpha():
                print(f"{char["char"]}: {char["num"]}")
        print("============= END ===============")


main()
