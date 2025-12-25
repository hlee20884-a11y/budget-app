class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23]
            amt = f"{entry['amount']:.2f}"[:7]
            items += f"{desc:<23}{amt:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    title = "Percentage spent by category\n"

    # Calculate total spent per category
    withdrawals = []
    for category in categories:
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total += abs(item["amount"])
        withdrawals.append(total)

    total_spent = sum(withdrawals)
    percentages = [int((w / total_spent) * 100) // 10 * 10 for w in withdrawals]

    # Y-axis labels
    chart = ""
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for p in percentages:
            chart += "o  " if p >= i else "   "
        chart += "\n"

    # Bottom line
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    # Category names vertically
    max_len = max(len(c.name) for c in categories)
    for i in range(max_len):
        chart += "     "
        for c in categories:
            chart += f"{c.name[i] if i < len(c.name) else ' '}  "
        if i < max_len - 1:
            chart += "\n"

    return title + chart


# Sample usage / testing
if __name__ == "__main__":
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and dessert")

    clothing = Category("Clothing")
    food.transfer(50, clothing)

    auto = Category("Auto")
    auto.deposit(200, "initial deposit")
    auto.withdraw(50, "gas")

    print(food)
    print(clothing)
    print(auto)
    print(create_spend_chart([food, clothing, auto]))