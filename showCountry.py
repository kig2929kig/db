#_*_ coding:utf-8 _*_

from tkinter import *
from connectDB import cur, conn
from tkinter import messagebox

current_page = 1
total_page = 0
pages = ""

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
    global total_page

    sql = "select * from worldPopulation order by 순번 asc"
    cur.execute(sql)
    total_page = len(cur.fetchall())  

    sql = "select * from worldPopulation order by 순번 asc"
    cur.execute(sql)
       
    for i in range(1, 11) :
        row = cur.fetchone()
        for j in range(5) :
            entry = Entry(columnFrame)
            entry.grid(row=i, column =j)

            if j==0 : entry.configure(width=5)
            if j==1 : entry.configure(width=10)
            if j==2 : entry.configure(width=20)
            if j==3 : entry.configure(width=20)
            if j==4 : entry.configure(width=20)
            entry.insert(END, row[j])

def prev_page():
    global current_page, total_page
    current_page = current_page - 1
    pages.set(str(current_page) + " / " + str(total_page))

def next_page() :
    global current_page, total_page
    current_page = current_page + 1
    pages.set(str(current_page) + " / " + str(total_page))

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