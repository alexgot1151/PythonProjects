import random
pass_lenght = int(input("How long password you want: "))
how_much_pass = int(input("How much passwords you want: "))
generated_pass = 0
generated_pass_lenght = 0
password = ""
while (generated_pass < how_much_pass):
    while (generated_pass_lenght < pass_lenght):
        character = random.choice(["a","b","c","d","e","f","g","h","i","j","k",
"l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
"1","2","3","4","5","6","7","8","9","@","&","*","$"
"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q"
"R","S","T","U","V","W","X","Y","Z"])
        generated_pass_lenght += 1
        password = password + character
    generated_pass += 1
    print(password)
    password = ""
    generated_pass_lenght = 0