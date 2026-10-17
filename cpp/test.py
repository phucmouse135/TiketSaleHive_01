# Bai 1 
# n ,m = map(int ,input().split())
# print((int(n//m) + 1) * m)

# Bai 2 
n , m = map(int , input().split())
s = input()
count = [0] * 27
for i in range(len(s)):
  a = ord(s[i]) - ord('A') 
  count[a]+=1

minn = 100001
for i in range(m): 
  minn = min(minn, count[i])
#   print(count[i] , i )
print(minn * m)
  
# Bai 3 
