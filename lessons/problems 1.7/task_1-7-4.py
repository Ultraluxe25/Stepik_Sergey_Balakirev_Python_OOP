class Application:
    def __init__(self, name: str, blocked: bool = False):
        self.name = name
        self.blocked = blocked


class AppStore:
    _Apps: list[Application] = []

    @classmethod
    def add_application(cls, app) -> None:
        cls._Apps.append(app)
        
    @classmethod
    def remove_application(cls, app) -> None:
        cls._Apps.remove(app)

    @staticmethod
    def block_application(app) -> None:
        app.blocked = True

    @classmethod
    def total_apps(cls) -> int:
        return len(cls._Apps)
    

store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
print(store.total_apps())
print(store._Apps[0].name)
store.remove_application(app_youtube)
