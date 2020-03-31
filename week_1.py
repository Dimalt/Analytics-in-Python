def reverse(sentence, reverse_word):
    return sentence[:sentence.find(reverse_word)]\
     + reverse_word[::-1]\
     + sentence[sentence.find(reverse_word) + len(reverse_word):]


print(reverse("Python improves my mood very much", "mood"))
