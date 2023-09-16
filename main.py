
def Raiz(num):
    varAuxiliar = 1.00
    for nIteraciones in range(1,10):
        varAuxiliar = ( varAuxiliar + num/varAuxiliar )/2
    return varAuxiliar

if __name__ == '__main__':
    numIngresado = float(input("Ingrese un número a sacar su Raíz  : "))
    numRaiz = Raiz(numIngresado)
    print (f"La raíz del número ingresado es {numRaiz}")
