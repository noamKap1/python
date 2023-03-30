letter = input("pls enter your letter: ")
num = len(letter)
alphabet = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
if letter not in alphabet and num>1:
    print("E3")
elif num>1:
    print("E1")
elif letter not in alphabet:
    print("E2")
else:
    print(letter)