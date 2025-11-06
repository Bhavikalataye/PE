import matplotlib.pyplot as plt

products = ['Product A', 'Product B', 'Product C', 'Product D']
sales = [40, 25, 20, 15]

plt.pie(sales, labels=products, autopct='%1.1f%%')
plt.title('Product Contribution to Total Sales')
plt.show()
