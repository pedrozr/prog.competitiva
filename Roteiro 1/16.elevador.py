nums = input("")
N = int(nums.split(' ')[0])
C = int(nums.split(' ')[1])
end = "N"
P = 0 
for i in range(N):
    nums1 = input("")
    S = int(nums1.split(' ')[0])
    E = int(nums1.split(' ')[1])
    P = P + E - S
    if P > C: 
        end = "S"
        break
print(end)