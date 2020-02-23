def npol(op):
    operador = ['+', '-', '/', '*']
    d = ''
    pila = []
    aux = []
    exp = []
    #Separa la expresión
    for elemento in op:
        exp.append(elemento)
    #Hace la notación polaca
    for caracter in exp:
        if (caracter not in operador) and (caracter != ')') and (caracter != '('):
            pila.append(caracter)
        elif (caracter in operador) and (caracter != ')') and (caracter != '('):
            if len(aux) != 0:
                if aux[-1] == '(':
                    d = aux.pop()
                if (len(aux) != 0) and (operador.index(caracter) <= operador.index(aux[-1])):
                    c = aux.pop()
                    pila.append(c)
                elif (len(aux) != 0) and (operador.index(caracter) >= operador.index(aux[-1])):
                    pila.append(caracter)
                if d == '(':
                    aux.append(d)
            aux.append(caracter)
            if pila[-1] == aux[-1]:
                aux.pop()
        elif caracter == '(':
            aux.append(caracter)
        elif caracter == ')':
            if len(aux) == 0:
                pass
            else:
                while aux[-1] != '(':
                    c = aux.pop()
                    pila.append(c)
            aux.pop()
    while len(aux) > 0:
        if aux[-1] in pila:
            aux.pop()
        else:
            c = aux.pop()
            pila.append(c)
    pila.reverse()
    print(''.join(pila))
    
npol("A+B/C")
npol("A+(B*C)")
