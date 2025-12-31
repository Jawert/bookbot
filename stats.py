def count_words(book_text):
    all_words = book_text.split()
    return len(all_words)


def count_num_words(book_text):
    words = {}

    for word in book_text:
        word = word.lower()
        for letter in word:
            if letter not in words:
                words[letter] = 1
            else:
                words[letter] += 1

    return words


def sort_on(item):
    return item["num"]


def sort_dict(dict):
    # [{"char": "b", "num": 4868}]
    sorted_letters = []

    for letter in dict:
        if letter.isalpha():
            tmp_dict = {}
            tmp_dict["char"] = letter
            tmp_dict["num"] = dict[letter]
            sorted_letters.append(tmp_dict)

    sorted_letters.sort(key=sort_on, reverse=True)

    return sorted_letters
