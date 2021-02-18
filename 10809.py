# 2021. 02. 16. 금
# 10809번
# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 
# 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 
# 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

word = input()

alphabet = list(range(97,123))
# 아스키코드 a = 97, z = 122
# 알파벳리스트 생성

for i in alphabet:
    print(word.find(chr(i)))
# ex) i = 97일때 chr(i)를 통해 아스키코드 -> 문자로 바꾼 후,
# find함수를 통해 word에서 chr(i)가 처음 나오는 위치를 찾아서 출력.    