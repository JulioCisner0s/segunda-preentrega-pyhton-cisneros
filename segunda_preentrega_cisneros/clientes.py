class Clientes:
    def __init__(self, nombre, apellido, direccion, telefono, email):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.pedidos = []
        
    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)