for b in range(1,21):
    with open (f"table of {b}.txt",'w') as f:
        for i in range (1,11):
            f.write(f"{b} X {i} = {b*i}\n")



            