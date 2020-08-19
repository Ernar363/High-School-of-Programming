def odometer(oksana: list):
  hour = 0
  kilometr = 0
  for i in range(len(oksana)):
    if i%2 != 0:
       hour = oksana[i] + hour
    else:
       kilometr = kilometr + oksana[i]
  ras = hour * kilometr
  return(ras)