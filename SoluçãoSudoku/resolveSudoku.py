def addbloco(x):
    bloco.append(x.copy())
    x.clear()
    
def addsublista(a, b):
    temp = [b]
    temp.append(b)
    subLista[a].append(temp[:])
    del(temp)


from random import randint
subLista = []
bloco = []
for l in range(9):
    for c in range(9):
        n = randint(0, 9)#int(input(f"Digite o valor [{l}][{c}] "))
        if n >= 0 and n < 10:
            while True:
                for i in range(1,10):
                    if l <= 2:
                        if c >= 0 and c <= 2:
                            numero = i
                            addsublista(numero, n)
                            addbloco(subLista)
                            break
                        if c >= 3 and c <= 5:
                            subLista['b'] = n
                            addbloco(subLista)
                            break
                        if c >= 6:
                            subLista['c'] = n
                            addbloco(subLista)
                            break
                    if l > 2 and l <= 5:
                        if c >= 0 and c <= 2:
                            subLista['d'] = n
                            addbloco(subLista)
                            break
                        if c >= 3 and c <= 5:
                            subLista['e'] = n
                            addbloco(subLista)
                            break
                        if c >= 6:
                            subLista['f'] = n
                            addbloco(subLista)
                            break
                    if l > 5 and l <= 8:
                        if c >= 0 and c <= 2:
                            subLista['g'] = n
                            addbloco(subLista)
                            break
                        if c >= 3 and c <= 5:
                            subLista['h'] = n
                            addbloco(subLista)
                            break
                        if c >= 6:
                            subLista['i'] = n
                            addbloco(subLista)
                            break
