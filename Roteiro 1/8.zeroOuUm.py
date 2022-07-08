nums = input('')

A = int(nums.split(' ')[0])
B = int(nums.split(' ')[1])
C = int(nums.split(' ')[2])

nums = [A,B,C]

countZero = nums.count(0)

match countZero:
    case 1: 
        if A == 0:
            print("A")
        elif B == 0:
            print("B")
        elif C == 0:
            print("C")
    case 2: 
        if A != 0:
            print ("A")
        elif B != 0:
            print ("B")
        elif C != 0:
            print ("C")
    case 3:
        print ("*")
    case 0:
        print ("*")
