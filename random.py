import random
# User data intake
want_1 = input('Do you want to play the game, Type, Y for yes and N for no: ')
want = want_1.upper()
#random number generator
user = int(input('Choose number from 1 to 10: '))
comp = random.randint(0,10)
score =  10
#while loop to iterate throught the inputs
while want == 'Y':
  if user > comp:
    score += -1
    print('Your selected number is Higher, Select lower number, Your current score is', score)
    user = int(input('Choose number from 1 to 10: '))
  elif user < comp:
    score += -1
    print('Your selected number is Lower, Select higher number, Your current score is', score)
    user = int(input('Choose number from 1 to 10: '))
  elif user == comp:
    print('Congrats!!! You gussed it, Your score is', score)
    break
  else:
    print('Please select valid input')
