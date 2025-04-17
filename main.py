
from stats import get_word_count
from stats import seperate_char
from stats import sort_book_dict
import sys


def get_book_text(path):
    file_contents = ""
    with open(f"{path}") as f:
        file_contents = f.read()
    return file_contents


def main():

        # System Aruguments
    arg = sys.argv
    book_path = ""

    if len(arg) >= 2:
        book_path = arg[1]
    else: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        

    book_dict = seperate_char(get_book_text(book_path))
    sorted_dict = sort_book_dict(book_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(get_book_text(book_path))} total words")
    print("--------- Character Count -------")

    for key, value in sorted_dict.items():
        if key.isalpha():
            print(f"{key}: {value}")
    print("============= END ===============")



if __name__ == "__main__":
    main()