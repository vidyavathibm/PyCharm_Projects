str=raw_input()
l=len(str)
up=0;
low=0;
for x in str:
    if x>=65 and x<=90:
        up=up+1
    else:
        low=low+1
print "UPPER CASE ",up
print "LOWER CASE ",low

