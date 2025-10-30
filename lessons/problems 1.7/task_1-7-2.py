from string import ascii_lowercase, digits

class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits
    
    @staticmethod
    def check_card_number(number: str) -> bool:
        if type(number) is not str or len(number) != 19:
            return False
        
        for i in range(4, 19, 5):
            if number[i] != '-':
                return False
        
        _is_valid = number.replace('-', '').isdigit()
        return _is_valid
    
    @classmethod
    def check_name(cls, name: str) -> bool:
        if type(name) is not str or len(name.split()) != 2:
            return False
        
        is_valid = set(name.replace(' ', '')).issubset(set(cls.CHARS_FOR_NAME))
        return is_valid
             

is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")

print(is_number)
print(is_name)
