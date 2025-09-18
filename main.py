from stats import *
import sys


def get_book_text(filepath):
    with open (filepath) as f:
        content = f.read()
    return content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]   
    text = get_book_text(filepath)
    count = word_count(text)
    letters = letter_count(text)
    sorted_letters = sorted_dict(letters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for sorted_letter in sorted_letters:
        if sorted_letter["char"].isalpha():
            print(sorted_letter["char"] + ":", sorted_letter["num"])

main()
