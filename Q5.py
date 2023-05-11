sub1 = 65
sub2 = 55
sub3 = 89
sub4 = 95
sub5 = 23
sub6 = 35
totalmarks = sub1 + sub2 + sub3 + sub4 + sub5 + sub6
print(totalmarks)
averagemarks = totalmarks/6
print(averagemarks)
if averagemarks >= 91 and averagemarks <= 100:
    print("A1")
elif averagemarks >= 81 and averagemarks < 91:
    print("A2")
elif averagemarks >= 71 and averagemarks < 81: 
    print("B1") 
elif averagemarks >= 61 and averagemarks < 71:
    print("B2")
elif averagemarks >= 51 and averagemarks < 61:
    print("C1") 
elif averagemarks >= 41 and averagemarks < 51:
    print("C2") 
elif averagemarks >= 31 and averagemarks < 41:
    print("D1")
elif averagemarks >= 21 and averagemarks < 31:
    print("D2")
elif averagemarks >= 11 and averagemarks < 21:
    print("E1") 
elif averagemarks >= 0 and averagemarks < 11:
    print("E2")
else:
    print("invalid input")           