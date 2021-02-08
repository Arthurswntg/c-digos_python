for cont in range(1,11):
    print(cont,"",end="")
    #impedido de quebrar linha

print("\n")
for cont in range(1, 21, 3):
    print(cont)


print("\n")
for cont in range(11,0,-1):
    print(cont,"-",end="")

print("\n\n")
print("-"*15,"VALORES PARES","-"*15)
for cont in range(1,11):
    if cont % 2 == 0:
        print(cont,"",end="")