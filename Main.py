import random
import pyperclip #pip install pyperclip
def Main():
    name = input("Enter your name ") # This take name 
    app_website_name = input("Enter your app and website name for your generator password ") # This is take app and website 
    ran = random.randint(0,999) # This is Generator random number
    Sun = int(ran) - int(random.randint(1,219)) # this - number to random 1 to 219
    con = '("'+ name + "Work" + "." + app_website_name + str(Sun) + '")' # this is add all things 
    print(con)
    pyperclip.copy(con) # This for copy password
    spam = pyperclip.paste()
    exit() # This exit the proprogramming
Main() 