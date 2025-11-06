import matplotlib.pyplot as plt

streams = ['Science', 'Commerce', 'Arts']
students = [50, 30, 20]

plt.pie(students, labels=streams, autopct='%1.1f%%')
plt.title('Students in Different Academic Streams')
plt.show()
