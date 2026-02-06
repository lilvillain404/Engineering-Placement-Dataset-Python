# 📊 Анализ успеваемости инженерных студентов
[![Python](https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=python&logoColor=FFD43B)](https://www.python.org/)
[![PyCharm](https://img.shields.io/badge/PyCharm-000000?style=for-the-badge&logo=pycharm&logoColor=white)](https://www.jetbrains.com/pycharm/)

**Цель проекта:** 
- Потренироваться в работе с библиотеками Pandas, Matplotlib и Seaborn,
- Выполнить первичный анализ данных,
- Научиться строить простые, но информативные визуализации,
- Увидеть, как Python помогает отвечать на вопросы о данных.

**Вопросы, на которые я искала ответы**
- Какой средний балл у студентов?
-  Какая специальность больше всего учится?
-  Где самая высокая посещаемость?
-  Какие специальности делают больше проектов?

## 🗂️ Источник данных
**Датасет:** [Indian Engineering College Placement Dataset](https://www.kaggle.com/datasets/vishardmehta/indian-engineering-college-placement-dataset/data) с Kaggle.


## 🛠️ Стек технологий
1. Pandas - для обработки и анализа данных
2. Matplotlib - для базовой визуализации
3. Seaborn - для улучшения стиля графиков

## 1. Загрузила данные и провела базовый анализ
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Загрузка данных
df = pd.read_csv('data/indian_engineering_student_placement.csv')

# 2. Базовый анализ
print("БАЗОВЫЙ АНАЛИЗ")
print(f"Всего студентов: {len(df)}")

# 3. Средний CGPA общий
average_cgpa = df['cgpa'].mean()
print(f"\n1. СРЕДНИЙ CGPA:")
print(f"   Общий средний CGPA: {average_cgpa:.2f}")
...
```

## 2. Построила визуализацию для некоторых параметров
```python
# График 1: Распределение по специальностям
plt.subplot(2, 3, 1)
branch_counts = df['branch'].value_counts()
bars = plt.bar(branch_counts.index, branch_counts.values, color='skyblue')
plt.title('Количество студентов по специальностям', fontsize=12, fontweight='bold')
plt.xlabel('Специальность', fontweight='bold')
plt.ylabel('Количество студентов', fontweight='bold')
plt.xticks(rotation=45)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2., height,
             f'{int(height)}', ha='center', va='bottom')
...
```
С полным кодом Вы можете ознакомиться в репозитории.

## 📊 Результаты анализа в Python
![Просмотр](https://github.com/lilvillain404/Engineering-Placement-Dataset-Python/blob/main/Result/Figure_1.png)

## 3. Вывела таблицу "топ-10 студентов"
Создала таблицу топ-10 студентов с самыми высокими CGPA с отображением их основных характеристик.
| ID  | Пол | Направление | CGPA | Часы обучения | Посещаемость(%)|
|-----|-----|---------------|------|----------------|------------------|
| 105 | Ж   | ECE           | 10.0| 5.9            | 75.7             |
| 124 | М   | ECE           | 10.0| 4.0            | 74.5             |
| 133 | М   | CSE           | 10.0| 4.3            | 68.4             |
| 157 | Ж   | CSE           | 10.0| 2.6            | 63.6             |
| 190 | М   | CSE           | 10.0| 3.0            | 67.9             |
| ... | ... | ...           | ... | ...            | ...             |

## 📊 Вопросы, на которые я искала ответы

**🔍 1. Какой средний балл у студентов и есть ли различия по полу?**

Средний CGPA составляет **8.28/10** – очень высокий показатель успеваемости. Между женщинами (8.29) и мужчинами (8.28) практически нет различий.
***

**⏰ 2. Какая специальность больше всего времени уделяет учебе?**
1. CSE (Computer Science) – 6115 часов – абсолютный лидер
2. ECE (Electronics & Communication) – 5572 часов
3. IT (Information Technology) – 3856 часов
***

**📅 3. Где самая высокая посещаемость занятий?**
1. ECE – 72.5% – лучшая регулярность посещений
2. ME и IT – по 72.0% – одинаково хорошие показатели
3. CSE – 71.8%
***

**🛠️ 4. Какие специальности делают больше всего проектов?**
1. CSE – 9089 проектов (32.9% от общего числа) – каждый третий проект в институте
2. ECE – 6726 проектов (24.3%)
3. IT – 5758 проектов (20.8%)


<p align="center">
  <b>Спасибо, что посмотрели мой проект на Python! 🐍</b><br>
  Буду рада вашим отзывам и предложениям.
</p>
