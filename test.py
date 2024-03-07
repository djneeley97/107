print("Hello world!")


# let variable = 21;
variable = 21
name = "Daniel"
last_name = "Neeley"
total = 12.99
age = 26
found = True

#if / else statement
#if(var==var2){
# logic
# }
if age < 100:
    print("dont worry youre not that old")
    print("this is only a example")
elif age == 100:
    print("congrats youre a century")
else:
    print("sorry it seems that youre old")

#function
# function say_hello(){}
    
def say_hello():
    print("Goodbye"+ name)

def say_goodbye(name):
    print("Goodbye"+ name)

#call a function
say_hello()
say_goodbye()

#concatenate
print("Hello my name is"+ name +"and i am" + str(age) + "years old")