#_*_ coding:utf-8 _*_

from tkinter import *
from connectDB import cur, conn
from tkinter import messagebox

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
    

root = Tk()
root.title("세계 나라별 인구수 테이블")
root.geometry("600x320")

columnFrame = Frame(root)
columnFrame.pack()

showColumn()
showEntry()


root.mainloop()
