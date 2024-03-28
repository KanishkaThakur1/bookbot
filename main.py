def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        count_letters = letter_count(file_contents)
        print(" Begin Report")
        print()
        print(f"{word_count} words found in the text")
        print()
        for dict in count_letters:
            dict_letter = dict["letter"]
            dict_count = dict["count"]
            print(f"The {dict_letter} character was found {dict_count} times")
        print()
        print("End Report")


def sort_on(dict):
    return dict["count"]

def letter_count(text):
    lower_text = text.lower()
    letter_dict = {}
    for letter in lower_text:
        if letter.isalpha():
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    letter_list = []
    for letter, count in letter_dict.items():
        new_dict = {"letter": letter, "count": count}
        letter_list.append(new_dict)
    letter_list.sort(reverse=True, key = sort_on)
    return letter_list


def count_words(words):
    split_words = words.split()
    count = len(split_words)
    return count

main()