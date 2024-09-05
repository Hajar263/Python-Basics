print("      O      ")
row=6
for i in range(row):
    for j in range(row-i):
        print(' ', end='')
    for j in range(2*i+1):
        if j==0 or j==2*i or i==1 :
            print('*',end='')
        else:
            print(' ', end='')
    print()
    if i==5:
        print("*"*13," "*i, "Ramadan Kareem")
        print("*"*13, " "*i, "IEEE Al_Azhar")
row=6
for i in range(row,0,-1):
    for j in range(row-i):
        print(' ', end='')
    for j in range(2*i+1):
        if j==0 or j==2*i :
            print('*',end='')
        elif i==1:
            print('*',end='')
        else:
            print(' ', end='')
    print()
print("   *******")
print("   *******")