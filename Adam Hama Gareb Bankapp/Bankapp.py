#Här är min Bank Applikation som jag gjorde med hjälp av tkinter och GUI!

#Här är några importer som kommer behövas till de olika kodfunktionerna senare
from atexit import register
from tkinter import *
import os
from PIL import ImageTk, Image

#Detta är huvudskärmen, med en titel ovanför appen. Variabeln "master" kommer vara huvudvariabeln 
#till alla funktioner i koden med namnet 'master'
master = Tk()
master.title('Banking App')

#Här nedan är det kod till funktioner som behöver defineras, som kommer behövas senare till sådant 
#som  buttons och labels som vi kommer att stöta på nedan i koden

#Exempelvis här defineras variabeln finish_reg. Den gjord för att något skall hända efter att man
#har tryckt på register knappen i registreringsfliken i den här appen. Vi stöter på den senare i
#koden
def finish_reg():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    all_accounts = os.listdir()
    
    #Här så dubbelcheckar koden med hjälp av en if sats ifall användaren har skrivit in något i alla
    #kriterier som man ska skriva in för att registrera. Har hen inte gjort det så skickas ett
    #meddelande där det står "Please fill in the requirements above!"
    if name == "" or age == "" or gender == "" or password == "":
        notif.config(fg="red", text="Please fill in the requirements above!")
        return
    

    #Här dubbelcheckar koden om det redan finns ett konto med samma namn registrerat. Finns det det
    #så kommer koden skicka ut meddelandet "Account already exists!" och kommer ej låta användaren
    #skapa kontot med det namnet. Finns inte det namnet registrerat så skapar den en fil med namnet
    #som användaren registrerade med, tillsammans med ett w i slutet
    #Här i koden där det börjar med "new_file" är det kod som lägger in all data den fick från
    #kriterierna i registrerings steget förut och sparar det i den nya filen (kontot) som skapas
    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg="red", text="Account already exists!")
        else:
            new_file = open(name,"w")
            new_file.write(name+'\n')
            new_file.write(password+'\n')
            new_file.write(age+'\n')
            new_file.write(gender+'\n')
            new_file.close()
            notif.config(fg="green", text="Account created!")

def register():
    #Variabler som defineras här men används i koden nedan
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()

    #Denna koden är till registreringsskärmen efter man har tryckt på register knappen, som vi stöter
    #på i koden nedan
    register_screen = Toplevel(master)
    register_screen.title('Register')


    #Här nedan är några labels som används till registreringsknappen efter man har tryckt på den. 
    #Här har jag använt en grid funktion i slutet. sticky=N, N som står för 'North gör så att den här 
    #label texten hamnar uppe på applikationen. Sedan har vi sticky=W där W är West, som gör att
    #texten hamnar på vänster sidan. Sedan har vi pady=10 vilket ger space mellan toppen och botten 
    #av applikationen, som lägger den mer i mitten av displayen, och i detta fall mellan Labeln
    #"Please enter your details below:" och "Name:", "Age:" osv.

    #Vi har också med fonter där vi först skriver namnen på fonten och efter det storleksvärdet

    #Och så har vi row. Row är som att säga vilken position var sin Label här kommer att få.
    #Man börjar alltid med 0, sedan när noll är upptagen med en label kör vi nästa på 1, nästa på 2 osv.
    Label(register_screen, text = "Please enter your details below:", font=('BankGothic Lt BT Smal', 12)).grid(row=0,sticky=N, pady=10)
    Label(register_screen, text = "Name:", font=('BankGothic Lt BT Smal', 10)).grid(row=1,sticky=W)
    Label(register_screen, text = "Age:", font=('BankGothic Lt BT Smal', 10)).grid(row=2,sticky=W)
    Label(register_screen, text = "Gender:", font=('BankGothic Lt BT Smal', 10)).grid(row=3,sticky=W)
    Label(register_screen, text = "Password:", font=('BankGothic Lt BT Smal', 7)).grid(row=4,sticky=W)
    notif = Label(register_screen, font=('BankGothic Lt BT Smal', 7))
    notif.grid(row=6, sticky=N, pady=10)

    #Det här är en Entry funktion, vilket används till att skriva in detaljerna som krävs för att
    #kunna registrera ett konto. textvariable används för att kunna spara informationen temporärt
    #På Entryn med 'textvariable=temp_password' har jag lagt till en show="*" vilket innebär att när
    #användaren skriver in lösenordet så ser man inte vad det står utan det kommer bara * tecken upp
    Entry(register_screen, textvariable=temp_name).grid(row=1, column=0)
    Entry(register_screen, textvariable=temp_age).grid(row=2, column=0)
    Entry(register_screen, textvariable=temp_gender).grid(row=3, column=0)
    Entry(register_screen, textvariable=temp_password, show="*").grid(row=4, column=0)

    #Buttons
    Button(register_screen, text="Register", command = finish_reg, font=('BankGothic Lt BT Smal', 12)).grid(row=5, sticky=N, pady=10)
def login():
    print("This is a login page")

#Här är koden för importering av bild. Här är hur man lägger till bank bilden i min app
#I Image.open('Bank.png') så läggs bilden till i koden och får variaben 'img' 
#sedan ändras storleken av bilden med img.resize
img = Image.open('Bank.png')
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

#Det här är titeln till själva appen, med en slogan också, som också görs genom att lägga till en 
#Label funktion på samma sätt som ovan
Label(master, text = "BANK CITY", font=('BankGothic Lt BT Smal', 12)).grid(row=0, sticky=N, pady=10)
Label(master, text = '"The bank that has all your needs"', font=('BankGothic Lt BT Smal', 8)).grid(row=1, sticky=N)
Label(master, image=img).grid(row=2, sticky=N, pady=15)

#Här är några buttons, där på första står det "Register" och den under står det "Login"
#Som vi ser har båda buttonen en command bredvid sin width, en är command=register och den andra
#är command=login. Dessa skickar varsin knapp till varsin unika flik där användaren antingen
#registrerar ett konto, men om den trycker login så får den en login text
Button(master, text = "Register", font=('BankGothic Lt BT Smal', 10),width=20, command=register).grid(row=3, sticky=N)
Button(master, text = "Login", font=('BankGothic Lt BT Smal', 10),width=20, command=login).grid(row=4, sticky=N, pady=5)

#Här är det som får variabeln 'master' att poppa upp på skärmen
master.mainloop()