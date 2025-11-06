import matplotlib.pyplot as plt

departments = ['R&D', 'Marketing', 'Operations', 'HR', 'IT']
budget = [30, 25, 20, 10, 15]

plt.pie(budget, labels=departments, autopct='%1.1f%%')
plt.title('Budget Allocation by Department')
plt.show()
