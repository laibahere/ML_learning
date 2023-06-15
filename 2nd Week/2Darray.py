## Create a two-dimensional integer array and insert numbers to the maximum size provided until the end of the array. Access the numbers inserted and then display the same as output.

r_num = int(input("Input number of rows:"))
c_num = int(input("Input number of columns:"))
twod_arr = [[0 for col in range(c_num)] for row in range(r_num)]

for row in range(r_num):
   for  col in range(c_num):
    twod_arr[row][col]= row * col 

print(twod_arr)