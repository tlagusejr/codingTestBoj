##알파벳 소문자와 대문자로만 이루어진 길이가 N인 단어가 주어진다.한 줄에 10글자씩 끊어서 출력하는 프로그램을 작성하시오.
string = input()
string10 = ""
for char in string:
    string10 += char
    if len(string10) == 10:
        print(string10)
        string10 = ""
if len(string10) != 10:
    print(string10)