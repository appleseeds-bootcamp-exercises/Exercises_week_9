def summer(list):
  x = list[0]
  for ele in list[1:]:
    x += ele
  return x

print(summer([1,4,-5]))
print(summer(['a', 'sdf', 'hytoi5']))
