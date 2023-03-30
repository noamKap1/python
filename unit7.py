need_to_guess_word = "broadly"
list1 = list(need_to_guess_word)
already_letters_guessed = ['a']
num = len(need_to_guess_word)
list = []
while num>0:
    list.append(" _")
    num -=1
def show_hidden_word(secret_word, old_letters_guessed):
    num1 = 0
    i = len(already_letters_guessed)
    while i > -2:
        if num1 == len(need_to_guess_word):
            num1 -= 1
        if list1[num1] in old_letters_guessed:
            list[num1] = list1[num1]
        num1 += 1
        i -= 1
    return list
print(show_hidden_word(need_to_guess_word, already_letters_guessed))


