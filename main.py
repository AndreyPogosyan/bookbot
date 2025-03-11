from stats import get_num_words, sorted_list
import sys


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    exit(1)


# Main function to call the get_book_text() function
def main():
    total_word_count = get_num_words()
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {total_word_count} total words")
    print("--------- Character Count -------")
    return sorted_list()


main()
