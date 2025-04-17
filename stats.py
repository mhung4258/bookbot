#accept text as string: returns number of words
def get_word_count(s) -> int:
    word_count = len(s.split())
    return word_count

#seperate the characters from a text
def seperate_char(text) -> dict:
    book_dic = {}
    #go through each text
    for i in text.lower():
        if i in book_dic:
            book_dic[i] += 1
        else: 
            book_dic[i] = 1

    return book_dic

# input: dict -> sorted Dict
def sort_book_dict(book_dict: dict) -> dict:
    sorted_dict = sorted(book_dict.items(), reverse=True, key=lambda x:x[1])

    return dict(sorted_dict)
