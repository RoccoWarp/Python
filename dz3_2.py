dic_num = {'one': 'один', 'two': 'два'}


def num_translate_adv(eng_word):
    if eng_word != eng_word.lower():
        return dic_num.get(eng_word.lower().capitalize())
    return dic_num.get(eng_word)


print(num_translate_adv('Rwo'))
