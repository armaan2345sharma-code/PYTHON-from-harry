import random
def game(Rand,b):
    if (Rand==1 and b=='h'):
        m="draw"
    elif(Rand==1 and b=='s'):
        m="u won"
    elif(Rand==1 and b=='c'):
        m="lost"
    if (Rand==2 and b=='h'):
        m="u lost"
    elif(Rand==2 and b=='s'):
        m="draw"
    elif(Rand==2 and b=='c'):
        m="u win"         
    if (Rand==3 and b=='h'):
        m="u won"
    elif(Rand==3 and b=='s'):
        m="u lost"
    elif(Rand==3 and b=='c'):
        m="draw"
    return m
Rand=random.randint(1,3)
print("Comuter turn: hand(h),stone(s),cesors(c)")
b=input("players turn: hand(h),stone(s),cesors(c)")
if (Rand==1):
    bh="Hand"
if (Rand==2):
    bh="stone"    
if (Rand==3):
    bh="cesiors"
print("Computer choose",bh)
if (b=='h'):
    bp="Hand"
if (b=='s'):
    bp="Stone"
if (b=='c'):
    bp="Cesiors"
print("U choose",bp)        
k=game(Rand,b)
print(k)

