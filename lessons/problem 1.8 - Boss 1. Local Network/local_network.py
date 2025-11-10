class Data:
    def __init__(self, data: str, ip: int):
        self.data = data
        self.ip = ip


class Server:
    _server_number: int = 1
    
    def __init__(self, buffer: list[Data] = []):
        self.buffer = buffer
        self.ip = Server._server_number
        # IP для нового сервера
        Server._server_number += 1
        
    def send_data(self, data: Data) -> None:
        self.buffer.append(data)
    
    def get_data(self) -> list[Data]:
        package: list[Data] = self.buffer.copy()
        self.buffer.clear()
        
        return package
    
    def get_ip(self) -> int:
        return self.ip
        
        
class Router:
    """Класс для работы роутера с серверами и отправки данных"""
    def __init__(self, servers: dict[Server] = {}, buffer: dict[Data] = {}):
        # Серверы подключенные к роутеру
        self.servers = servers
        self.buffer = buffer 
    
    def link(self, server: Server) -> None:
        self.servers[server.ip] = server
        self.buffer[server.ip] = server.buffer
    
    def unlink(self, server: Server) -> None:
        self.servers.pop(server.ip)
        
    def send_data(self) -> None:
        for ip, server in self.servers.items():
            server.buffer



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
