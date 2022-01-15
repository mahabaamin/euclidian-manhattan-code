import random
import pandas as pd
import numpy as np
import math
points = [[3, 4],[3, 6],[3, 8],[4, 5],[4, 7],[5, 1],[5, 5],[7, 3],[7, 5],[8, 5],]
points2 = [[3, 4],[3, 6],[3, 8],[4, 5],[4, 7], [5, 1], [5, 5], [7, 3], [7, 5], [8, 5],]
k = int(input("Enter the value of K: "))
userchooce = int(input("Enter yor chice 1-euclidian \n 2-manhattan"))
RANDOMpoints = []
m = []
Csum = [[0, 0] for _ in range(k * 2)]
C = [[] for _ in range(k)]
NEWpoints = [0 for _ in range(k * 2)]
flag = True
flag2 = True
nums = [[] for _ in range(k)]
Cname = []
X = []
Y = []
Counter = 0
Cchoose = [[] for _ in range (k*2)]
#put the random points in list
for l in range(k):
    RANDOMpoints.append(random.choice(points2))
    #add 0 for ever random value 
    m.append(0)
#check if there's similir points
while True:
    if not flag:
        break
    for q in range(k - 1):
        for w in range(q + 1, k):
            if RANDOMpoints[q] == RANDOMpoints[w]:
              flag = True
              print('\nsame points  flag.\nplease Choosing another random points')
              RANDOMpoints.clear()
            for l in range(k):
                RANDOMpoints.append(random.choice(points2))
                print("\nThe new points are: ", RANDOMpoints)
            else:
                flag = False
print(RANDOMpoints)

def euclidian():
    print("Manhattan")
    global flag2
    global Csum
    global C
    global nums
    global Counter
    global Cchoose
    while True:
        Csum.clear()
        Cchoose.clear()
        Cchoose = [[] for _ in range (k*2)]
        C.clear()
        C = [[] for _ in range(k)]
        nums.clear()
        nums = [[] for _ in range(k)]
        Cname.clear()
        Csum = [[0, 0] for _ in range(k * 2)]
        X.clear()
        Y.clear()
        flag2 = True
        Counter += 1
        for i in range(len(points)):
            for n in range(k):
                m[n] = round(math.sqrt(math.pow((points[i][0] - RANDOMpoints[n][0]), 2) + math.pow((points[i][0 + 1] - RANDOMpoints[n][0 + 1]),2)), 2)
                nums[n].append(m[n])
            mini = min(m)
            for y in range(k):
                if m[y] == mini:
                    C[y].append(round(mini, 2))

                    name = 'cluster {}'.format(y + 1)
                    Cname.append(name)

                    X.append(points[i][0])
                    Y.append(points[i][0 + 1])
                    Cchoose[y*2]=y
                    Cchoose[(y*2)+1]=y
                    Csum[y*2][0]+=points[i][0]
                    Csum[(y*2)+1][0]+=points[i][0+1]
                    break

        for a in range(k * 2):
            NEWpoints[a] = round(Csum[a][0] / len(C[Cchoose[a]]), 2)

        print('\n{} Iteration: \n',Counter)
        print('\npoints: ', points)
        print('\ndistance: ' ,nums)
        print('\nx:' ,X)
        print('\ny:', Y)

        print('\t Sum \t Average \t New(M)')
        for o in range(k * 2):
            if o % 2 == 0:
                val = '(X)'
            else:
                val = '(Y)'

            print('Cluster{}{}\t{}\t{}\tNewM{} = {}'.format(Csum[o][0] + 1, val,Csum[o][1], NEWpoints[o],Cchoose[0] +1,Csum[o][0] + 1, NEWpoints[o]))

        p = 0
        c = 0
        for r in range(k):
            if NEWpoints[p] != RANDOMpoints[r][0] or NEWpoints[p + 1] != RANDOMpoints[r][0 + 1]:
                for t in range(k):
                    RANDOMpoints[t][0] = NEWpoints[c]
                    RANDOMpoints[t][1] = NEWpoints[c + 1]
                    c += 2

                flag2 = False
                break

            p += 2

        if flag2:
           
            exit(0)



def manhattan():
    print("Manhattan")
    global flag2
    global Csum
    global C
    global nums
    global Counter
    global Cchoose
    while True:
        Csum.clear()
        C.clear()
        C = [[] for _ in range(k)]
        nums.clear()
        nums = [[] for _ in range(k)]
        Cname.clear()
        Csum = [[0, 0] for _ in range(k * 2)]
        Cchoose.clear()
        Cchoose = [[] for _ in range (k*2)]
        X.clear()
        Y.clear()
        flag2 = True
        Counter += 1

        for i in range(len(points)):
            for n in range(k):
                m[n] = round(abs(points[i][0] - RANDOMpoints[n][0]) + abs(points[i][0 + 1] - RANDOMpoints[n][0 + 1]), 2)

                nums[n].append(m[n])

            mini = min(m)
            for y in range(k):
                if m[y] == mini:
                    C[y].append(round(mini, 2))

                    name = 'cluster {}'.format(y + 1)
                    Cname.append(name)

                    X.append(points[i][0])
                    Y.append(points[i][0 + 1])
                    Cchoose[y*2]=y
                    Cchoose[(y*2)+1]=y
                    Csum[y*2][0]+=points[i][0]
                    Csum[(y*2)+1][0]+=points[i][0+1]
                    break

        for a in range(k * 2):
            NEWpoints[a] = round(Csum[a][0] / len(C[Cchoose[a]]), 2)

        print('\n{}Iteration:\n',Counter)
        print('\npoints: ', points)
        print('\ndistance: ' ,nums)
        print('\nx:' ,X)
        print('\ny:', Y)

        print("****************************")
        print('\t\t Sum \t Average \tNew(M)')
        for o in range(k * 2):
            if o % 2 == 0:
                val = '(X)'
            else:
                val = '(Y)'

            print('Cluster{}{}\t{}\t{}\tNewM{} = {}'.format(Csum[o][0] + 1, val, Csum[o][1], NEWpoints[o],Csum[o][0] + 1, NEWpoints[o]))

        p = 0
        c = 0
        for r in range(k):
            if NEWpoints[p] != RANDOMpoints[r][0] or NEWpoints[p + 1] != RANDOMpoints[r][0 + 1]:
                for t in range(k):
                    RANDOMpoints[t][0] = NEWpoints[c]
                    RANDOMpoints[t][1] = NEWpoints[c + 1]
                    c += 2

                flag2 = False
                break

            p += 2

        if flag2:
            
            exit(0)





def switch(arg):
    if arg == 1:
       euclidian()
    elif arg == 2:
      manhattan()
    else:
        print("Please choose from the menu")



switch(userchooce)
