def double_chars(s):
  new_str = ''
  for i in range(len(s)):
    new_str += 2 * s[i]   
  return new_str
print(double_chars("abc"))