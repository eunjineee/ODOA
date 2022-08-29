D, H, W  = map(int, input().split())

x = (D**2 /(H**2 + W**2))**(1/2)

print(int(x*H),int(x*W))