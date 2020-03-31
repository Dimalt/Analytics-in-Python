def word_distribution(input_text):
    dictionary = {}

    for string in input_text.split():
        if (string[0].isalpha() and string[-1].isalpha()):
            word = string.lower()
        elif(string[0].isalpha() and (not string[-1].isalpha())):
            word = string[:-1].lower()
        else:
            word = string[1:].lower()

        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    return dictionary


input_text = "That's when I saw Jane (John's sister)! and i said to jane hello"
print(word_distribution(input_text))

input_text = "That's when I saw Jane (John's sister)! and i said to jane hello"
print(word_distribution(input_text))
