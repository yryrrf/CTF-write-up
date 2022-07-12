a = "54 396 131 198 225 258 87 258 128 211 57 235 114 258 144 220 39 175 330 338 297 288"
text =""
for each in a.split(' '):
     text= text+ str(int(each)%37)+" "

data = text.split(' ')
def convert(data):
     for i in range(len(data)-1):
             if(data[i]=="36"):
                     data[i] = "_"
             elif int(data[i])>=0 and int(data[i])<=25:
                     data[i] = chr(97+int(data[i]))
             else:
                     data[i] = int(data[i]) - 26
     return data
ans = convert(data)
for i in ans:
        print(i, end="");


# r0und_n_r0und_79c18fb3
