# Strategy Interface

class PaymentMethod:

    def pay(self, amount):
        pass


# Different Payment Methods

class CreditCard(PaymentMethod):

    def pay(self, amount):
        print("Paid ₹", amount, "using Credit Card")


class UPI(PaymentMethod):

    def pay(self, amount):
        print("Paid ₹", amount, "using UPI")


class Cash(PaymentMethod):

    def pay(self, amount):
        print("Paid ₹", amount, "using Cash")


# Payment Processor

class PaymentProcessor:

    def __init__(self):
        self.method = None

    def set_payment_method(self, method):
        self.method = method

    def make_payment(self, amount):

        if self.method is None:
            print("Please select a payment method.")
        else:
            self.method.pay(amount)


# Main Program

payment = PaymentProcessor()

print("Select Payment Method")
print("1. Credit Card")
print("2. UPI")
print("3. Cash")

choice = int(input("Enter your choice: "))
amount = float(input("Enter amount: "))

if choice == 1:
    payment.set_payment_method(CreditCard())

elif choice == 2:
    payment.set_payment_method(UPI())

elif choice == 3:
    payment.set_payment_method(Cash())

else:
    print("Invalid Choice")

if choice >= 1 and choice <= 3:
    payment.make_payment(amount)