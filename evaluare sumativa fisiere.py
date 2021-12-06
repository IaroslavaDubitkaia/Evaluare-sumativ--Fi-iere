with open('desktop/INPUT.txt', 'r') as f:
    c= f.readlines()
print(' Nr.    Numele          Prenumele      Nota1    Nota2   Nota3\n',*c)
with open('desktop/REZERVA.txt', 'w') as f:
    for i in c:
        f.write(i)
for i in c:
    c2= i.split()
    a= c2[0]+' '+c2[1]+' '+c2[2]
    media= str(float(c2[3])+float(c2[4])+float(c2[5]))
    b= a+' '+media+'\n'
    with open('desktop/OUTPUT.txt','w') as f:
        f.write(b)
with open('desktop/OUTPUT.txt','r') as f:
    m=f.readlines()
print('Nr.      Numele      Prenumele   Media\n',*m)