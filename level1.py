def level1(N):
  for i in range(2, N):
    N *= i
  return(N//100)