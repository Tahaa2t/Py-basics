import string
from art import logo
def ceaser(txt,sh,ch):
    end_txt = ""
    if ch == "decode":
        sh*=-1
    #end if
    for letter in txt:
        if letter in alphabets:
            found = int(alphabets.index(letter))    #find the element, gives index
            end_txt += alphabets[(found+sh)%26]
        else:
            end_txt += letter
        #end if
    #end for
    print(f"{ch}d: {end_txt}")    

print(logo)

alphabets = list(string.ascii_lowercase)
wanna_exit = False
while not wanna_exit:
    direction = input("Encode or Decode?: ").lower()
    text = input("Enter text: ").lower()
    shift = int(input("Enter shift number: "))
    ceaser(text,shift,direction)
    ch = input("wanna exit? (yes/no): ").lower()
    if ch == 'yes':
        wanna_exit=True
    else:
        wanna_exit=False
