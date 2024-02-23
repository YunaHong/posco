def avg(m,f):
    return str((m+f)/2)
def grade(avg):
    if avg < 60:
        return "F"
    elif avg < 70:
        return "D"
    elif avg < 80:
        return "C"
    elif avg < 90:
        return "B"
    else: 
        return "A"
slist =[]
f = open("stu.txt","r")
cnt = 0
for l in f:
    slist.append(l.split("\n"))  
    
for i in range(0,len(slist)):
    temp = slist[i][0]
    #print(temp)
    slist[i]=temp.split("\t") #이중리스트 열 0:id, 1:이름 2:중간 3:기말 
    
    slist[i].append(avg(int(slist[i][2]),int(slist[i][3])))
    slist[i].append(grade(float(slist[i][4])))

slist.sort(key = lambda x : float(x[4]), reverse = True)
    
print(slist)
f.close()
f = open("ana.txt","w")
data = ""

# for e in slist:
#     for i in range(0,len(e)):
#         data = data + e[i] +"\t"
#     data = data + "\n"

# print(data)
# f.write(data)
title = "{:^9}\t{:>18}\t{:^15}\t{:^15}\t{:^15}\t{:^15}\n".format("Student", "Name", "Midterm", "Final", "Average", "Grade")
f.write(title)
lines = "----------" * 10 + "\n"
f.write(lines)
for i in range(0,len(slist)):
    data += "{:^9}\t{:>18}\t{:^15}\t{:^15}\t{:^15}\t{:^15}\n".format(slist[i][0],slist[i][1],slist[i][2],slist[i][3],slist[i][4],slist[i][5])
    
f.write(data)
f.close()
#######search함수실험#####
target = input("Student ID:")
f = open("ana.txt","r")
for l in f:
    if target in l:
         title = "{:^9}\t{:>18}\t{:^15}\t{:^15}\t{:^15}\t{:^15}\n".format("Student", "Name", "Midterm", "Final", "Average", "Grade")
         lines = "----------" * 10 + "\n"
         print(title, lines)
         print(l,end = "")
    else:
         print("NO SUCH PERSON.")

f.close()
