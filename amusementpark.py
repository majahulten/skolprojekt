# Varning programmet öppnar program i din webbrowser med ljud så vänligen ha hörlurar och ljud på
# Vill du åka något mer  ---
# Välkommen åter   ---
# Fixa while n=+1 saken ---
# Implementera ålder, tålamod och längdkrav för de olika attraktionerna --- fixa att det funkar ---S
# Fixa fel URL för house of terror och Bergodalbana
# Rensa upp koden
# Källförteckning
# Kommentarer + övertext
# skicka in person ---

import time
import webbrowser
import random


def intro_main():
    print ('Varmt välkommen till vårt nöjesfält, för att få ut så mycket som möjligt av den här upplevelsen vänligen '
           'aktivera ljudet på datorn. För att komma in och delta på ett säkert sätt behöver vi veta några saker om dig först')
    return

class visitor:
    def __init__(self,age,patience,length):
        self.age=age
        self.patience=patience
        self.length=length
    def __str__(self):
        return "Besökaren är "+str(self.age)+"år, har en "+str(self.patience)+":a i tålmodighet och är "+str(self.length)+"cm."

def create_profile_visitor():
    age=int(input('Hur gammal är du?'))
    patience=int(input('Om du ska ranka ditt tålamod på en skala 1-10 vad skulle du sätta då?'))
    length=int(input('Hur lång är du i cm?'))
    person=visitor(age,patience,length)
    print (person)
    return person
intro_main()
person=create_profile_visitor()



def accident_Chalmers():
    print('Åh nej, åkturen gick inte som planerat du var för naiv.')
    accident = ['Du la lite väl mycket pengar på Gasquen igår',
                'Mailet från ladok rapporterar att du inte klarade kursen',
                'Urkund rapporterar att den hittade en match för ditt arbete online',
                'CSN krånglar igen']
    print (accident[random.randrange(len(accident))])
    time.sleep(5)
    #webbrowser.open('URL')

def attraction_works_Chalmers():
    works = [1,2,3]
    work=(works[random.randrange(len(works))])
    if work == 1:
        print('Du klarade det!!!')
        time.sleep(5)
        webbrowser.open('https://media.giphy.com/media/114IumHhV6sTRK/giphy.gif')
    if work == 2:
        print('Äntligen ingengör')
        time.sleep(5)
        webbrowser.open('http://scarc.library.oregonstate.edu/omeka/files/original/6de07777cfb10eb37b7b48ae5bcff5dc.jpg')
    if work== 3:
        print('Du överlevde första året')
        webbrowser.open('https://media.giphy.com/media/bKBM7H63PIykM/giphy.gif')


def attraction_Chalmers(person):
    if person.age < 18:
        print('Tyvärr har du inte åldern inne, men du är välkommen åter efter gymnasiet')
    if person.age > 18:
        if person.patience < 6:
            print('Tyvärr, en sån här utbildning kräver mycket tålamod så tror inte att den kan vara något för dig')
        else:
            webbrowser.open('https://upload.wikimedia.org/wikipedia/commons/c/cd/Chalmers_huvudentre.jpg')
            attraction=[attraction_works_Chalmers,accident_Chalmers]
            what_happens=(attraction[random.randrange(len(attraction))])
            if what_happens==attraction_works_Chalmers:
                attraction_works_Chalmers()
            if what_happens==accident_Chalmers:
                accident_Chalmers()
    
    

def accident_Houseofterror():
    accident = ['Skådespelarna strejkar så spökhuset måste tyvärr stänga',
                'Vi har problem med mögel och var tvungna att stänga för sannering',
                'Någon i omgången innan blev så rädd att vi nu väntar på ett sjukvårdsteam',
                'Tyvärr, allt fejkblod tog slut så tills nästa leverans är vi stängda']
    print (accident[random.randrange(len(accident))])
    time.sleep(5)
    webbrowser.open('URL')

def attraction_works_Houseofterror():
    works = [1,2,3,4]
    work= (works[random.randrange(len(works))])
    if work == 1:
        webbrowser.open('https://www.youtube.com/watch?v=TFAf_xgNjpE') # Witch laugh
    if work == 2:
        webbrowser.open('https://www.youtube.com/watch?v=WZt7YEuLQ1U') # Creapy lullaby
    if work == 3:
        webbrowser.open('https://www.youtube.com/watch?v=MytAOmbnLpg') # Sound from a mental hospital
    if work == 4:
        webbrowser.open('https://www.youtube.com/watch?v=HpqbJMd6n-U') # scary house sound effects
        
def attraction_Houseofterror(person):
    if person.age < 15:
        print('Tyvärr har du inte åldern inne, men du är välkommen åter efter att du fyllt 15')
    else:
        webbrowser.open('https://s-media-cache-ak0.pinimg.com/originals/a0/cd/3d/a0cd3de541fe2c84e2fe4bf41667e175.jpg')
        attraction=[attraction_works_Houseofterror,accident_Houseofterror]
        what_happens=(attraction[random.randrange(len(attraction))])
        if what_happens==attraction_works_Houseofterror:
            attraction_works_Houseofterror()
        if what_happens==accident_Houseofterror:
            accident_Houseofterror()
    


    
def accident_Bergochdalbana():
    accident = ['Du vaknade precis ur koma, tåget du satt på spårade ur',
                'Vi fick elfel så för alls säkerhet var vi tvungna att stänga',
                'Vi har fastnat så nu väntar vi på att en brandbil ska komma och plocka ner er med stege',
                'Det brinner!!!','Ett av tågen har blivit förhäxat och jagar oss']
    print (accident[random.randrange(len(accident))])
    time.sleep(5)
    webbrowser.open('URL')

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

def attraction_Bergochdalbana(person):
    if person.length < 140:
        print('Tyvärr behöver du växa lite mer innan vi säkert kan låta dig åka med oss')
    else:
        attraction = [attraction_works_Bergochdalbana,accident_Bergochdalbana]
        what_happens=(attraction[random.randrange(len(attraction))])
        if what_happens==attraction_works_Bergochdalbana:
            attraction_works_Bergochdalbana()
        if what_happens==accident_Bergochdalbana:
            accident_Bergochdalbana()

    

def choose_attraction(person):

    print('Vad är du sugen på att åka? För Chalmers skriv 1, Houseofterror skriv 2 eller Bergochdalbana skriv 3')
    choose=int(input())
    if choose == 1:
        attraction_Chalmers(person)
    if choose == 2:
        attraction_Houseofterror(person)
    if choose == 3:
        attraction_Bergochdalbana(person)


def main(person):

    choose_attraction(person)

    print('Vill du åka något mer? (Ja/Nej)')
    stay_or_go=input()
    if stay_or_go == 'Ja':
        main (person)
        return
    if stay_or_go == 'Nej':
        print('Tack för att du valde vårt nöjesfält, välkommen åter')
    else:
        print('Jag förstod inte vad du sa vänligen försök igen')
        main(person)


main(person)
