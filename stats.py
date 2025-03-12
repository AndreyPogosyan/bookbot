import sys


def get_book_text(filepath):
    content = filepath.read()
    return content


def character_count():
    book_text = get_book_text(open(sys.argv[1])).lower()
    characters = list(book_text)
    new_dict = {}
    for character in characters:
        if character in new_dict:
            new_dict[character] += 1
        else:
            new_dict[character] = 1
    return new_dict


def sorted_list():
    character_dict = character_count()
    sorted_one = dict(sorted(character_dict.items(), key=lambda item: item[1], reverse=True))
    for key, value in sorted_one.items():
        if key.isalpha():
            print(f"{key}: {value}")
    print("============= END ===============")
