# i=0
# while i<5:
#     j=1
#     while j<=i:
#         print(' ',end='')
#         j=j+1
#     j=1
#     while j<=9-2*i:
#         print('*',end='')
#         j=j+1
#     print()
#     i+=1


a = 0
k = 9
for i in range(1, a+1):
    for space in range(1, (a-i)+1):
        print(end="  ")

    while k != (2*i-1):
        print("* ", end="")
        k += 1

    k = 0
    print()
