from segunda_preentrega_cisneros.clientes import Clientes
from segunda_preentrega_cisneros.pedidos import Pedidos

def crear_cliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    direccion = input("Ingrese su direccion: ")
    telefono = input("Ingrese su telefono: ")
    email = input("Ingrese su email: ")
    return Clientes(nombre, apellido, direccion, telefono, email)

def crear_pedido(cliente):
    no_pedido = Pedidos.count + 1
    fecha_del_pedido = input("Ingrese la fecha del pedido (dd/mm/aaaa): ")
    productos = input("Ingrese los productos del pedido (separados por comas): ").split(",")
    return Pedidos(no_pedido, fecha_del_pedido, cliente, productos)

def agregar_pedido(cliente, pedido):
    cliente.agregar_pedido(pedido)
    print("Pedido creado con exito")

def listar_clientes(clientes):
    for cliente in clientes.values():
        print(cliente.nombre, cliente.apellido, cliente.direccion, cliente.telefono, cliente.email)
        
def listar_pedidos(clientes):
    for cliente_id, cliente in clientes.items():
        print(f"\nPedidos de {cliente.nombre}: ")
        for pedido in cliente.pedidos:
            print(pedido)
            
def main():
    clientes = {}
    while True:
        print("\n1.- Crear cliente\n")
        print("\n2.- Crear pedido\n")
        print("\n3.- Listar clientes\n")
        print("\n4.- Listar pedidos\n")
        print("\n5.- Salir\n")
        opcion = int(input("Ingrese su opcion: "))
        if opcion == 1 :
            cliente = crear_cliente()
            clientes[cliente.nombre] = cliente
            print("Cliente creado con exito")
        elif opcion == 2:
            cliente = clientes[input("Ingrese su nombre: ")]
            pedido = crear_pedido(cliente)
            cliente.agregar_pedido(pedido)
            print("Pedido creado con exito")
        elif opcion == 3 :
            listar_clientes(clientes)
        elif opcion == 4 :
            listar_pedidos(clientes)
        elif opcion == 5 :
            break
        else:
            print("Opcion invalida")
            
if __name__ == "__main__":
    main()