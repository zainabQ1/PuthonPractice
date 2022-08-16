temp_var=100

while(temp_var >=90):
    print("The water boils at {} " .format(temp_var))
    temp_var -=1
    if temp_var == 95:
        break


for number in range (1,11):
    if number == 7:
        print ("we're skipping number 7")
        continue
        print ("the number is {}" .format(number))