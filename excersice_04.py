x = []
for i in range(5):
  while True:
    try:
      x.append(int(input('enter an int number: ')))
      break
    except ValueError:
      print('Invalid input')
print(sum(x))