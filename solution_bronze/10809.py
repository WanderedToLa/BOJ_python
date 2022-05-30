import string

s = input()
lower = [i for i in string.ascii_lowercase]

for i in lower:
  print(s.find(i), end=" ") #해당 문자가 존재하면 인덱스 반환 / 없으면 -1