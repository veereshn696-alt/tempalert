import sys
if len(sys.argv)!=2 :
 print("usage : python script.py <temp>")
 exit(1)
script_name=sys.argv[0]
temp=float(sys.argv[1])
if temp<15 :
  print("cold")
elif temp>15 and temp<30:
  print("moderate")
else :
 print("hot")
