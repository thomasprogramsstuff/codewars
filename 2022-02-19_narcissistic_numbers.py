#2022-02-19
#A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. 
#In this Kata, we will restrict ourselves to decimal (base 10).
#For example, take 153 (3 digits), which is narcisstic:
#    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
#and 1652 (4 digits), which isn't:
#    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
#The Challenge:
#Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a Narcissistic number in base 10. 
#This may be True and False in your language, e.g. PHP.
#Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function.

def narcissistic(value):
  ###value to value_list
  value_list = [int(a) for a in str(value)]
  print(value_list)
  ###list values ^ len(value_list)
  value_list_calc = [b**len(value_list) for b in value_list]   
  print(value_list_calc)
    ###sum new list values
  print(sum(value_list_calc))
  ###Compare:
  if value==sum(value_list_calc):
    return True
  else:
    return False
    
### Test Cases (Provided)
test.assert_equals(narcissistic(7), True, '7 is narcissistic');
test.assert_equals(narcissistic(371), True, '371 is narcissistic');
test.assert_equals(narcissistic(122), False, '122 is not narcissistic')
test.assert_equals(narcissistic(4887), False, '4887 is not narcissistic')

#### Suggested Best Practice (efficient) Solution:
#def narcissistic(value):
#    return value == sum(int(x) ** len(str(value)) for x in str(value))
