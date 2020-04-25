#Return True if all of the elements are positive and any of the elements is Pallindrome number
#Otherwise return False


def ispositive(l):
    flag=True
    for x in l:
        if x<0:
            flag=False
            break
        else:
            flag=True
    return flag

def ispallin(l):
    flag=True
    for x in l:
        #Reverse or Pallindrome Check
        if x==x[::-1]:
            flag=True
            break
        else:
            flag=False
    return flag       
n=input()#string
str=input()#string
str_li=str.split()#list containing string elements
li=list(map(int,str.split()))#list converting the string elements to integer

if(all([ispositive(li),ispallin(str_li)])):
    print(True)
else:
    print(False)    


*****************************************************
### Replace

#The above code blocks can be replaced by the following codes:
N,n = int(input()),input().split()
print all([int(i)>0 for i in n]) and any([j == j[::-1] for j in n])
