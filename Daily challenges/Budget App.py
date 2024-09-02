class Category:
    def __init__(self, cat):
        self.cat = cat
        self.ledger = []
        self.amount = 0

    def __str__(self):
        final = [self.cat.center(30, "*"), ]
        for item in self.ledger:
            x = item["description"][:23].ljust(23, " ")
            y = str(item["amount"])
            y += ".00" if "." not in y else ""
            final.append(x + y.rjust(7, " "))

        final.append(f"Total: {self.amount}")
        return "\n".join(final)

    def check_funds(self, amount):
        return self.amount >= amount

    def deposit(self, amount, description=""):
        self.amount += amount
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.amount -= amount
            self.ledger.append({
                "amount": -(amount),
                "description": description
            })
            return True
        return False

    def get_balance(self):
        return self.amount

    def transfer(self, amount, budget):
        if self.check_funds(amount):
            self.amount -= amount
            self.ledger.append({
                "amount": -(amount),
                "description": f"Transfer to {budget.cat}"
            })
            budget.deposit(amount, f"Transfer from {self.cat}")
            return True
        return False


def create_spend_chart(*categories) -> str:
    final = ["Percentage spent by category", ]
    for i in range(10, -1, -1):
        final.append(f"{i * 10}|".rjust(4, " "))

    number = 0
    final2 = []
    initial = " " * 4
    for item in categories:
        number += 1
        total = 0
        total2 = 0
        for thing in item.ledger:
            if thing["amount"] < 0:
                total += abs(thing["amount"])
            else:
                total2 += thing["amount"]
        percent = round((total / total2) * 100)
        if percent < 5:
            percent = 0
        elif percent < 10:
            percent = 10
        else:
            if percent % 10 < 5:
                percent = (percent // 10) * 10
            else:
                percent = ((percent // 10) + 1) * 10
        for i in range(11, 0, -1):
            if percent >= (11 - i) * 10:
                final[i] += " o "
            else:
                break

        for i in range(len(item.cat)):
            try:
                final2[i] += f" {item.cat[i]} "
            except:
                final2.append(initial + f" {item.cat[i]} ")
        initial += "   "

    final.append((" " * 4) + ("---" * number) + "-")
    final += final2

    return "\n".join(final)