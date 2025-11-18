class Data:
    """Класс для хранения данных и отправки их на сервера."""
    def __init__(self, data: str, ip: int):
        self.data = data
        self.ip = ip


class Server:
    """Класс для работы сервера. Для получения данных и отправки их другим серверам через роутер."""
    _server_number: int = 1
    
    def __init__(self):
        self.buffer: list[Data] = []
        self.ip = Server._server_number
        # IP для нового сервера
        Server._server_number += 1
        
    def send_data(self, data: Data) -> None:
        # Данные можно отправить только если сервер подключен к роутеру
        if self.router:
            self.router.buffer.append(data)
    
    def get_data(self) -> list[Data]:
        package: list[Data] = self.buffer.copy()
        self.buffer.clear()
        
        return package
    
    def get_ip(self) -> int:
        return self.ip
        
        
class Router:
    """Класс для работы роутера с серверами и отправки данных."""
    def __init__(self):
        # Для каждого роутера свои собственные атрибуты
        self.current_servers: dict[Server] = {}
        # Каждый буфер уже содержит адрес назначения IP
        self.buffer: list[Data] = []
    
    def link(self, server: Server) -> None:
        # Подключаем роутер к серверу (сервер теперь имеет доступ к роутеру)
        server.router = self
        # Подключаем сервер к роутеру
        self.current_servers[server.ip] = server
    
    def unlink(self, server: Server) -> None:
        # Отключаем сервер от роутера
        self.current_servers.pop(server.ip)
        # Отключаем доступ сервера к роутеру
        server.router = None
        
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
