s = input()

print("ДА") if [all([s[0] == "+", s[1].isdigit(), s[2] == "(", s[3].isdigit(), s[4].isdigit(), s[5].isdigit(), s[6] == ")", s[7].isdigit(), s[8].isdigit(), s[9].isdigit(), s[10] == "-", s[11].isdigit(), s[12].isdigit(), s[13] == "-", s[14].isdigit(), s[15].isdigit()])] == True else print("НЕТ")