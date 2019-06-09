import cs50
import sys


def main():

    if len(sys.argv) != 2:
        print("Usage: Provide banned.txt as argument")
        sys.exit

    banned_file = sys.argv[1]

    banned_words = set()

    file = open(banned_file, "r")
    for line in file:
        banned_words.add(line.rstrip('\n'))
    file.close()

    user_word = cs50.get_string("Provide a word please: ")

    stored_text = user_word.split()

    banned_upper = set()
    for word in banned_words:
        banned_upper.add(word.upper())

    for word in stored_text:
        if word in banned_words:
            index = stored_text.index(word)
            ban = stored_text[index]
            new_word = ""
            for i in range (len(ban)):
                new_word =  new_word + "*"
            stored_text[index] = new_word

    for word in stored_text:
        if word in banned_upper:
            index = stored_text.index(word)
            ban = stored_text[index]
            new_word = ""
            for i in range (len(ban)):
                new_word =  new_word + "*"
            stored_text[index] = new_word



    print_word = ""

    for item in stored_text:
        print_word = print_word + " " + item

    print(print_word)


if __name__ == "__main__":
    main()
