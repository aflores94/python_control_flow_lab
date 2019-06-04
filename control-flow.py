
# exercise-01 Vowel or Consonant

x = input('Please enter a letter from the alphabet (a-z or A-Z): ')

if x in 'aeiou':
    print(f'The letter {x} is a vowel')
else:
    print(f'The letter {x} is not a vowel')

# exercise-02 Length of Phrase

x = None 

while x != 'quit':
    x = input('Please enter a word or phrase: ')
    print(f'What you entered is {len(x)} characters long')

# exercise-03 Calculate Dog Years

human_years = int(input("Input a dog's age in human years: "))
if human_years < 3:
  dog_years = human_years * 10
else:
  dog_years = 20 + (human_years - 2) * 7
print(f"The dog's age in dog years is {dog_years}")


# exercise-04 What kind of Triangle?

a = input('Enter the length of side a: ')
b = input('Enter the length of side b: ')
c = input('Enter the length of side c: ')

if a == b and b == c:
  print(f'A triangle with sides of {a}, {b} & {c} is an equalateral triangle')
elif a != b and a != c and b != c:
  print(f'A triangle with sides of {a}, {b} & {c} is a scalene triangle')
else:
  print(f'A triangle with sides of {a}, {b} & {c} is an isosceles triangle')


# exercise-05 Fibonacci sequence for first 50 terms

term = 0
a = 0
b = 1
while term < 50:
  if term < 2:
    print(f'term: {term} / number: {term}')
  else:
    num = a + b
    print(f'term: {term} / number: {num}')
    a = b
    b = num
  term += 1



# exercise-06 What's the  Season?

month = input('Enter the month of the season (Jan - Dec): ')
day = int(input('Enter the day of the month: '))

if month in ('Jan', 'Feb', 'Mar'):
  season = 'Winter'
elif month in ('Apr', 'May', 'Jun'):
  season = 'Spring'
elif month in ('Jul', 'Aug', 'Sep'):
  season = 'Summer'
else:
  season = 'Fall'

if month == 'Mar' and day > 19:
  season = 'Spring'
elif month == 'Jun' and day > 20:
  season = 'Summer'
elif month == 'Sep' and day > 21:
  season = 'Fall'
elif month == 'Dec' and day > 20:
  season = 'Winter'
  
print(f'{month} {day} is in {season}')