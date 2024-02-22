import sys
input_f = sys.argv[1]
output_f = sys.argv[2]
#input file
f = open(input_f,"r")
l = f.readlines()
f.close()

#output file
f = open(output_f,"w")
for line in l:
    f.write(line)
f.close()
