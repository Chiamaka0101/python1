class BankAccount():
  def __init__(self, owner, balance):
    self.owner = owner
    self.__balance = balance #encapsulation

  def deposit(self, amount):
    if amount > 0:
      self.__balance += amount 
    
  def get_balance(self):
    return self.__balance

  