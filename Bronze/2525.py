ch, cm = map(int, input().split())
rm = int(input())

rt = cm + rm
if(rt <  60):
 print(ch, rt)
else:
 ch = int(ch + rt / 60)
 if(ch < 24):
  print(ch, rt % 60)
 else:
  print(ch - 24, rt % 60)
 
