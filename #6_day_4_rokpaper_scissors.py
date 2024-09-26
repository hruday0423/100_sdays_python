rock = '''
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''   
 _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

scissor = '''  
  _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

list=[rock, paper, scissor]
user_choice = int(input('enter 0 for rock, 1 for paper, 2 for scissor'))

import random
comp=random.randint(0,2)
print('computer chose:')


if user_choice>=3 or user_choice<0:
    print('you chose invalid number')
else:
    print(list[comp])
    print(list[user_choice])
    if user_choice == 0 and comp == 2:
        print('you won')

    elif user_choice==1 and comp==0:
        print('you won')

    elif user_choice == 2 and comp ==1:
        print(' you won')

    elif user_choice == comp:
         print('drawn')
    else:
         print('you loose')



