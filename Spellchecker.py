from Levenshtein import WagnerFischer


def Spellcheck(word, dictionary_path):
    word = word.lower()
    min_dist = len(word) + 1
    correct = []

    with open(dictionary_path) as f:
        for dict_word in f:
            dict_word = dict_word.strip()

            dist = WagnerFischer(word, dict_word)

            if dist < min_dist:
                correct = [dict_word]
                min_dist = dist

            elif dist == min_dist:
                correct.append(dict_word)

    return correct


def SpellcheckSentence(sentence, dictionary_path):
    output = ""
    for word in sentence.split(" "):
        original_word = word
        word = word.replace(".", "").replace(",", "").replace('"', "").replace("!", "").replace("?", "")
        corrected = Spellcheck(word, dictionary_path)
        if word.lower() == corrected[0]:
            output += original_word
        else:
            output += ("/".join(corrected)).upper()

        output += " "

    return output
