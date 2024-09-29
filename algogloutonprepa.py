r = []
d = []
f = open('glouton.txt','r')
t = []
dis = []
z = ' '
e = ''
textefinal = ''
for i in f:
    for mot in i:
        r.append(mot)
a = r.count('a')
b = r.count('b')
c = r.count('c')
espace = r.count(' ')
retour = r.count('\n')

d=[(a,'a'),(b,'b'),(c,'c'),(espace,'espace'),(retour,'retour')]
d = sorted(d)

for i in range(len(r)):
    if r[i]=='a':
        r[i]=0

    if r[i]==' ':
        r[i]=3

    if r[i]=='b':
        r[i]=4

    if r[i]=='c':
        r[i]=10

    if r[i]=='\n':
        r[i]=11


for i in range (len(r)):
    r[i]=bin(r[i])
    z+=str(r[i])

print(z)
z = z.replace('0b1010',' 1 0 1 0')
z = z.replace('0b0',' 0')
z = z.replace('0b100',' 1 0 0')
z = z.replace('0b11',' 1 1')
z = z.replace('0b1011',' 1 0 1 1')

print(z)
u = z.split()
while len(u)%8!=0:
    u.append('0')
print(u)
g = len(u)
print(g)
g = int(g/8)
print(g)

for i in range(g):
    e = ''
    e += u[i*8]
    e += u[i*8+1]
    e += u[i*8+2]
    e += u[i*8+3]
    e += u[i*8+4]
    e += u[i*8+5]
    e += u[i*8+6]
    e += u[i*8+7]
    t.append(e)

print(t)
for i in range(len(t)):
    t[i]=int(t[i],2)
print(t)

h = open('essai_b','wb')
B = bytes(t)
h.write(B)
h.close()
j = []
k = open('essai_b','rb')
texte_bytes = k.read()
for b in texte_bytes :
    print(b, end=' ')
    j.append(b)
print()

for i in range(len(j)):
    j[i]=bin(j[i])
    dis = []
    tata = ''
    for char in j[i]:
        dis.append(char)
    dis.reverse()
    dis.pop()
    dis.pop()
    dis.reverse()
    for i in range(len(dis)):
        tata+=dis[i]
    textefinal+=tata
textefinal.replace('0b','')
print(textefinal)
q = []
for bin in textefinal:
    q.append(bin)
for i in range(len(q)):
    q[i]=int(q[i])
print(q)
print(len(u))
finiiii=[]
for i in range(g):
    if q[i]==0:
        q.reverse()
        q.pop()
        q.reverse()
        finiiii.append('a')

    elif q[i+1]==1:
        q.reverse()
        q.pop()
        q.pop()
        q.reverse()
        finiiii.append(' ')

    elif q[i+2]==0:
        q.reverse()
        q.pop()
        q.pop()
        q.pop()
        q.reverse()
        finiiii.append('b')

    elif q[i+3]==0:
        q.reverse()
        q.pop()
        q.pop()
        q.pop()
        q.pop()
        q.reverse()
        finiiii.append('c')

    elif q[i+3]==1:
        q.reverse()
        q.pop()
        q.pop()
        q.pop()
        q.pop()
        q.reverse()
        finiiii.append('\n')

fin_de_la_fin = ''
for i in range(len(finiiii)):
    fin_de_la_fin+=finiiii[i]
print(fin_de_la_fin)