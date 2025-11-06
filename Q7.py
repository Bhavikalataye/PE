import matplotlib.pyplot as plt

products = ['Laptop', 'Mobile', 'Tablet', 'Headphones', 'Smartwatch']
sales = [35, 30, 15, 10, 10]

plt.pie(sales, labels=products, autopct='%1.1f%%')
plt.title('Different Products Contribution to Total Sales')
plt.show()
