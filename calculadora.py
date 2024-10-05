print("*****************************\n")
print("<<<<<<< Calculadora >>>>>>>>>")
print("_____________________________\n")
n1 = float(input("Dime tu primer número: "))
n2 = float(input("Dime tu segundo número: "))

opcion = 0
while True:
      print("""
      Dime, ¿qué quieres hacer?\n
      1) Sumar los dos números
      2) Restar los dos números
      3) Multiplicar los dos números
      4) divide los dos numero
      5) Cambiar los números elegidos
      6) Apagar calculadora
      """)
      opcion = int(input("Elige una opción a realizar: "))     

      if opcion == 1:
            print(" ")
            print("RESULTADO: La suma de",n1,"+",n2,"es igual a",n1+n2)
      elif opcion == 2:
            print(" ")
            print("RESULTADO: La resta de",n1,"-",n2,"es igual a",n1-n2)
      elif opcion == 3:
            print(" ")
            print("RESULTADO: El producto de",n1,"*",n2,"es igual a",n1*n2)
      elif opcion == 4:
            print(" ")
            print("RESULTADO: El producto de",n1,"/",n2,"es igual a",n1/n2)
      elif opcion == 5:
            n1 = float(input("Dime tu primer número: "))
            n2 = float(input("Dime tu segundo número: "))
      elif opcion == 6:
            break
      else:
            print("Opción incorrecta")
      
def suma(n1,n2):
      return n1+n2;

def resta(n1,n2):
      return n1-n2;  

def Multiplicar(n1,n2):
      return n1*n2;

def dividir(n1,n2):
      return n1/n2;   