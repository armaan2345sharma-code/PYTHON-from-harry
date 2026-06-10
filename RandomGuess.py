import random
RandNum=random.randint(1,100)
guess=0
numberGuess=0
print(RandNum)
print("Welcome to the number guessing game!")
while guess!=RandNum:
    guess=int(input("guess the number between 1 and 100: "))
    numberGuess+=1
    if guess<RandNum:
        print("too low")
    elif guess>RandNum:
        print("too high")
    else:
        print("correct!")
with open("Highscore.txt","r") as f:
    highscore=int(f.read())
if numberGuess<highscore:
    print("Congratulations you beat the Highscore!")
    with open("Highscore.txt","w") as f:
        f.write(str(numberGuess))
    
print(f"you guessed the number in {numberGuess} attempts!")