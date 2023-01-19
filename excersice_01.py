def unique(elements):
  num = list(dict.fromkeys(elements))
  return num

num = int(input('Enter total numbers: '))
arrayList = []
for i in range (num):
  arrayList.append(input(f'Enter a number {i}: '))
num = unique(arrayList)
print(num)
