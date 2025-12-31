from stats import count_words, count_num_words, sort_dict
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    num_words = count_words(get_book_text(sys.argv[1]))
    num_letters = count_num_words(get_book_text(sys.argv[1]))
    sorted_dict = sort_dict(num_letters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter in sorted_dict:
        print(f"{letter['char']}: {letter['num']}")
    print("============= END ===============")


main()
