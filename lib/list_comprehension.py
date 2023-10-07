#!/usr/bin/env python3

def return_evens(num_list):
    even_nums = [num for num in num_list if num % 2 == 0]

    for num in even_nums:
        print(num, end='\n')

    return even_nums


print(return_evens([1, 2, 3, 4, 5, 6, 7]))


def make_exclamation(sentence_list):
    exclaimed_sentence = [word + "!" for word in sentence_list]

    # for word in exclaimed_sentence:
    #     print(word)

    return (exclaimed_sentence)


sentence_list = ["I like computers",
                 "I require coffee", "Live long and prosper"]
make_exclamation(sentence_list)
