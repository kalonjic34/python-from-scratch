class SmartPhone():
    def __init__(self):
        self._company = "Apple"
        self._firware = 10.0
        
    def get_os_version(self):
        return self._firware
    
    def update_firmware(self):
        print("Reaching out to the server for the next version")
        self._firware += 1
        
iphone = SmartPhone()
print(iphone._company)
print(iphone._firware)

print(iphone.update_firmware())
print(iphone._firware)