from sys import argv

print 'Number of arguments:', len(argv), 'arguments.'
f1, f2, f3 = argv
print f2
txt = open(f2, 'r')
for line in txt:
	print line

txt2 = open(f3,'w')
txt2.write('test2')

txt.close()
txt2.close()