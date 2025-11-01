# It’s not perfect, but it works. And that’s enough for tonight. 🍻
import random
print("Welcome to Caterpillar Password Generator !")

letters =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#0-25
numbers =['0','1','2','3','4','5','6','7','8','9']
#0-9
symbols =['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 
 ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
#0-31

storage = [letters,numbers,symbols]
# print(storage)
num_letters = int(input("How many letters would you like in your password ?\n"))
num_numbers =int(input("How many numbers would you like in your password ?\n"))
num_symbols =int(input("How many symbols would you like in your password ?\n"))
length_of_password = num_letters + num_numbers + num_symbols




password = ""
n_l = n_n = n_s = 0

for i in range(length_of_password):#{

    position_x = random.randint(0,2)
    if n_l == num_letters:
            position_x = random.randint(1,2)
    elif n_n == num_numbers:
            position_x = random.choice([0,2])
    elif n_s == num_symbols:
            position_x = random.randint(0,1)                


    if position_x == 0 and n_l < num_letters:
        position_y = random.randint(0,25)
        n_l += 1
        password += storage[position_x][position_y]

    elif position_x == 1 and n_n < num_numbers:
        position_y = random.randint(0,9)
        n_n += 1
        password += storage[position_x][position_y]

    elif position_x == 2 and n_s < num_symbols:
        position_y = random.randint(0,31)
        n_s += 1
        password += storage[position_x][position_y]
            
 # password += storage[position_x][position_y]
#}
print(password)


# It’s not perfect, but it works. And that’s enough for tonight. 🍻