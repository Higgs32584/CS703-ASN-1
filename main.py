from matplotlib import pyplot as plt
def blank_check(y):
    if y == "\n" or y == " ":
        return True
    return False
def readtolist(filepath):
    f = open(filepath, "r")
    strbuild = ""
    data = []
    for x in f:
        for y in x:
            if blank_check(y):
                data.append(int(strbuild))
                strbuild=""
            elif blank_check(y):
                data.append(int(strbuild))
                strbuild=""
            else:
                strbuild = strbuild+y
    if strbuild != "":
        data.append(int(strbuild))
    
    print(data)
    
    return data

data = readtolist("/data/CS703/A1/test.txt")

ydata=readtolist("/data/CS703/A1/ages.txt")
xdata=readtolist("/data/CS703/A1/years.txt")

plt.plot(xdata,ydata,color='blue',marker='o',linestyle='dotted')
plt.title("Ages Over Time")
plt.xlabel("Years")
plt.ylabel("Ages")

xdata_fil=[]
ydata_fil=[]
c=[10,20,30,40,50]
for x in range(len(xdata)):
    if(xdata[x] < 2021 and xdata[x] > 2000):
        xdata_fil.append(xdata[x])
        ydata_fil.append(ydata[x])

plt.scatter(xdata_fil, ydata_fil,marker='o',linestyle='solid')
