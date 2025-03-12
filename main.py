import sys
from stats import sorted_list


def get_book_text(filepath):
    content = filepath.read()
    return content


def get_num_words():
    file_contents = open(sys.argv[1])
    content = get_book_text(file_contents)
    split_words = content.split()
    length = len(split_words)
    return length


def main():
    total_word_count = get_num_words()
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {total_word_count} total words")
    print("--------- Character Count -------")
    return sorted_list()


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()
