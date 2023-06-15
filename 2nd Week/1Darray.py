print("How many element to store inside the array?",end="")
num=input()
arr=[]
print('\nEnter',num,"element:",end="")
num=int(num)
for i in range(num):
    element=input()
    arr.append(element)
print("\nThe array elements are ")
for i in range(num):
    print(arr[i],end="")