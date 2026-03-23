n1 = n1 = str(input('digite seu sexo')).strip().upper()[0]
while n1 not in 'MF' :
    n1 = str(input('dados invalidos digite seu sexo novamente'))
print('sexo registrado com suceso:',n1)
