print("""    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/""")
max_tries=6
print(max_tries)
num_of_trys=1
alphabet = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'


def choose_word(file_path, index):
    """
        This function is choosing a word from a file that the user decided.
        :param file_path: the path for the file
        :type file_path: str
        :param index: the index of the word that the user chose
        :type index: int
        :return: the function return a tuple from the file for the file and the index that the function was given
    """
    f = open(file_path, "r")
    cd_data = f.read()
    cd_splitted_lines = cd_data.split(" ")
    cd_splitted_lines_hi = cd_data.split(" ")
    num = 0
    count = 0
    count1 = 0
    for word in cd_splitted_lines:
        count1 += 1
    if index<15:
        index -= 1
    while index>=(count1+1):
        index -=(count1 + 1)
    while num<count1:
        cd_splitted_lines_hi.pop(0)
        cd_splitted_lines_hi.append("and")
        if cd_splitted_lines[num] in cd_splitted_lines_hi:
            count += 1
        num +=1
    f.close()
    return cd_splitted_lines[index]
word_number = input("pls enter your word number: ")
text_file = input("pls write your text file: ")
secret_word = choose_word(text_file, int(word_number))
already_letters_guessed = []
num_of_fails=0
list1 = list(secret_word)



zero = """x-------x
|       |
|       
|      
|      
|"""
first = """x-------x
|       |
|       0
|      
|      
|"""
second = """x-------x
|       |
|       0
|      /
|      
|"""
third = """x-------x
|       |
|       0
|      /|
|      
|"""
forth = """x-------x
|       |
|       0
|      /|\\
|      
|"""
fifth = """x-------x
|       |
|       0
|      /|\\
|      / 
|"""
sixth = """x-------x
|       |
|       0
|      /|\\
|      / \\
|"""
HANGMAN_PHOTOS = {0: zero, 1: first, 2: second, 3: third, 4: forth, 5: fifth, 6: sixth}

print(HANGMAN_PHOTOS[0])
num1 = len(secret_word)
print(" _" * num1)






while num_of_fails<6:

    def print_hangman(num_of_failed_tries):
        """

           :param num_of_failed_tries: the number of the failed tries the user used
           :type: int
           :return:the current position of the hangman(due to number of failed tries)
           :rtype: str
           """
        return HANGMAN_PHOTOS[num_of_failed_tries]

    if num_of_fails > 0:
        print(print_hangman(num_of_fails))

    guessed = input("pls enter your letter: ")
    num = len(guessed)

    def check_valid_input(letter_guessed, old_letters):
        """
           this function is checking if the letter that the user chose is valid and if so, it will add the letter to a list
           :param letter_guessed: the letter that the user chose
           :type: str
           :param old_letter: all the valid letters that the user chose
           :type: list
           :return: if the letter is valid
           :rtype: bool
           """
        if num > 1 or letter_guessed not in alphabet or guessed.lower() in old_letters:
            return False
        return True
    def try_update_letter_guessed(letter_guessed, old_letters_guessed):
        """
                   this function is checking if the letter that the user chose is in the list of old letters and if not it will print "x"  if yes it will return true
                   :param letter_guessed: the letter that the user chose
                   :type: str
                   :param old_letters_guessed: all the valid letters that the user chose
                   :type: list
                   :return: if the letter is valid
                   :rtype: bool
                   """
        if check_valid_input(letter_guessed, old_letters_guessed):
            return True
        else:
            print("X")
            return False

    if try_update_letter_guessed(guessed, already_letters_guessed):
        already_letters_guessed.append(guessed.lower())
    else:
        num_of_fails +=1
    print(already_letters_guessed)
    if guessed not in alphabet:
        num_of_fails -=1



    num = len(secret_word)
    list = []
    list2 = list
    while num > 0:
        list.append(" _")
        num -= 1
    def show_hidden_word(secret_word1, old_letters_guessed):
        """
           this function is checking if the letters appear in the word that the user chose
           :param secret_word1: the word the user chose
           :type: secret_word1: str
           :param old_letter_guessed: all the valid letters that the user chose
           :type: old_letter_guessed: list
           :return: this function returns a string with the letters that the user guessed and underscores instead pf the letters he didnt guessed
           :rtype: str
           :return: if the letter is in the word
           :rtype: bool
           :return: the word with space between the characters
           :rtype: str
           """
        num2 = 0
        i = len(already_letters_guessed)
        while i > -3:
            if num2 == len(secret_word):
                num2 -= 1
            if list1[num2] in old_letters_guessed:
                list[num2] = list1[num2]
            num2 += 1
            i -= 1
        return list
    print(show_hidden_word(secret_word, already_letters_guessed))
    if guessed not in list:
        num_of_fails += 1

    def check_win(guessed_letters, hidden_word):
        """
                           this function is checking if the letters that were guessed all of them fill the secret word if yes it will return true if not it will return false
                           :param guessed_letters: the letter that the user guessed
                           :type: list
                           :param hidden_word: the secret word from the beginning
                           :type: list
                           :return: if the letters fill the secret word
                           :rtype: bool
                           """
        if guessed_letters == hidden_word:
            return True
        else:
            return False
    if check_win(list, list1):
        print("win")
        break

    num_of_trys +=1
if num_of_fails>=6:
    print(HANGMAN_PHOTOS[6])
    print("lose")
    print("the word was: " + secret_word)


