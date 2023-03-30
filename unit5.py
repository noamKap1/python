guessed = input("pls enter your letter: ")
num = len(guessed)
alphabet = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
def is_valid_input(letter_guessed):
    if num > 1 or letter_guessed not in alphabet:
        return False
    return True
print(is_valid_input(guessed))
if is_valid_input(guessed):
    print("hi")
