quote = 'some people drink from the fountain of knowledge, others just gargle.'
VOWELS = 'aeiou'

def vowels_positions(quote, vowels):
  return [i for i in range(len(quote)) if quote[i] in vowels]
  
print(vowels_positions(quote, VOWELS))