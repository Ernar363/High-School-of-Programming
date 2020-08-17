def level1(N):
factorial = 1
if N == 0:
    return(1)
elif N == 1:
    return(1)
else:
   for i in range(2, N+1):
      factorial *= i
   s = str(factorial)
   first_digit = int(s[0])
   return(first_digit)
