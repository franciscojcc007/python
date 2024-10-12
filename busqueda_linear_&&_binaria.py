# def busqueda_linear(lista, objetivo):
#     for i in range(len(lista)):
#         if lista[i] == objetivo: 
#             return i
    
#     return -1  

# # Lista de ejemplo
# ls = [1, 2, 2, 2, 3, 3, 4, 5, 6, 6, 6, 7]
# print(busqueda_linear(ls, 3))  

def busqueda_linear(lista, objetivo):
  for i,elem in enumerate(lista):
    if  elem == objetivo:
      return i
    
  return -1
# Ejemplo de uso
ls = [1,2,2,2,3,3,4,5,6,6,6,7]
print(busqueda_linear(ls, 3)) 


def busqueda_binario(lista, objetivo):
  izquierda = 0
  derecha = len(lista) - 1
  while izquierda <= derecha:
    medio = (izquierda + derecha) // 2
    if lista[medio] == objetivo:
      return medio
    elif lista[medio] < objetivo:
      izquierda = medio + 1
    else:
      derecha = medio - 1
      
    
  return -1
print(busqueda_binario(ls, 2))