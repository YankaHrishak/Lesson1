class contactTelegram():
    user = ""
    phone = ""
class contactViber():
    name = ""
    phone = ""
class contactList(contactTelegram,contactViber):
    name = ""
    phone = ""
    category = ""
    def __int__(self,n,p,c):
        self.name = n
        self.phone = p
        self.category = c
        self.user = contactTelegram.user
    def __init__(self,c):
        self.name = contactViber.name
        self.phone = contactViber.phone
        self.category = c
        self.user = contactTelegram.user
