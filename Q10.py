import matplotlib.pyplot as plt

platforms = ['Instagram', 'YouTube', 'Facebook', 'Twitter', 'Snapchat']
time_spent = [35, 30, 20, 10, 5]

plt.pie(time_spent, labels=platforms, autopct='%1.1f%%')
plt.title('Time Spent on Social Media Platforms')
plt.show()
