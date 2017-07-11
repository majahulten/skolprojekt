# Programmeringsteknik webbkurs KTH inlämningsuppgift 3.
# <Maja Hultén>
# <11/7-2017)
# <Programmet låter dig välja mellan att åka tre olika attraktioner, när du är nöjd och inte vill åka mer avslutas programmet.
# Då programmet spelar upp ljud och filmklipp från youtube som öppnas i din webbläsare så rekommenderas det att ha ljudet på.
# Då en av attraktionerna är ett skräckhus kan viss bakrundsmusik vara lite läskig men ingen större fara. Källor som använts
# för de olika effekterna är youtube, pinterest,Chalmers, gettyimage, giphy och wikimedia>

import time
import webbrowser
import random

def intro_main(): # Välkomsthälsning/introduktion
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

def int_question(question): # håller koll på att svaren på attributfrågorna är ett heltal
    while(True):
        number=input(question)
        if number.isnumeric():
            return int(number)
        print('Vänligen använd enbart heltal när du svarar på frågorna')

def create_profile_visitor():
    age = int_question('Hur gammal är du?')
    patience = int_question('Om du ska ranka ditt tålamod på en skala 1-10 vad skulle du sätta då?')
    length = int_question('Hur lång är du i cm?')
    person = visitor(age, patience, length)
    print(person)
    return person
intro_main()
person=create_profile_visitor()

def accident_Chalmers(): # Om du inte klarar chalmers
    print('Åh nej, åkturen gick inte som planerat du var för naiv.')
    accident = ['Du la lite väl mycket pengar på Gasquen igår',
                'Mailet från ladok rapporterar att du inte klarade kursen',
                'Urkund rapporterar att den hittade en match för ditt arbete online',
                'CSN krånglar igen']
    print (accident[random.randrange(len(accident))])
    time.sleep(5)
    webbrowser.open('http://media.gettyimages.com/photos/this-is-too-hard-picture-id484743293?s=170667a')

def attraction_works_Chalmers(): # Om du klarar chalmers
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
        time.sleep(5)
        webbrowser.open('https://media.giphy.com/media/bKBM7H63PIykM/giphy.gif')

def attraction_Chalmers(person): # Kontrollerar att du har rätt attributer och slumpar fram om du klarar Chalmers eller inte
    if person.age <= 18:
        print('Tyvärr har du inte åldern inne, men du är välkommen åter efter gymnasiet')
    if person.age > 18:
        if person.patience <= 6:
            print('Tyvärr, en sån här utbildning kräver mycket tålamod så tror inte att den kan vara något för dig')
        else:
            webbrowser.open('https://upload.wikimedia.org/wikipedia/commons/c/cd/Chalmers_huvudentre.jpg')
            attraction=[attraction_works_Chalmers,accident_Chalmers]
            what_happens=(attraction[random.randrange(len(attraction))])
            if what_happens==attraction_works_Chalmers:
                attraction_works_Chalmers()
            if what_happens==accident_Chalmers:
                accident_Chalmers()

def accident_Houseofterror(): # Olycka spökhus
    accident = ['Skådespelarna strejkar så spökhuset måste tyvärr stänga',
                'Vi har problem med mögel och var tvungna att stänga för sannering',
                'Någon i omgången innan blev så rädd att vi nu väntar på ett sjukvårdsteam',
                'Tyvärr, allt fejkblod tog slut så tills nästa leverans är vi stängda']
    print (accident[random.randrange(len(accident))])
    time.sleep(5)
    webbrowser.open('http://www.safetysign.com/images/source/large-images/R5335.png')

def attraction_works_Houseofterror(): # När allt funkar för attraktionen spökhus
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
        
def attraction_Houseofterror(person): # Kollar att du har åldern inne samt slumpar om attraktionen funkar
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

def accident_Bergochdalbana(): # Olycka Bergochdalbana
    accident = ['Du vaknade precis ur koma, tåget du satt på spårade ur',
                'Vi fick elfel så för alls säkerhet var vi tvungna att stänga',
                'Vi har fastnat så nu väntar vi på att en brandbil ska komma och plocka ner er med stege',
                'Det brinner!!!','Ett av tågen har blivit förhäxat och jagar oss']
    print (accident[random.randrange(len(accident))])
    time.sleep(5)
    webbrowser.open('http://maryannemistretta.files.wordpress.com/2013/05/seaside-heights-roller-coaster.jpg')

def attraction_works_Bergochdalbana(): # Fungerande bergochdalbana
    works = [1, 2, 3, 4]
    work = (works[random.randrange(len(works))])
    if work == 1:
        webbrowser.open('https://www.youtube.com/watch?v=h_lcZcBcQ0o')#Tyskland
    if work == 2:
        webbrowser.open('https://www.youtube.com/watch?v=1kR34mY1Z0A')# soundeffect scream
    if work == 3:
        webbrowser.open('https://www.youtube.com/watch?v=unocjGOPRUM') # trä china
    if work == 4:
        webbrowser.open('https://www.youtube.com/watch?v=_8JBcmoHDPI') # soundeffects

def attraction_Bergochdalbana(person): # Kollar om du är tillräckligt lång och slumpar om attraktionen fungerar
    if person.length <140:
        print('Tyvärr behöver du växa lite mer innan vi säkert kan låta dig åka med oss')
    else:
        attraction = [attraction_works_Bergochdalbana,accident_Bergochdalbana]
        what_happens=(attraction[random.randrange(len(attraction))])
        if what_happens==attraction_works_Bergochdalbana:
            attraction_works_Bergochdalbana()
        if what_happens==accident_Bergochdalbana:
            accident_Bergochdalbana()

def choose_attraction(person): # Val av attraktion
    print('Vad är du sugen på att åka? För Chalmers skriv 1, Houseofterror skriv 2 eller Bergochdalbana skriv 3')
    choose=int(input())
    if choose == 1:
        attraction_Chalmers(person)
    elif choose == 2:
        attraction_Houseofterror(person)
    elif choose == 3:
        attraction_Bergochdalbana(person)
    else:
        print('Du valde inget nummer mellan 1 och 3. Vänlligen försök igen')
        time.sleep(3)
        choose_attraction(person)
def goodbye(): # Vill du åka mer eller gå hem?
    print('Vill du åka något mer? (Ja/Nej)')
    stay_or_go=input()
    if stay_or_go == 'Ja':
        main (person)
        return
    elif stay_or_go == 'Nej':
        print('Tack för att du valde vårt nöjesfält, välkommen åter')
    else:
        print('Jag förstod inte vad du sa vänligen försök igen')
        goodbye()

def main(person):
    choose_attraction(person)
    goodbye()
main(person)
