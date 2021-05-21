class Solution(object):
   def isHappy(self, n):
      return self.solve(n,{})
   def solve(self,n,visited):
      if n == 1:
         return True
      if n in visited:
         return False
      visited[n]= 1
      n = str(n)
      l = list(n)
      l = list(map(int,l))
      temp = 0
      for i in l:
         temp += (i**2)
      return self.solve(temp,visited)
ob1 = Solution()
for i in range(1,101):
   op = ob1.isHappy(i)
   print("{}Is Happy:".format(i),op);