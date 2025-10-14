# índices em uma string

# Acessando índices em uma string
a = "Python"
print(a[0]) # P
print(a[1]) # y
print(a[2]) # t
print(a[3]) # h
print(a[4]) # o
print(a[5]) # n

# Acessando índices em uma string de forma reversa
a = "Python"
print(a[-1]) # n
print(a[-2]) # o
print(a[-3]) # h
print(a[-4]) # t
print(a[-5]) # y
print(a[-6]) # P

# Acessando índices em uma string com intervalo
a = "Python"
print(a[0:2]) # Py
print(a[2:6]) # thon
print(a[:2]) # Py
print(a[2:]) # thon
print(a[:]) # Python

# Acessando índices em uma string com intervalo negativo
a = "Python"
print(a[-4:-2]) # th
print(a[-2:]) # on
print(a[:-2]) # Pyth
print(a[-4:]) # thon
print(a[:]) # Python

# Acessando índices em uma string com intervalo e passo
a = "Python"
print(a[0:6:2]) # Pto
print(a[0:6:3]) # Ph
print(a[0:6:4]) # Po
print(a[0:6:5]) # Pn
print(a[0:6:6]) # P
print(a[0:6:7]) # P

# Acessando índices em uma string com intervalo negativo e passo
a = "Python"
print(a[-1:-6:-1]) # nohty
print(a[-1:-6:-2]) # nhy
print(a[-1:-6:-3]) # nty
print(a[-1:-6:-4]) # ny
print(a[-1:-6:-5]) # n
print(a[-1:-6:-6]) # n
print(a[-1:-6:-7]) # n

# Acessando índices em uma string com passo
a = "Python"
print(a[::2]) # Pto
print(a[::3]) # Ph
print(a[::4]) # Po
print(a[::5]) # Pn
print(a[::6]) # P
print(a[::7]) # P

# Acessando índices em uma string com passo negativo
a = "Python"
print(a[::-1]) # nohtyP
print(a[::-2]) # nhy
print(a[::-3]) # nty
print(a[::-4]) # ny
print(a[::-5]) # n
print(a[::-6]) # n
print(a[::-7]) # n

# Acessando índices em uma string com passo negativo e intervalo
a = "Python"
print(a[6:0:-1]) # nohty
print(a[6:0:-2]) # nhy
print(a[6:0:-3]) # nty
print(a[6:0:-4]) # ny
print(a[6:0:-5]) # n
print(a[6:0:-6]) # n
print(a[6:0:-7]) # n

# Acessando índices em uma string com passo negativo e intervalo
a = "Python"
print(a[-1:-6:-1]) # nohty
print(a[-1:-6:-2]) # nhy
print(a[-1:-6:-3]) # nty
print(a[-1:-6:-4]) # ny
print(a[-1:-6:-5]) # n
print(a[-1:-6:-6]) # n
print(a[-1:-6:-7]) # n
