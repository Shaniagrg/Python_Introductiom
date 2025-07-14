class Bank:
    checking:float = 0.0
    saving:float = 0.0 
    def __inhit__ (self,c,s):
        self .checking = c
        self.saving = s

#Bank CA = new CA (10.00,20.00)

CA:Bank = Bank(10.00,20.00)