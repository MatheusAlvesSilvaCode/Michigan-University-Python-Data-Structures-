fh = open('mbox-short.txt')

for lx in fh:
    ly = lx.rstrip()
    #print(ly.upper())


friends = ['Matheus','lucas','Nathalia','Antonio']
print(list(range(len(friends))))

t = [1,2,3,4,5,6]



print(t[2:6])
t[:4]

stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)

nums = [5,5,7,3,10]
print(len(nums))

print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))


numlist = list()


#while True:
 #   inp = input('Enter a number: ')
  #  if inp == 'done' : break
   # value = float(inp)
    #numlist.append(value)

#average = sum(numlist)/ len(numlist)
#print(average)


abc = 'Árvore de três galhos'
abc_split = abc.split()
print(abc_split)
print(len(abc_split))
print(abc_split[3])

for w in abc_split: 
    print(w)

line = 'firts;second;third'

line_clean = line.split()
print(line_clean)
print(len(line_clean))
thing = line.split(';') # Adicionar parametros de separaçao para o split
print(thing)
print(len(thing))

print('------Ex: 4--------')

han = open('mbox-short.txt')
for line in han:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 1 :
        continue
    if wds[0] != 'From' :
        continue
    print(wds[2]) 