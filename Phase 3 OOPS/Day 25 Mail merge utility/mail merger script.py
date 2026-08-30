with open("name.txt", "r") as f:
    names = f.readlines()
    names_list = []
    for name in names:
        names_list.append(name.strip())

with open("starting_letter.txt", "r") as f:
     starting_letters = f.read()

for name in names_list:
        new_letter = starting_letters.replace("[name]", name)
        with open(f"letter_for_{name}.txt", "w") as f:
            f.write(new_letter)

  
    
        

