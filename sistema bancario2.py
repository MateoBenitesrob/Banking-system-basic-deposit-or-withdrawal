cuentas = {"mateo" : 3400,
           "joaquim" : 500,
           "luciano" : 600,
           "vasquibidi" : 568}

def retirar_dinero(usuario, monto_retirar):

    saldo =  cuentas[usuario]


    # Retirar dinero
    retiro = saldo - monto_retirar
    print(f"Retiro exitoso\nha retirado {retiro} dolares")



def depositar_dinero(usuario, monto_depositar):

    saldo = cuentas[usuario]

    # Depositar
    depositar = saldo + monto_depositar
    print(f"Deposito exitoso\nha depositado {depositar} dolares")

print("Escriba los siguientes nombres: mateo, joaquim, luciano, vaskibidi.")
usuario = input("Escriba su nombre: ")
if usuario.isalpha():
    if usuario in cuentas:
        menú = input("escriba uno de los siguientes métodos: retirar/depositar. ")
        if menú.isalpha():
            if menú == "retirar":
                monto_retirar = input("Escriba el monto que desea retirar: ")
                if monto_retirar.isdigit():

                    monto_retirar = int(monto_retirar)
            
                    retirar_dinero(usuario, monto_retirar)
                else:
                    print("Indique el monto que desee realizar.")
            
            elif menú == "depositar":
                monto_depositar = input("Escriba el monto que desee depositar: ")
                if monto_depositar.isdigit():

                    monto_depositar = int(monto_depositar)

                    depositar_dinero(usuario, monto_depositar)

                else:
                    print("Indique el monto que desee realizar")
            else:
                print("Escriba una de las dos opciones.")   
        else:
            print("Inténtelo de nuevo.")
    else:
        print("Escriba los siguientes nombres: mateo, joaquim, luciano, vaskibidi. Nuevamente.")
else:
    print("Escriba su nombre nuevamente.")