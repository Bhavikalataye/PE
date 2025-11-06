import matplotlib.pyplot as plt

expenses = ['Rent', 'Food', 'Transport', 'Savings', 'Entertainment']
amount = [30, 25, 15, 20, 10]

plt.pie(amount, labels=expenses, autopct='%1.1f%%')
plt.title('Monthly Income Spending')
plt.show()
