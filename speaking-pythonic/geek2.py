def double_chars(s):
  new_str = ''
  for i in range(len(s)):
    new_str += 2 * s[i]   
  return new_str
  # chars = [2*char for char in str]
  # for 
print(double_chars("abc"))