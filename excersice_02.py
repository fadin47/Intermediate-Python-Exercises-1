def get_combined_dict(dict1, dict2):
  dict3 = {}
  for keys in dict2:
    if keys in dict1:
      dict3[keys] = dict2[keys] + dict1[keys]
  return dict3

x = int(input('Enter a number value: '))
dict1 = {}
for i in range(x):
    keys = input('Enter a string: ') 
    values = int(input('Enter an int number: '))
    dict1[keys] = values
print(dict1)

y = int(input('Enter a number value: '))
dict2 = {}
for i in range(y):
    keys = input('Enter a string: ')  
    values = int(input('Enter an int number: '))
    dict2[keys] = values
print(dict2)

combined_dict = get_combined_dict(dict1, dict2)
print(combined_dict)
