def intro():
    print ("Skriv in fyra meningar")
    return
def create_poem(sentence): #funktion för att få fyra meningar
    n=0
    while n < 4 :
        sentence[n] = input('sentence number '+ str(n+1) + ' : ')
        n+=1
    return sentence
def write_headline(sentence): # Ger dikten sin rubrik bestående av de första fyra orden med stor bokstäver
    headline = sentence[0].split()
    print('\n')
    for item in headline[:4]:
        headline = print("".join(item.upper()), end=" ")
    return headline
def write_poem(sentence): # Skriver ut dikten och lagrar olika delar av dikten i en egen lista
    sentence1 = sentence[0].split()
    sentence2 = sentence[1].split()
    sentence3 = sentence[2].split()
    sentence4 = sentence[3].split()
    for item in sentence1[:4]:
        print("".join(item), end=" ")
    print('')
    if len(sentence1) > 4: # om meningen1 har mindre än eller fyra ord eller är tom ska en tom rad inte skrivas
        for item in sentence1[4:]:
            print("".join(item), end=" ")
        print('')
    for item in sentence1[:4]: #SKRIV IHOP ALLT DET HÄR TILL EN MENING
        print("".join(item), end=" ")
    print('')
    if len(sentence2) > 0:
        print(" ".join(sentence2))
    if len(sentence3) > 0:
        print(" ".join(sentence3))
    if len(sentence4) > 0:
        print(" ".join(sentence4))
    for item in sentence1[:4]:
        print("".join(item), end=" ")
    print('')
    return sentence1, sentence2, sentence3, sentence4

if __name__ == "__main__":
    def huvudprogram():  # Huvudprogrammet som kör allt
        sentence = 4 * [None]
        intro()
        create_poem(sentence)
        write_headline(sentence)
        print('\n')
        write_poem(sentence)

    huvudprogram()

