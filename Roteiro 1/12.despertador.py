# (0≤H1≤23, 0≤M1≤59, 0≤H2≤23, 0≤M2 ≤59).
nums = input(' ')
H1 = (nums.split(' ')[0])
M1 = int(nums.split(' ')[1])
H2 = int(nums.split(' ')[2])
M2 = int(nums.split(' ')[3])

minIni = H1 * 60 + M1
minFin = H2 * 60 + M2
total = minFin - minIni 
print(total)