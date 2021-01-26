from PyDictionary import PyDictionary
dictionary=PyDictionary()
def get_meaning(word):
    try:
        meaning = dictionary.meaning(word)
        word_meaning = """"""
        for type_of_word in meaning.keys():
            word_meaning += type_of_word
            word_meaning += ":"
            word_meaning += "\n"
            for idx,meaning_of_word in enumerate(meaning[type_of_word]):
                word_meaning += str(idx+1)
                word_meaning += ". "
                word_meaning += meaning_of_word
                word_meaning += "\n"
            word_meaning += "\n\n"
        return word_meaning
    except:
        return False

