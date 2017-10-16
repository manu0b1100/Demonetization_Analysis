from tkinter import *
from tkinter import messagebox
from Charts import Demon

def barplot():
    demon.getBarSentiment(var.get())

def getMap():
    demon.showmap(var2.get())
    master.quit()

def getDateGraph():
    sentiment=[]
    granularity=[]
    paper=[]



    if sent.get()==0:
        sentiment.extend([-1,1])
    else:
        sentiment.append(sent.get())

    if gran.get()=='day':
        granularity.extend(['year','month','day'])
    if gran.get()=='month':
        granularity.extend(['year','month'])
    if gran.get()=='year':
        granularity.append('year')

    if pap.get()=="All":
        paper.extend(['toi','The Hindu'])
    else:
        paper.append(pap.get())

    demon.showDateGraph(startDateEntry.get(),endDateEntry.get(),sentiment=sentiment,granularity=granularity,paper=paper)

master = Tk()
demon=Demon.Demon()


labelText3=StringVar()
labelText3.set("Get Sentiment bargraph based in the following attributes")
labelDir3=Label(master, textvariable=labelText3)
labelDir3.pack()
var=StringVar(master)
var.set("Paper")

option=OptionMenu(master,var,*['Category','City','Paper'])
option.pack()

button=Button(master,text="plot",command=barplot)
button.pack()




labelText4=StringVar()
labelText4.set("Get Map based on Sentiment")
labelDir4=Label(master, textvariable=labelText4)
labelDir4.pack()

var2=IntVar(master)
var2.set(-1)
option2=OptionMenu(master,var2,*[-1,1])
option2.pack()

mapbutton=Button(master,text='GetMap',command=getMap)
mapbutton.pack()


labelText5=StringVar()
labelText5.set("Get Sentiment Timeline")
labelDir5=Label(master, textvariable=labelText5)
labelDir5.pack()

labelText1=StringVar()
labelText1.set("Enter Start Date Format- YYYY-MM-DD")
labelDir1=Label(master, textvariable=labelText1)
labelDir1.pack()
startDateEntry=Entry(master)
startDateEntry.pack()


labelText2=StringVar()
labelText2.set("Enter End Date Format- YYYY-MM-DD")
labelDir2=Label(master, textvariable=labelText2)
labelDir2.pack()
endDateEntry=Entry(master)
endDateEntry.pack()

sent=IntVar(master)
sent.set(-1)
option3=OptionMenu(master,sent,-1,1,0)
option3.pack()

gran=StringVar(master)
gran.set('year')
option4=OptionMenu(master,gran,'year','month','day')
option4.pack()

pap=StringVar(master)
pap.set('toi')
option5=OptionMenu(master,pap,'toi','The Hindu','All')
option5.pack()

Datebutton=Button(master,text='Dategraph',command=getDateGraph)
Datebutton.pack()

mainloop()



