#Часть 1
import pandas as pd

# Чтение данных из файла 'titanic.csv'
# Используйте метод pd.read_csv()
df = pd.read_csv('titanic.csv')

#Часть 2

# Вывод первых 5 строк данных
# Используйте метод .head()
df.head()

df.info()

# Проверка на наличие NaN в DataFrame
# Используйте метод .isna()
df.isna()

# Заполнение NaN определенным значением (например, нулем)
# Используйте метод .fillna()
df_filled = df.fillna(0)

# Удаление строк, содержащих NaN
# Используйте метод .dropna()
df_dropped = df.dropna()

# Выбор столбца по метке
# Используйте синтаксис DataFrame['название_столбца']
age_column = df['Age']

#Часть 3

# Выбор нескольких столбцов
# Используйте синтаксис DataFrame[['столбец_1', 'столбец_2']]
selected_columns = df[['Age', 'Sex']]


# Выбор строк по индексу
# Используйте метод .loc[]
rows_by_index = df.loc[0:4]


# Выбор строк и столбцов по условию
# Используя логические операции, выберите мужчин старше 30
male_over_30 = df[(df['Sex'] == 'male') & (df['Age'] > 30)]

# Сортировка данных по столбцу 'столбец_1' по возрастанию
# Используйте метод .sort_values()
df_sorted = df.sort_values('Fare', ascending=False)

# Найдите долю выживших среди всех PClass
# Используйте метод .groupby()
average_age_by_class = df.groupby('Pclass')['Age'].mean()

#Часть 4

# 1. Прочитать данные
df_practice = pd.read_csv('titanic.csv')


# 2. Проверить и заполнить пропущенные значения нулями
df_practice = df_practice.fillna(0)


# 3. Вывести первые 10 строк
df_practice.head(10)


# 4. Выбрать строки, где Age > 30
age_over_30 = df_practice[df_practice['Age'] > 30]


# 5. Отсортировать по 'Fare' в порядке убывания
df_sorted_fare = df_practice.sort_values('Fare', ascending=False)


# 6. Группировка по 'Pclass' и средний возраст
average_age_pclass = df_practice.groupby('Pclass')['Age'].mean()
