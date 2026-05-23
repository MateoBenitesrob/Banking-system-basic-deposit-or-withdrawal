import time
cuentas = {"mateo": 1500,
           "alex": 900,
           "sofia": 2000,
           "Lukas": 1300,
           "Joaquim": 1200
           }

def retirar_dinero(usuario, monto):

    saldo = cuentas[usuario]

    # Retiro de dinero
    retiro_nuevo = saldo - monto
    print(f"retirando dinero...")
    time.sleep(1)
    print(f"Su saldo restante es de: {retiro_nuevo}")


def depositar_dinero(usuario, monto):

    saldo = cuentas[usuario]
    # Depositar dinero
    saldo_nuevo = saldo + monto
    print("Depositando dinero...")
    time.sleep(1)
    print(f"Su saldo total es de: {saldo_nuevo}")




usuario = input("Escriba su nombre: ")
if usuario.lower():
    if usuario in cuentas:
        time.sleep(0.1)

        depositar_retirar = input("Indique el método que desee hacer: *depositar* o *retirar*: ")
        if depositar_retirar == "depositar":

            depositar = input("Indique el monto que desee depositar: ")
            if depositar.isdigit():


                depositar = int(depositar)

                
        elif depositar_retirar == "retirar":
            retiro = input("indique el monto que desee retirar: ")
            if retiro.isdigit():
    
                usuario in cuentas

                retiro = int(retiro)

                retirar_dinero(usuario, retiro)
            else:
                print("Indique el monto que desee retirar nuevamente.")
        else:
            print("Inténtelo de nuevo.")
    else:
        print("Inténtelo denuevo y escriba uno de los siguientes nombres: mateo, alex, sofia. ")