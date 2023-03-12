import array
from datetime import datetime
import string
import os

#arrays for users
emailUser = []
passWordUser = []
nombreUser = []
tipoCuentaUser = []
fechausers = []

#first user in system
nombreUser.append("Jose Jeronimo");
emailUser.append("admin@bank.com");
passWordUser.append("soyeladmin");
tipoCuentaUser.append("ADMIN");
fechausers.append("01/01/2020");

for email in emailUser:
    print(email);
for passw in passWordUser:
    print(passw);
    
#arrays for accounts
nombreCuentas = []
codigoCuentas = []
tipoCuentas = []
saldoCuentas = []
estadoCuentas = []
fechasCuentas =[]

#variables del prgrama
init_Programa = True; 
Habilitar_Menu = False;

#variables de la cuenta
taza_interes = 0;

def retorna_Usuario_Existe(user_Principal,password):
    user_Existe = False;
    for email in emailUser:
       if email == user_Principal:
          for passw in passWordUser:
             if password == passw:
                user_Existe = True;
                break;                
    return user_Existe;

def Depositar_En_Cuenta(Codigo_Cuenta, monto_Depositar):
    for codigo in codigoCuentas:
        if codigo == Codigo_Cuenta:
               if estadoCuentas[codigoCuentas.index(codigo)] == "ACTIVA":
                  saldoCuentas[codigoCuentas.index(codigo)] += monto_Depositar;
               else:
                   print("La cuenta esta desactivada");
                   monto_Depositar = (monto_Depositar * 0.20);
                   saldoCuentas[codigoCuentas.index(codigo)] += monto_Depositar;
                   estadoCuentas[codigoCuentas.index(codigo)] = "ACTIVA";
               break;     
        print("Deposito realizado con exito");
        break;
    else:
        print("El codigo no existe");

Menu = "Bienvenido al Sistema Bancario Unitec (Estructurada) \n \n" + "1- Agregar Cuenta " + "\n2- Depositar En Cuenta " + "\n3- Retirar De Cuenta" + "\n4- Registrar Intereses" + "\n5- Tranferir A Terceros" + "\n6- Desactivar Cuentas" + "\n7- Cancelar Cuentas " + "\n8- Crear Usuarios " + "\n9- Reportes " +"\n10- Cerrar Sesion " + "\n11- SALIR";

while init_Programa:
   
    user_Principal = input("Ingrese su usuario: ");
    password_default = input("Ingrese su clave: ");
    
     
    #validacion de los datos de usuario default
    if retorna_Usuario_Existe(user_Principal,password_default):
        print("\n \n -_-_- Usuario Encontrado con exito -_-_-");
        Habilitar_Menu = True;
    else:
        #validamos que el usuario ingrese correctamente los datos
         print("\n \n -_-_- Usuario no encontrado -_-_- ");
     
         acceder = True;
         while(acceder):
              user_Principal = input("Ingrese su usuario: ");
              password_default = input("Ingrese su clave: ");
              if retorna_Usuario_Existe(user_Principal,password_default):
                   print("\n \n -_-_- Usuario Encontrado con exito -_-_-");
                   Habilitar_Menu = True;
                   acceder = False;
                   break;
              else:
                  print("\n \n -_-_- Usuario no encontrado -_-_- ");
                  acceder = True;
                  Habilitar_Menu = False;
                 
     
    if (Habilitar_Menu):
      Habilitar_Menu = False;
      control_opciones = False;
  
      print(Menu);
      
    #validar que la opcion del usuario sea valida
      opcion = int(input("Ingrese su opcion: ")); 
      if opcion>11:
        print("Valor no disponible");
       
        print(Menu);
        error_dato = True;
        while(error_dato):
          opcion =int(input("Ingrese su opcion: "));
          if opcion>11:
           print("Valor no disponible");
           error_dato = True;
          
           print(Menu);
          else:
            control_opciones = True;
            error_dato = False;
      else:
          control_opciones = True;
     #fin validacion del dato de usuario
            
    if control_opciones:
        if(opcion == 1):
            print(" Bienvenido al Apartado De Agregar Cuenta");
            Nombre_Cliente = input("Ingrese el nombre del cliente: ");
            Codigo_Cliente = input("Ingrese el codigo del cliente: ");
            Fecha = datetime.now();
            if Nombre_Cliente == "-1" or Codigo_Cliente == "-1":
            
             print(Menu);
             Habilitar_Menu = True;
            else:
              Tipo_Cliente = input("Ingrese el tipo de cuenta: ");
            for codigo in codigoCuentas:
                if codigo == Codigo_Cliente:
                    print("El codigo ya existe ingrese otro");
                    Codigo_Cliente = input("Ingrese el codigo del cliente: ");
                    break;
            
            if Tipo_Cliente == "PLANILLA":
                taza_interes = 0;
            elif Tipo_Cliente == "NORMAL":
                taza_interes = 0.2;
            elif Tipo_Cliente == "VIP":
                taza_interes = 0.4;
               
            nombreCuentas.append(Nombre_Cliente);
            codigoCuentas.append(Codigo_Cliente);
            tipoCuentas.append(Tipo_Cliente);
            saldoCuentas.append(500);
            estadoCuentas.append(True);
            fechasCuentas.append(Fecha);
            
            for nombre in nombreCuentas:
                print(nombre);
            for codigo in codigoCuentas:
                print(codigo);
            for tipo in tipoCuentas:
                print(tipo);
            for saldo in saldoCuentas:
                print(saldo);
            for fechas in fechasCuentas:
                print(fechas);
            print("Cuenta Creada con exito");       
            print(Menu);
            Habilitar_Menu = True;
            
        elif(opcion == 2):
            print("Depositar En Cuenta");
            C_Cuenta = input("Ingrese el codigo de la cuenta: ");
            monto = input("Ingrese monto a depositar: ");
            Depositar_En_Cuenta(C_Cuenta,monto);
        elif(opcion == 3):
            print("Retirar De Cuenta");
        elif(opcion == 4):
            print("Registrar Intereses");
        elif(opcion == 5):
            print("Tranferir A Terceros");
        elif(opcion == 6):
            print("Desactivar Cuentas");
        elif(opcion == 7):
            print("Cancelar Cuentas");
        elif(opcion == 8):
            print("Crear Usuarios");
        elif(opcion == 9):
            print("Reportes");
        elif(opcion == 10):
            print("Cerrar Sesion");
            Habilitar_Menu = False;
            print("\n");
        elif(opcion == 11):
            print("SALIR");
            init_Programa = False;
            break;   
            
             
