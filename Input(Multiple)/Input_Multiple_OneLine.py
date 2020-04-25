#several input in one line 

#a,b,c,d=input().spilt()

# But all of these will be counted as string

#if you want to make it integer then int(input().spilt()) will not be worked 
#Because int(input().spilt()) it will work for only one input but you have taken 4 inputs
#At this time we have to use map to make all the 4 inputs as an integer map(int,input().split())


#The Most easiest way to take the integers in one line input
a,b,c=(int(input()) for _ in range(3))

# _ marked as no usage of this _ variable : only for loop iteration