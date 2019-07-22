import unittest
from BankAccount import BankAccount


class TestBankAccount(unittest.TestCase):

    def test_show_balance(self):
        show_1 = BankAccount("gigi").show_balance()

        self.assertEqual(show_1, "Your Balance is $2000.00")

    def test_deposit(self):
        dep_1 = BankAccount("gigi").deposit(2000)
        dep_2 = BankAccount("gigi").deposit(3000)
        dep_3 = BankAccount("gigi").deposit(-6000)

        self.assertEqual(dep_1, "The amount you want to deposit is $2000.00")
        self.assertEqual(dep_2, "The amount you want to deposit is $3000.00")
        self.assertEqual(dep_3, "The amount you entered is incorrect!")

    def test_withdraw(self):
        widraw_1 = BankAccount("gigi").withdraw(1000)
        widraw_2 = BankAccount("gigi").withdraw(3000)
        self.assertEqual(widraw_1, "The amount of $1000.00 had been withdrawed from your account! \n"
             "Your Balance is $1000.00")
        self.assertEqual(widraw_2, "The amount you entered is grater than the balance!")
        with self.assertRaises(ValueError):
            BankAccount("gigi").withdraw(-6000)






if __name__ == '__main__':
    unittest.main()
