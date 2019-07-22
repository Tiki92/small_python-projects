class BankAccount:
  balance = 2000
  def __init__(self, name):
    self.name = name
    
  def __repr__(self):
    return "The Account belongs to %s, and the balace is $%.2f" % (self.name, self.balance)
  
  def show_balance(self):
    return("Your Balance is $%.2f" % (self.balance))
    
  def deposit(self, amount):
    if amount <= 0:
      return("The amount you entered is incorrect!")
    else:
      self.balance += amount
      self.show_balance()
      return("The amount you want to deposit is $%.2f" % (amount))
      
  def withdraw(self, amount):
    if amount > self.balance:
      return("The amount you entered is grater than the balance!")
    elif amount < 0:
      raise ValueError("You can't  enter a NEGATIVE value!")
    else:
      self.balance -= amount
      bal = self.show_balance()
      return("The amount of $%.2f had been withdrawed from your account! \n"
             "%s"% (amount, bal))
      
#my_account = BanckAccount("your Name")
#print(my_account)
#print(my_account.show_balance())
#print(my_account.deposit(2000))
#print(my_account.withdraw(1000))
#print(my_account)
