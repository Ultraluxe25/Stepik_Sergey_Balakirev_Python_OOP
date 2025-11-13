class Data:
    def __init__(self, data: str, ip: int):
        self.data = data
        self.ip = ip


class Server:
    _server_number: int = 1
    
    def __init__(self):
        self.buffer: list[Data] = []
        self.ip = Server._server_number
        # IP для нового сервера
        Server._server_number += 1
        
    def send_data(self, data: Data) -> None:
        self.router.buffer.append(data)
    
    def get_data(self) -> list[Data]:
        package: list[Data] = self.buffer.copy()
        self.buffer.clear()
        
        return package
    
    def get_ip(self) -> int:
        return self.ip
        
        
class Router:
    """Класс для работы роутера с серверами и отправки данных"""
    def __init__(self, current_servers: dict[Server] = {}, buffer: list[Data] = []):
        self.current_servers = current_servers
        # Каждый буфер уже содержит адрес назначения IP
        self.buffer = buffer
    
    def link(self, server: Server) -> None:
        server.router = self
        self.current_servers[server.ip] = server
    
    def unlink(self, server: Server) -> None:
        self.current_servers.pop(server.ip)
        
    def send_data(self) -> None:
        for package in self.buffer:
            if package.ip in self.current_servers:
                self.current_servers[package.ip].buffer.append(package)
        # Очищаем буффер после отправки всех сообщений
        self.buffer.clear()


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)

sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()

msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()

print(msg_lst_from)
print(msg_lst_to)
