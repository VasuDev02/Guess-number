#guess the number by computer:
import random
def guess_number(x):
    low=1
    high=x
    feedback=' '
    while feedback!='C':
        random_num=random.randint(low,high)
        print(random_num)
        print("Is the %d correct(C), or it is Too High(H), or Too Low(L)??"%random_num)
        feedback = input()
        if feedback=='H':
            high=random_num-1
        elif feedback=='L':
            low=random_num+1
    print("Yay....computer guessed my number(%d) correctly"%random_num)




#guess the number by user:
import random
def guess_number(x):
    random_num=random.randint(1,x)
    guess=0
    count=0
    print("Guess the number between 1 and %d"%x)
    while random_num!=guess:
        count=count+1
        guess=int(input())
        if random_num>guess:
            print("Too Low...Guess again")
        elif random_num<guess:
            print("Too High...Guess again")
    print("Yeah...you have Guessed correctly %d"%random_num)
    print("you have taken %d chances to guess correctly"%count)
guess_number(10)
