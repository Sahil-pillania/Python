''' The game() function in a program lets a user play a game and return the score
as an integer. You need to read a file "hiscore" which contains the 
previous hi score. You need to write a program to update the hi score whenever game()
breaks the hi score.'''

def game():
    return 66574          # input value and value will be changed in hiscore.txt file if score is higher

score = game()
with open("hiscore.txt") as f:
    hiscore = int(f.read()) 
    
if hiscore<score: 
    with open("hiscore.txt", "w") as f:
        f.write(str(score))  