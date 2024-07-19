from tkinter import Tk, ttk
from tkinter import * #type:ignore

import requests
import json

#colors

clr0 = "#FFFFFF"  #WHITE
clr1 = "#333333"  #BLACK
clr2 = "#EB5D51"  #RED


window = Tk()
window.geometry('300x320')
window.title('converter')
window.configure(bg=clr0)
window.resizable(height=FALSE, width=FALSE)


#frames

top = Frame(window, width=300, height=60, bg=clr2)
top.grid(row=0, column=0)

main = Frame(window, width=300, height=260, bg=clr0)
main.grid(row=1, column=0)



def convert():

    url = "https://currency-conversion-and-exchange-rates.p.rapidapi.com/convert"


    currency_1= combo1.get()
    currency_2= combo2.get()
    amount= value.get()
    querystring = {"from":currency_1,"to":currency_2,"amount":amount}

    if currency_2=="USD":
        symbol='$'
    elif currency_2=="INR":  
        symbol='₹' 
    elif currency_2=="BDT":
        symbol='Taka'  
    elif currency_2=="EUR":
        symbol='€'   
    elif currency_2=="GBP": 
        symbol='£'  
    elif currency_2=="CAD": 
        symbol='Can$'    
    elif currency_2=="AUD": 
        symbol='AU$'  
    elif currency_2=="JPY": 
        symbol='¥'  
    elif currency_2=="CHF": 
        symbol='swiss franc'    
    elif currency_2=="CNY": 
        symbol='chinese$'  
    elif currency_2=="SGD": 
        symbol='S$'  

    headers = {
    "x-rapidapi-key": "5c3f34fb42mshb5de68f15bd30a9p183b80jsn1512de77e1cc",
    "x-rapidapi-host": "currency-conversion-and-exchange-rates.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = json.loads(response.text)
    converted_amount = data["result"]
    formatted =symbol+ "{:,.2f}".format(converted_amount) #type:ignore
    result['text'] = formatted
    print(formatted)






#top frame

app_name = Label(top, text="Currency Converter", width=20, padx=13, pady=15, anchor=CENTER, font=('Arial 16 bold'),bg=clr2, fg=clr0)
app_name.place(x=0, y=0)

#main frames

result =  Label(main, text=" ", width=16, height=2, pady=7, relief="solid", anchor=CENTER, font=('Ivy 15 bold'),bg=clr0, fg=clr1)
result.place(x=50, y=10)


currency = ['INR', 'USD', 'BDT', 'EUR', 'GBP', 'CAD', 'AUD', 'CHF', 'JPY', 'CNY', 'SGD']


from_label =  Label(main, text="From", width=8, height=1, padx=0, pady=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=clr0, fg=clr1)
from_label.place(x=48, y=90)
combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo1['values'] = (currency)
combo1.place(x=50, y=115)


to_label =  Label(main, text="To", width=8, height=1, padx=0, pady=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=clr0, fg=clr1)
to_label.place(x=158, y=90)
combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo2['values'] = (currency)
combo2.place(x=160, y=115)



value = Entry(main, width=22, justify=CENTER, relief="solid", font=("Ivy 12 bold"))
value.place(x=50, y=155)

button = Button(main, text="Convert", width=19, padx=5, height=1, bg=clr2, fg=clr0, font=('Ivy 12 bold'), relief='solid', command=convert)
button.place(x=50, y=210)






window.mainloop()


