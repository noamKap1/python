def choose_word(file_path, index):
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
    print(index)
    while num<count1:
        cd_splitted_lines_hi.pop(0)
        cd_splitted_lines_hi.append("and")
        if cd_splitted_lines[num] in cd_splitted_lines_hi:
            count += 1
        num +=1
    f.close()
    return cd_splitted_lines[index], (count1-count)
word_number = input("pls enter your word number: ")
print(choose_word("D:\words.txt", int(word_number)))