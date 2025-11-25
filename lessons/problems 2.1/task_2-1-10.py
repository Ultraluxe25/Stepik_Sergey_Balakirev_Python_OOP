from string import ascii_lowercase, ascii_uppercase, digits
from random import randint

class EmailValidator:
    _email_begins: str = ascii_lowercase + ascii_uppercase + digits + '_.'

    def __new__(cls, *args, **kwargs ):
        return None
    
    @classmethod
    def get_random_email(cls) -> str:
        # All symbols for local-part of emails
        _local_part = ''
        n = len(cls._email_begins)
        
        for _ in range(randint(0, 64)):
            _local_part += cls._email_begins[randint(0, n - 1)]
            
        return _local_part + '@gmail.com'
    
    @staticmethod
    def __is_email_str(email: str) -> bool:
        return isinstance(email, str)
    
    @classmethod
    def check_email(cls, email) -> bool:        
        if not cls.__is_email_str(email):
            return False
        
        if not set(email) < set(cls._email_begins + '@'):
            return False
        
        # Must be two parts separeted my at-sign
        _email_parts = email.split('@')
        if len(_email_parts) != 2:
            return False
        
        if len(_email_parts[0]) > 100 or len(_email_parts[1]) > 50:
            return False
        
        if '.' not in _email_parts[1]:
            return False
        
        if '..' in email:
            return False

        # Email is correct
        return True
    