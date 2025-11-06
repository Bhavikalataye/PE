import matplotlib.pyplot as plt

brands = ['Samsung', 'Apple', 'Xiaomi', 'Oppo', 'Vivo']
market_share = [30, 25, 20, 15, 10]

plt.pie(market_share, labels=brands, autopct='%1.1f%%')
plt.title('Market Share of Mobile Phone Brands')
plt.show()
