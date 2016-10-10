#! Python3

# roman7.py program

import re


roman_numeral_map = (('M', 1000),
                     ('CM', 900),
                     ('D', 500),
                     ('CD', 400),
                     ('C', 100),
                     ('XC', 90),
                     ('L', 50),
                     ('XL',40),
                     ('X', 10),
                     ('IX', 9),
                     ('V', 5),
                     ('IV', 4),
                     ('I', 1))


def to_roman(n) :
  """Convert Integer to Roman Numeral"""

  if n > 3999 :
    raise OutOfRangeError('number out of range(must be less than 4000)')
  if n <= 0 :
    raise OutOfRangeError('zero/negative number(s) is(are) not defined in roman numeral')
  if not isinstance(n, int) :
    raise NotAnIntegerError('Non integer values cannot be handled')

  result = ''
  for numeral, integer in roman_numeral_map :
    while n >= integer :
      result += numeral
      n -= integer
      print('subtracting {0} from input, adding {1} to output'.format(integer, numeral))
  return result


roman_numeral_pattern = re.compile('''
  ^                                             # beginning of string
  M{0,3}                                        # thousands - 0 to 3 Ms
  (CM|CD|D?C{0,3})                              # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs), or 500-800 (D, followed by 0 to 3 Cs)
  (XC|XL|L?X{0,3})                              # tens -      90 (XC), 40 (XL), 0-30 (0 to 3 Xs),    or 50-80 (L, followed by 0 to 3 Xs)
  (IX|IV|V?I{0,3})                              # ones -       9 (IX), 4 (IV), 0-3 (0 to 3 Is),       or 5-8 (V, followed by 0 to 3 Is)
  $                                             # end of string
  ''', re.VERBOSE)    ##end of compilation


def from_roman(s) :
  '''Convert Roman numeral to integer'''
  if not s :
    raise InvalidRomanNumeralError('Input cannot be blank')
  if not roman_numeral_pattern.search(s) :
    raise InvalidRomanNumeralError('Invalid Roman numeral: {0}'.format(s))

  result = 0
  index =  0
  for numeral, integer in roman_numeral_map :
    while s[index:index+len(numeral)] == numeral :
      result += integer
      index += len(numeral)
  return result 


class OutOfRangeError(ValueError) :  pass

class NotAnIntegerError(ValueError) : pass
  
class InvalidRomanNumeralError(ValueError) : pass 
