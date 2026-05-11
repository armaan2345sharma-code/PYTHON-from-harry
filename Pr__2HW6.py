
#PROJECT2
#finding a student is pass or fail if he require 33percent in each subject and toal above 40
eng=int(input("percentage in english"))
phy=int(input("percentage in physics"))
chem=int(input("percentage in chemistry"))
math=int(input("percentage in maths"))
ai=int(input("percentage in ai"))
total=int(input("percentsge in total"))
if(phy>33 and chem>33 and math>33 and ai>33 and eng>33 and total>40):
    print("You are pass")
else:
    print("Try better next time")