class Money:
    def __init__(self,dollars,cents):
        self.dollars = dollars
        self.cents = cents
    
    def __add__(self,new_money):
        self.cents += new_money.cents + 100 * new_money.dollars
        self.dollars += self.cents // 100
        self.cents %= 100
    
    def __repr__(self):
        return f'${self.dollars}, {self.cents} c'

krabs = Money(5,10)
print(krabs)
krabs + Money(10,8)
print(krabs)