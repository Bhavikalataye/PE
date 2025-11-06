import matplotlib.pyplot as plt

roles = ['Manager', 'Engineer', 'HR', 'Sales', 'Support']
count = [10, 40, 5, 25, 20]

plt.pie(count, labels=roles, autopct='%1.1f%%')
plt.title('Roles in a Company')
plt.show()
