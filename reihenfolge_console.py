# try:
from random import randint;
from time import sleep;
from os import system;
score = 0;
subscore = 0;
temp = 1;

while True:
    array = [];
    subscore = 0;
    for i in range(temp):
        a = str(randint(0,9));
        array.append(a);
        print('Level', temp);
        print(a);
        sleep(2);
        system('cls');

    system('cls');
    print('Level', temp);
    user_input = list(input('Enter the sequence: '));

    for i in user_input:
        if i == array[user_input.index(i)]:
            subscore += 1;
        else:
            subscore = 0;
            break;
    
    if subscore == temp:
        temp += 1;
        score += 1;
        print('You won! The next level is', temp);
        sleep(1);

    else:
        score -= 1;
        print('Your sequence is incorrect. Try again');
        sleep(1);
    
    system('cls');
'''
except Exception as e:
    input(e);
'''