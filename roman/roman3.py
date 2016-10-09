#! Python3

# roman3.py program




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
  result = ''
  for numeral, integer in roman_numeral_map :
    while n >= integer :
      result += numeral
      n -= integer
      print('subtracting {0} from input, adding {1} to output'.format(integer, numeral))
  return result



class OutOfRangeError(ValueError) :  
  pass
   
