def level1(N):
   factorial = 1
   for i in range(2, N+1):
      factorial *= i
   s = str(factorial)
   first_digit = int(s[0])
   return first_digit
