#_*_ coding:utf-8 _*_

from tkinter import *
from connectDB import cur, conn
from tkinter import messagebox

current_page = 1
total_page = 0
pages = ""
btns = []
entrys = []

def updateRecord(no, code, country, city, population) :
    #print(no, code, country, city, population)
    print(entrys[no].get(), entrys[code].get(), entrys[country].get(), entrys[city].get(), entrys[population].get())
    
def showDB():
    cur.execute("select * from worldPopulation order by 순번 asc")
    for row in cur.fetchall() :
        print(row)

def showColumn():
    lbl1 = Label(columnFrame, width=5, text='순번', relief='ridge', bg='yellow')
    lbl1.grid(row=0, column=0)
    lbl2 = Label(columnFrame, width=10, text='국가코드', relief='ridge', bg='yellow')
    lbl2.grid(row=0, column=1)
    lbl3 = Label(columnFrame, width=20,text='국가', relief='ridge', bg='yellow')
    lbl3.grid(row=0, column=2)
    lbl4 = Label(columnFrame, width=20,text='수도', relief='ridge', bg='yellow')
    lbl4.grid(row=0, column=3)
    lbl5 = Label(columnFrame, width=20, text='인구', relief='ridge', bg='yellow')
    lbl5.grid(row=0, column=4)

def showEntry() :
    global total_page, current_page, btns, entrys
    btns = []
    entrys = []
    sql = "select * from worldPopulation order by 순번 asc"
    cur.execute(sql)
    total_page = len(cur.fetchall()) #레코드 수
    
    limit_page = 10
    total_page = round(total_page / limit_page) #총 페이지수

    sql = "select * from worldPopulation order by 순번 asc limit %s OFFSET %s"
    cur.execute(sql, (limit_page, (current_page-1) * limit_page))

    # 기존 Entry 삭제 ##########################################
    for (i, child) in enumerate(columnFrame.winfo_children()):
        #print(i, child)
        if (i <= 4): continue
        child.destroy()
    ############################################################

    for i in range(1, 11) :
        row = cur.fetchone()
        for j in range(5) :

            if row != None :
                entry = Entry(columnFrame)
                entry.grid(row=i, column =j)

                if j==0 : entry.configure(width=5)
                if j==1 : entry.configure(width=10)
                if j==2 : entry.configure(width=20)
                if j==3 : entry.configure(width=20)
                if j==4 : entry.configure(width=20)
                entry.insert(END, row[j])
                entrys.append(entry)
        if row != None :
            #print(no, code, country, city, population)
            btn = Button(columnFrame, text="Edit")
            btn.grid(row=i, column=5, padx=5)
            btns.append(btn)
    try :
        btns[0].configure(command=lambda:updateRecord(0,1,2,3,4))
        btns[1].configure(command=lambda:updateRecord(5,6,7,8,9))
        btns[2].configure(command=lambda:updateRecord(10,11,12,13,14))
        btns[3].configure(command=lambda:updateRecord(15,16,17,18,19))
        btns[4].configure(command=lambda:updateRecord(20,21,22,23,24))
        btns[5].configure(command=lambda:updateRecord(25,26,27,28,29))
        btns[6].configure(command=lambda:updateRecord(30,31,32,33,34))
        btns[7].configure(command=lambda:updateRecord(35,36,37,38,39))
        btns[8].configure(command=lambda:updateRecord(40,41,42,43,44))
        btns[9].configure(command=lambda:updateRecord(45,46,47,48,49))
    except Exception as e :
        print(e)
    
def prev_page():
    global current_page, total_page
    if current_page > 1 :
        current_page = current_page - 1
    
    pages.set(str(current_page) + " / " + str(total_page))
    showEntry()

def next_page() :
    global current_page, total_page

    if current_page < 20 : 
        current_page = current_page + 1

    pages.set(str(current_page) + " / " + str(total_page))
    showEntry()

def showBtn():
    global pages
    
    prev_btn = Button(btnFrame, text ="<", command=prev_page)
    prev_btn.pack(side=LEFT, padx=10)

    pages = StringVar()
    pages.set(str(current_page) + " / " + str(total_page))
    page_state = Label(btnFrame, textvariable = pages)
    page_state.pack(side = LEFT, padx=10)
    
    next_btn = Button(btnFrame, text = ">", command=next_page)
    next_btn.pack(side=LEFT, padx=10)
    
root = Tk()
root.title("세계 나라별 인구수 테이블")
root.geometry("600x320")

columnFrame = Frame(root)
columnFrame.pack()

btnFrame = Frame(root)
btnFrame.pack()

showColumn()
showEntry()
showBtn()

root.mainloop()
