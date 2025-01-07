
# Read book and and count words
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
    lower_case = []

    for character in characters:
        lower_case.append(character.lower())
    
    for i in range(0, len(lower_case)):
        

    return lower_case 


def main():
    return character_count()

print(main())