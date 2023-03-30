guessed = input("pls enter your letter: ")
num = len(guessed)
alphabet = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
old_letter_guessed = ['b', 'a', 'c']
def check_valid_input(letter_guessed, old_letters):
    if num > 1 or letter_guessed not in alphabet or guessed.lower() in old_letters:
        print("X")
        print("-> ".join(sorted(old_letters)))
        return False
    old_letters.append(guessed.lower())
    return True
print(check_valid_input(guessed, old_letter_guessed))



