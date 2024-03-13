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
    print("Hello there")

def say_goodbye(name):
    print("Goodbye"+ name)

#call a function
say_hello()
say_goodbye()

#concatenate
print("Hello my name is"+ name +"and i am" + str(age) + "years old")

#array
#list
color = ["white","red","black","blue"]
print(color)
#add
color.append("pink")
print(color)
#travel the list 
for colors in color:
    print(colors)
# for(i=0;color.len;i++)
    # let temp = color[i]
    #console.log(temp)

    #dictionary
    me={
        "first_name":"Daniel",
        "month":"october",
        "last_name":"Neeley",
        "age":26,
    }
    print(me["first_name"])

    me["age"] = 99
    me["color"]="Blue"
    print(me)