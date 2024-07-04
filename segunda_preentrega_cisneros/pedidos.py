from segunda_preentrega_cisneros.clientes import Clientes

class Pedidos:
    count = 0
    
    def __init__(self, no_pedido, fecha_del_pedido, cliente, productos):
        self.no_pedido = no_pedido
        self.fecha_del_pedido = fecha_del_pedido
        self.cliente = cliente
        self.productos = productos
        Pedidos.count += 1
        
    def __str__(self):
        return f"Pedido No: {self.no_pedido}, con fecha del: {self.fecha_del_pedido}, con No de Cliente: {self.cliente.nombre}, y con Productos: {', '.join(self.productos)}"