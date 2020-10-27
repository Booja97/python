number = 7
attempt =3
while attempt>0:
    attempt-=1
    print("Enter a number between 1 to 10:")
    guess= int(input())
    if guess> number:
        print("your guess is greater than the number")
    elif guess< number:
        print("your guess is less")
    elif guess==number:
        print("your guess is correct")
        quit()
