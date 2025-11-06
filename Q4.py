import matplotlib.pyplot as plt

continents = ['Asia', 'Europe', 'North America', 'South America', 'Africa', 'Oceania']
users = [50, 20, 10, 8, 10, 2]

plt.pie(users, labels=continents, autopct='%1.1f%%')
plt.title('Global Internet Users by Continent')
plt.show()
