
def read_book():
    word_cout = 0
    read_book = open("books/frankenstein.txt", "r")
    books = read_book.read().split()
    for book in books:
        if book:
            word_cout += 1
    return word_cout

def character_count():
    characters = list(open("books/frankenstein.txt", "r").read())
    lower_case = [character.lower() for character in characters if character.isalpha()]
    count = {}


    for character in lower_case:
        if character in count:
            count[character] += 1
        else:
            count[character] = 1

    return count
    # for key, character in count.items():
    #     print(f"The '{key}' character was found '{character}' times")
        

    # return count
    # for character in characters:
    #     if character.isalpha():
    #       lower_case.append(character.lower())

def main():
    # read_book()
    character_count()

print(main())