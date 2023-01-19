def count_dict(count_letter):
  string_generator = {}
  count_letter = count_letter.lower()
  count_letter = count_letter.replace(' ','')
  for x in count_letter:
    string_generator[x] = count_letter.count(x)
  return string_generator
    
x = input('Enter a string: ')
print (count_dict(x))
