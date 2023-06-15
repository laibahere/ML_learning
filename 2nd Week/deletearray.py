print(end="Enter the size of Array:")
tot= int(input())
arr = []
print(end="Enter " + str(tot) + "Elements:")
for i in range(tot):
    arr.append(input())
print(end='\nEnter the Value to delete :')
val = input()
if val in arr:
    arr.remove(val)
    print("\n The New Array is:")
    for i in range (tot-1):
        print(end=arr[i]+"")
else:
    print("\n Elements doesnt exist in the list!")