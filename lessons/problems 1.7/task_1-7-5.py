# здесь объявляйте класс Message
class Message:
    def __init__(self, text: str, fl_like: bool = False):
        self.text = text
        self.fl_like = fl_like


class Viber:
    msgs = {}

    # здесь продолжайте класс Viber
    @classmethod
    def add_message(cls, msg: Message) -> None:
        cls.msgs[id(msg)] = msg

    @classmethod
    def remove_message(cls, msg: Message) -> None:
        if id(msg) in cls.msgs:
            del cls.msgs[id(msg)]

    @staticmethod
    def set_like(msg: Message) -> None:
        msg.fl_like = not msg.fl_like

    @classmethod
    def show_last_message(cls, last_n: int) -> list[str]:
        texts = [cls.msgs[id].text for id in sorted(cls.msgs)]
        return texts[-last_n:]

    @classmethod
    def total_messages(cls) -> int:
        return len(cls.msgs)


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)

print(Viber.show_last_message(2))
print(Viber.total_messages())
