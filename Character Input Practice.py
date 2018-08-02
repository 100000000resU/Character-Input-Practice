
run = True

while run:
    name = input("What is your name?")
    age = int(input("How old are you?"))
    years = 100 - age
    if age < 100:
        print("Hello",name,"you will be 100 years old in",years,"years")
        run = False
    else:
        print("You are already over 100",name,"nice try!")
        run = False
        
