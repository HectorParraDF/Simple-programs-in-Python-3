#This simple script prints out the Fibonacci sequence up to the entry n = rg.

#Print formatting style
style = "{0:10}{1:10}"

#How many elements to display
rg = 30;

#Starting values
i_1 = 1
i_2 = 1

#Print the starting values
print(style.format(1, i_1))
print(style.format(2, i_2))

#Print the other rg - 2 values
for a in range(3, rg + 1):
    i_n = i_2 + i_1
    print(style.format(a, i_n))
    i_1 = i_2
    i_2 = i_n
    (a)
