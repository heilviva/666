import pandas as pd
import matplotlib.pyplot as plt

# Чтение данных из CSV файла
data = pd.read_csv('car_sales.csv')

# Линейный график
plt.plot(data['x'], data['y1'], label='График 1')
plt.plot(data['x'], data['y2'], label='График 2')
plt.plot(data['x'], data['y3'], label='График 3')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Линейный график')
plt.legend()
plt.savefig('line_plot.png')
plt.show()

# Столбчатая диаграмма
plt.bar(data['x'], data['y1'], label='Диаграмма 1')
plt.bar(data['x'], data['y2'], label='Диаграмма 2')
plt.bar(data['x'], data['y3'], label='Диаграмма 3')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Столбчатая диаграмма')
plt.legend()
plt.savefig('bar_chart.png')
plt.show()

# Круговая диаграмма
plt.pie(data['y1'], labels=data['x'], autopct='%1.1f%%')
plt.title('Круговая диаграмма 1')
plt.savefig('pie_chart1.png')
plt.show()

plt.pie(data['y2'], labels=data['x'], autopct='%1.1f%%')
plt.title('Круговая диаграмма 2')
plt.savefig('pie_chart2.png')
plt.show()

# Диаграмма рассеяния
plt.scatter(data['x'], data['y1'], label='Диаграмма 1')
plt.scatter(data['x'], data['y2'], label='Диаграмма 2')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Диаграмма рассеяния')
plt.legend()
plt.savefig('scatter_plot.png')
plt.show()

# Гистограмма
plt.hist(data['y1'], bins=10, label='Гистограмма 1')
plt.hist(data['y2'], bins=10, label='Гистограмма 2')
plt.hist(data['y3'], bins=10, label='Гистограмма 3')
plt.xlabel('Y')
plt.ylabel('Частота')
plt.title('Гистограмма')
plt.legend()
plt.savefig('histogram.png')
plt.show()

