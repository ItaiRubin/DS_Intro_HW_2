def reverse(sentence, reverse_word):
    try:
        if reverse_word not in sentence:
            return "The word was not found"
        else:
            wordlen = len(reverse_word)
            wordindex = sentence.index(reverse_word)
            move1 = sentence[:wordindex]
            move2 = sentence[wordindex+wordlen:]
            reverse1 = reverse_word[::-1]
            end = move1 + reverse1 + move2
            return end
    except:
        return "invalid input"



