import sys
text = sys.stdin.read()
z = text.split()
print(z)
a = "ID\tFROM\tLEMMA\tUPOS\tXPOS\tFEATS\tHEAD\tDEPREL\tDEPS\tMISC"
print(a)
for i in range(len(z)):
        print("%d\t%s\t-\t-\t-\t-\t-\t-\t-"%(i+1,z[i]))
