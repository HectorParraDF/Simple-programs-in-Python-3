#How many elements to display
rg = 30;

#Starting values
i_1 = 1;
i_2 = 1;

#Print the starting values
print(i_1)
print(i_2)

#Print the other rg - 2 values
for a in range(0,rg - 2):
    i_n = i_2 + i_1
    print(i_n)
    i_1 = i_n
    i_2 = i_1
(a)
