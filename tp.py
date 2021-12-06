import os
import random
import pyrecord

def elegir(ultimo):
    print()
    print(" "*22,end=" ")
    opc=int(input(" Elija una opción: "))
    while((opc>ultimo) or (opc<0)):
        print(" "*20,"Lo siento, la Opción es inválida")
        print(" "*22,end=" ")
        opc=int(input(" Elija una opción: "))
    return opc


def menu():
    print(' '*20, '1- Para consultar el Saldo de su cuenta.')
    return elegir(5)







def operaciones():

    a1 = open('operaciones.txt', 'r')
    linea = a1.readline().strip()
    s = linea.split(',')

    pass





def cargar_cajeros(Rcajeros, veccajeros):

    a1 = open('cajeros.txt', 'r')
    linea = a1.readline().strip()
    s = linea.split(',')
    while linea != "":
        for i in range(len(veccajeros)):
                veccajeros[i] = Rcajeros()
                veccajeros[i].numero_cajero = s[0]
                veccajeros[i].ubicacion = s[1]
                veccajeros[i].cant_mov = s[2]
                linea = a1.readline().strip()
                s = linea.split(",")
                #print(veccajeros[i].numero_cajero)
    a1.close()
    return veccajeros[i].numero_cajero , veccajeros[i].ubicacion, veccajeros[i].cant_mov

def cargar_Rcuentas(Rcuentas, veccuentas):

    a1 = open('cuentas.txt', 'r')
    linea = a1.readline().strip()
    
    s = linea.split(',')
    while linea != "":
        for i in range(len(veccuentas)):
        

            veccuentas[i] = Rcuentas()
            veccuentas[i].numero_cuenta = int(s[0])
            veccuentas[i].apellido = str(s[1])
            veccuentas[i].nombre = str(s[2])
            veccuentas[i].DNI = int(s[3])
            veccuentas[i].tipo_cuenta = int(s[4])
            veccuentas[i].saldo= float(s[5])
            veccuentas[i].activa = bool(s[6])
            #print(f'{veccuentas[i].numero_cuenta},{veccuentas[i].apellido},{veccuentas[i].nombre},{veccuentas[i].DNI},{veccuentas[i].tipo_cuenta},{veccuentas[i].saldo},{veccuentas[i].activa}')

            linea = a1.readline().strip()
            s = linea.split(',')
    a1.close()

    return veccuentas[i].numero_cuenta, veccuentas[i].apellido, veccuentas[i].nombre,veccuentas[i].DNI,veccuentas[i].tipo_cuenta,veccuentas[i].saldo,veccuentas[i].activa
    #for i in range(len(veccuentas)):
       
       #print(f'{veccuentas[i].numero_cuenta},{veccuentas[i].apellido},{veccuentas[i].nombre},{veccuentas[i].DNI},{veccuentas[i].tipo_cuenta},{veccuentas[i].saldo},{veccuentas[i].activa}')

def consulta_cuentas(Rcuentas, veccuentas):
    numero = int(input('ingrese su numero de cuenta: '))
    x = numero -1000
    print('Su saldo acutal es $',veccuentas[x].saldo)






Rcajeros = pyrecord.Record.create_type('Rcajeros','numero_cajero', 'ubicacion','cant_mov',numero_cajero = 0, ubicacion = "", cant_mov = 0)
veccajeros = [Rcajeros] * 120
Rcuentas = pyrecord.Record.create_type('Rcuentas','numero_cuenta','apellido','nombre','DNI','tipo_cuenta','saldo','activa',numero_cuenta = 0,apellido = "",nombre = "", DNI = 0 , tipo_cuenta = 0,saldo = 0.0,activa = bool)
veccuentas = [Rcuentas] *600






#cargar_Rcuentas(Rcuentas, veccuentas)
#consulta_cuentas(Rcuentas, veccuentas)
