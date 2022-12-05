import math
a, b, c = map(int, input().split())

if (c-b) == 0:
  print(-1)
else:
  if a == 0:
    if (c-b) < 0:
      print(-1)
    else:
      print(math.floor((c-b))+1)
  else:
    if a/(c-b) < 0:
      print(-1)
    else:
      print(math.floor(a/(c-b))+1)
