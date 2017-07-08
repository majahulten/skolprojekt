
######## example 1

x = 1

if x == 1:
    print('1')

if x == 2:
    print('2')

else:
    print("not a number")


'''
if x = 1
    do something
___
if x = 2
    do something
else
    do something if x = 2 is false
'''

# else if version

if x == 1:
    print('1')

elif x == 2:
    print('2')

else:
    print("not a number")


'''
if x = 1
    do something
or x = 2
    do something
if neither
    do something if both is false
'''

######## example 2

def attraction_works_Bergochdalbana():
    works = [1,2,3,4]
    work= (works[random.randrange(len(works))])
    if work == 1:
        webbrowser.open('https://www.youtube.com/watch?v=h_lcZcBcQ0o')#Tyskland
    if work == 2:
        webbrowser.open('https://www.youtube.com/watch?v=1kR34mY1Z0A')# soundeffect scream
    if work == 3:
        webbrowser.open('https://www.youtube.com/watch?v=unocjGOPRUM') # trä china
    if work == 4:
        webbrowser.open('https://www.youtube.com/watch?v=_8JBcmoHDPI') # soundeffects

# kan skrivas om till
def attraction_works_Bergochdalbana1():
    # split url from url params
    url = 'https://www.youtube.com/watch?v='
    works = {
        1: 'h_lcZcBcQ0o',
        2: '1kR34mY1Z0A',
        3: 'unocjGOPRUM',
        4: '8JBcmoHDPI'
    }
    # random 1-4 in dict
    work= (works[random.randrange(len(works))])

    # baseURL + works[1-4] (gives a string from works)
    full_url = url+works[work]
    # open url in browser
    webbrowser.open(full_url)

# du kan köra functioner på samma sätt
dict_functions = {
    1: attraction_works_Bergochdalbana,
    2: attraction_works_Bergochdalbana1,
}
# kör attraction_works_Bergochdalbana()
dict_functions[1]()


########## example 3

"Besökaren är "+str(self.age)+"år, har en "+str(self.patience)+":a i tålmodighet och är "+str(self.length)+"cm."

# mycket lättare att jobba med
"Besökaren är {0} år, har en {1}:a i tålmodighet och är {2}cm.".format(str(self.age), str(self.patience), str(self.length))


########## example 4

while True:
    try:
        age = int(input("Please enter your age: "))

    # ValueError = age is not a integer
    except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
    else:
        #age was successfully parsed!
        #we're ready to exit the loop.
        break
# if we got here the input is a valid integer
if age >= 18:
    print("You are able to vote in the United States!")
else:
    print("You are not able to vote in the United States.")


# short version
while True:
    try:
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break