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
def print_hangman(num_of_tries):
    return HANGMAN_PHOTOS[num_of_tries]
print(print_hangman(6))