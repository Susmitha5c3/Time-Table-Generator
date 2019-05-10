import re


def convert_list_dict(l):
    d = {}
    for keys in l:
        d[keys] = ""
    for keys in d:
        count=0
        for i in l:
            if keys == i:
                count+=1
        d[keys] = count
    return d


def swap(a,b):
     t = a
     a = b
     b = t
     return a,b

def changeList(tot):
     l=[]
     for i in tot:
          l.append(i[0])
     return l

def labSeperate(tot):
     t=[]
     c=0
     for i in tot:
          if re.search('LAB',i[-1]):
               t.append([i[len(i)-1], c])
               for k in range(3):
                    i.remove(i[len(i)-1])
               c+=1
     return t

def constraint1(day):
     result=[]
     day=dict(sorted(day.items(), key = 
                  lambda kv:(kv[1], kv[0])))
     for sub,value in day.items():
          if value == 1:
               result.append(sub)
               day[sub]=value-1
          elif value == 2:
               result.append(sub)
               day[sub]=value-1
          elif value ==3:
               result.append(sub)
               result.insert(-1,sub)
               result.insert(-2,sub)
               day[sub]=0
     for keys in day:
          if day[keys] == 1:
               for i in range(len(result)):
                    if result[i]==keys:
                         if i == len(result)-1 and result[-4]!=keys:
                              result.insert(i-2, keys)
                         elif re.search('LAB',result[i+1]):
                              result.insert(i-1, keys)
                         else:
                              result.insert(i+2,keys)
                         day[keys]=0
                         break
     return result


def constraint2(tot):
     d=changeList(tot)
     for i in range(len(tot)):
          c=0
          for j in range(6):
               if tot[i][0] == tot[j][0]:
                    c+=1
          if c>1:
               k=2
               while(k<len(tot[i])):
                    t=0
                    if(tot[i][0] != tot[i][k]):
                         for keys in d:
                              if tot[i][k-1] == keys:
                                   t=1
                                   break
                         if(t!=1):
                              tot[i][0],tot[i][k-1]=swap(tot[i][0],tot[i][k-1])
                    k=k+1
          d =changeList(tot)
     return tot


print("Enter the periods of the day.....(labs in UPPERCASE)")
main_l = []
for i in range(6):
     l=[x for x in input().split(' ')]
     main_l.append(l)
monday = convert_list_dict(main_l[0])
tuesday= convert_list_dict(main_l[1])
wedday=convert_list_dict(main_l[2])
thursday=convert_list_dict(main_l[3])
friday=convert_list_dict(main_l[4])
satday=convert_list_dict(main_l[5])
m=constraint1(monday)
t=constraint1(tuesday)
w=constraint1(wedday)
th=constraint1(thursday)
f=constraint1(friday)
s=constraint1(satday)
tot=[m,t,w,th,f,s]
temp=labSeperate(tot)
total=constraint2(tot)
for i in temp:
     for k in range(3):
          total[i[1]].append(i[0])
for i in total:
     print(i)













