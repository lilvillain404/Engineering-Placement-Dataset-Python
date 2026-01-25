import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Загрузка данных
df = pd.read_csv('data/indian_engineering_student_placement.csv')

# 2. Базовый анализ
print("\n" + "=" * 50)
print("БАЗОВЫЙ АНАЛИЗ")
print("=" * 50)
print(f"Всего студентов: {len(df)}")

# 3. Средний CGPA общий
average_cgpa = df['cgpa'].mean()
print(f"\n1. СРЕДНИЙ CGPA:")
print(f"   Общий средний CGPA: {average_cgpa:.2f}")

# 4. Средний CGPA по мужчинам и женщинам
cgpa_by_gender = df.groupby('gender')['cgpa'].mean()
print(f"   Средний CGPA мужчин: {cgpa_by_gender.get('Male', 0):.2f}")
print(f"   Средний CGPA женщин: {cgpa_by_gender.get('Female', 0):.2f}")

# 5. Количество учебных часов по специальностям
print(f"\n2. УЧЕБНЫЕ ЧАСЫ ПО СПЕЦИАЛЬНОСТЯМ (ОБЩЕЕ КОЛИЧЕСТВО):")
study_hours_total_by_branch = df.groupby('branch')['study_hours_per_day'].sum().sort_values(ascending=False)
for branch, total_hours in study_hours_total_by_branch.items():
    print(f"   {branch}: {total_hours:.0f} часов")

# 6. Процент посещаемости по специальностям
print(f"\n3. ПОСЕЩАЕМОСТЬ ПО СПЕЦИАЛЬНОСТЯМ:")
attendance_by_branch = df.groupby('branch')['attendance_percentage'].mean().sort_values(ascending=False)
for branch, attendance in attendance_by_branch.items():
    print(f"   {branch}: {attendance:.1f}%")

# 7. Количество проектов по специальностям
print(f"\n5. ПРОЕКТЫ ПО СПЕЦИАЛЬНОСТЯМ:")
projects_by_branch = df.groupby('branch')['projects_completed'].sum().sort_values(ascending=False)
total_projects = projects_by_branch.sum()
for branch, projects in projects_by_branch.items():
    percentage = (projects / total_projects) * 100
    print(f"   {branch}: {projects} проектов ({percentage:.1f}% от общего числа)")

# 8. Визуализация - Первая страница графиков
plt.figure(figsize=(16, 10))

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

# График 2: Распределение CGPA
plt.subplot(2, 3, 2)
plt.hist(df['cgpa'], bins=20, color='lightgreen', edgecolor='black', alpha=0.7)
plt.title('Распределение CGPA студентов', fontsize=12, fontweight='bold')
plt.xlabel('CGPA', fontweight='bold')
plt.ylabel('Количество студентов', fontweight='bold')
plt.axvline(average_cgpa, color='red', linestyle='--', linewidth=2, label=f'Среднее: {average_cgpa:.2f}')
plt.legend()

# График 3: CGPA по полу
plt.subplot(2, 3, 3)
genders = ['Male', 'Female']
cgpa_values = [cgpa_by_gender.get('Male', 0), cgpa_by_gender.get('Female', 0)]
colors = ['blue', 'pink']
bars = plt.bar(genders, cgpa_values, color=colors)
plt.title('Средний CGPA по полу', fontsize=12, fontweight='bold')
plt.xlabel('Пол', fontweight='bold')
plt.ylabel('Средний CGPA', fontweight='bold')
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2., height,
             f'{height:.2f}', ha='center', va='bottom')

# График 4: Учебные часы по специальностям
plt.subplot(2, 3, 4)
branches = study_hours_total_by_branch.index
bars = plt.bar(branches, study_hours_total_by_branch.values, color='orange', alpha=0.7)
plt.title('Общее количество учебных часов по специальностям', fontsize=12, fontweight='bold')
plt.xlabel('Специальность', fontweight='bold')
plt.ylabel('Всего часов учебы', fontweight='bold')
plt.xticks(rotation=45)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2., height,
             f'{int(height):,}'.replace(',', ' '), ha='center', va='bottom')

# График 5: Посещаемость по специальностям
plt.subplot(2, 3, 5)
branches = attendance_by_branch.index
bars = plt.bar(branches, attendance_by_branch.values, color='purple', alpha=0.7)
plt.title('Средняя посещаемость по специальностям', fontsize=12, fontweight='bold')
plt.xlabel('Специальность', fontweight='bold')
plt.ylabel('Посещаемость (%)', fontweight='bold')
plt.xticks(rotation=45)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2., height,
             f'{height:.1f}%', ha='center', va='bottom')

# График 6: Проекты по специальностям
plt.subplot(2, 3, 6)
projects_by_branch_sorted = projects_by_branch.sort_values(ascending=False)
bars = plt.bar(projects_by_branch_sorted.index, projects_by_branch_sorted.values,
               color='teal', alpha=0.7)
plt.title('Завершенные проекты по специальностям', fontsize=12, fontweight='bold')
plt.xlabel('Специальность', fontweight='bold')
plt.ylabel('Количество проектов', fontweight='bold')
plt.xticks(rotation=45)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2., height,
             f'{int(height)}', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()

# 9. Вывод таблицы с топ-10 студентов
print("\n" + "=" * 70)
print("ТАБЛИЦА: ТОП-10 СТУДЕНТОВ ПО CGPA")
print("=" * 70)
print(f"{'ID':<8} {'Пол':<6} {'Специальность':<12} {'CGPA':<8} {'Часы учебы':<12} {'Посещаемость':<12}")
print("-" * 70)

top_10_table = df.nlargest(10, 'cgpa')[['Student_ID', 'gender', 'branch', 'cgpa',
                                        'study_hours_per_day', 'attendance_percentage']]

for _, row in top_10_table.iterrows():
    gender_ru = "М" if row['gender'] == 'Male' else "Ж"
    print(f"{row['Student_ID']:<8} {gender_ru:<6} {row['branch']:<12} {row['cgpa']:<8.2f} "
          f"{row['study_hours_per_day']:<12.1f} {row['attendance_percentage']:<12.1f}")
