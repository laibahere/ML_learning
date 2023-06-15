 # implementation of the bubble sort algorithm

arr = [ 10 , 22 , 38 , 27 , 11]  #unsorted array 
temp=0


# displaying the original array 
print("the element of original array :")
for i in range(0,len(arr)):   
    print(arr[i],end="")

#sorting the array in acending order
for i in range(0,len(arr)):    # first element 
    for j in range(i+1,len(arr)):  #  2nd element 
        if(arr[i]>arr[j]):  # compare both first elementt [i] and second element [j] and if i is bigger than j 
            temp=arr[i]      #then give [i]
            arr[i]=arr[j]      # if i is equal to j 
            arr[j]=temp         
print()

#displaying the array after soting
print("\nElements of the sorted array are:")
for i in range(0,len(arr)):
    print(arr[i],end="")        