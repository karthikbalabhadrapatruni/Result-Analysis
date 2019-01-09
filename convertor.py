from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import csv


def points(a):
    if(a=='o' or a=='O'):
        return 10
    elif(a=='s' or a=='S'):
        return 9
    elif(a=='a' or a=='A'):
        return 8
    elif(a=='b' or a=='B'):
        return 7
    elif(a=='c' or a=='C'):
        return 6
    elif(a=='d' or a=='D'):
        return 5
    else:
        return 0






def fopen(fpath,su,la):
    f=open(fpath,'r')

    L=[]
    for i in f:
        l=[]
        l=i.split(",")
        L.append(l)
    Rno=[]
    for i in range(0,len(L)):
        Rno.append(L[i][0].strip())
    s=set(Rno)
    length=len(s)
    Grades=[]
    K=0
    T=L[0][2]
    t=[]
    t.append("Roll number")
    t.append(L[0][2])
    K=K+1
    while(L[K][2]!=L[0][2]):
        t.append(L[K][2])
        K=K+1
    t.append("S.G.P.A")
    t.append("No.of backlogs")
    Grades.append(t)
    pts=su*3+la*2  
        
    A=0
    for i in range(0,length):
        l=[]
        f=0
        sgpa=0
        gpa=0
        l.append(L[A][0].strip())
        grd=L[A][3].strip()
        l.append(grd)
        if(int(L[A][4].strip())==0):
            f=f+1
                   
        gpa=gpa+points(grd)*int(L[A][4].strip())
        A=A+1
        while (L[A][0]==L[A-1][0]):
            grd=L[A][3].strip()
            l.append(grd)
            if(int(L[A][4].strip())==0):
                f=f+1    
            gpa=gpa+points(grd)*int(L[A][4].strip())
            A=A+1
            if(A==len(L)):
                break
        sgpa=gpa/pts
        
        l.append(sgpa)
        l.append(f)
            
        Grades.append(l)

    fpa=fpath[:-4]+'1.csv'
    f1=open(fpa,'w')
    with f1:
        write=csv.writer(f1,lineterminator='\r')
        write.writerows(Grades)







def grades(fpath):
    f2=open(fpath[:-4]+'1.csv','r')
    
    L=[]
    for i in f2:
        l=[]
        l=i.split(",")
        L.append(l)
    attend=len(L)-1
    totfail=0
    A=1
    for i in range(1,len(L)):
        l=L[i]
        for j in range(1,len(l)-2):
            if(L[i][j].strip()=='f' or L[i][j].strip()=='F'):

                totfail=totfail+1
                break
    totpass=attend-totfail
    subfail=[]
    l=L[0]
    for i in range(1,len(l)-2):
        subjfail=0
        for j in range(1,len(L)):
            if(L[j][i].strip()=='f' or L[j][i].strip()=='F'):
                subjfail=subjfail+1
        subfail.append(subjfail)
    F=[]
    l=L[0]
    f=[]
    f.append("subjects")
    for i in range(1,len(l)-2):
        f.append(L[0][i].strip())
    F.append(f)
    f=[]
    f.append("No.of students appeared")
    for i in range(1,len(l)-2):
        f.append(attend)
    F.append(f)
    f=[]
    f.append("No.of students passed")
    for i in subfail:
        f.append(attend-i)
    pas=f
    F.append(f)
    f=[]
    f.append("No.of Students Failed")
    for i in subfail:
        f.append(i)
    F.append(f)
    subo=[]
    l=L[0]
    subo.append("No.of outstandings in the Subject")
    for i in range(1,len(l)-2):
        subjo=0
        for j in range(1,len(L)):
            if(L[j][i].strip()=='o' or L[j][i].strip()=='O'):
                subjo=subjo+1
        subo.append(subjo)
    F.append(subo)
    subper=[]
    subper.append("Pass percent of each Subject")
    for i in range(1,len(pas)):
        per=(pas[i]/attend)*100
        subper.append(per)
    F.append(subper)
        

    dic={}
    length=len(l)-2
    for i in range(1,len(L)):
       
        dic[(L[i][length].strip())]=L[i][0]

    sgpa=[]
    col=len(l)-2
    for i in range(1,len(L)):
        sgpa.append((L[i][col].strip()))
    sgpa.sort()
    sgpa.reverse()
    Sgpa=[]
    Sgpa1=[]
    Sgpa1.append("First place")
    Sgpa1.append(dic[sgpa[0]])
    Sgpa1.append(sgpa[0])
    Sgpa.append(Sgpa1)
    Sgpa2=[]
    Sgpa2.append("Second place")
    Sgpa2.append(dic[sgpa[1]])
    Sgpa2.append(sgpa[1])
    Sgpa.append(Sgpa2)
    Sgpa3=[]
    Sgpa3.append("Third place")
    Sgpa3.append(dic[sgpa[2]])
    Sgpa3.append(sgpa[2])
    Sgpa.append(Sgpa3)
    percent=[]
    percent.append("Total pass percentage")
    per=(totpass/attend)*100
    percent.append(per)
    Sgpa.append(percent)
    
    
    f1=open(fpath[:-4]+'1.csv','a')
    with f1:
        write=csv.writer(f1,lineterminator='\r')
        write.writerows("\n")
        write.writerows("\n")
        write.writerows(F)
        write.writerows("\n")
        write.writerows("\n")
        write.writerows(Sgpa)

def change(fpath,s,l):
   
    if(s.get()!="" and l.get()!="" and s.get().isnumeric()  and l.get().isnumeric()):
        try:
            fopen(fpath,int(s.get()),int(l.get()))
            grades(fpath)
            messagebox.showinfo("COMPLETED","SUCCESSFULLY CONVERSION COMPLETED")
        except FileNotFoundError:
            print(fpath)
            messagebox.showerror("Error","INVALID PATH")

        except:
            messagebox.showerror("Error","INVALID INPUT")
    
            
            
            
                       
    
    


        
t=Tk()
def getfilename(e):
    filename=filedialog.askopenfilename(filetypes=(("CSV","*.csv"),("ALL TYPES","*.*")))
    e.insert(0,filename)
    
p=Label(t,text="path").grid(row=0)
e=Entry(t)
e.grid(row=0,column=1)
fb=Button(t,text="GETFILE",command=lambda:getfilename(e))
fb.grid(row=0,column=2)
sub=Label(t,text="Theory subjects").grid(row=1)
subj=Entry(t)
subj.grid(row=1,column=1)
la=Label(t,text="labs").grid(row=2)
lab=Entry(t)
lab.grid(row=2,column=1)
b=Button(t,text="SUBMIT",command=lambda:change(e.get(),subj,lab))
b.grid(row=3)
t.title("CONVERTOR")
t.mainloop()


