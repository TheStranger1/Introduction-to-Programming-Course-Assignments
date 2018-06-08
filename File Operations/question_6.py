
question = {'1':'name', '2':'age','3': 'weight','4':'height'}

print 'Select the criteria to sort file'

for i in range(1,5):
    print i, question[str(i)]
sort = input('Sort by which criteria: ')
print "Sorted by", question[str(sort)]+'!'

file = open('persons.dat','r')
lines = file.readlines()
list1 = []
for row in lines:
    row = row.strip()
    row = row.split(',')
    list1.append(row)
file.close()
print list1
print '........................................'
print '........................................'
def sortKey(a):
    return a[sort-1]
list2 = sorted(list1, key=sortKey)
print list2
print '........................................'
print '........................................'
print '........................................'

f = open('persons1.dat','w')

for row in list2:
    #for item in row:
    f.write(str(row))
f.close()


f = open('persons1.dat','r')
print f.read()    ## reading to check if the file has been changed
f.close()
