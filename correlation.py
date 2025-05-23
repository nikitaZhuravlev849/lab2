#Часть 1
import pandas as pd
brainFrame = pd.read_csv("brainsize.txt", delimiter='\t')


brainFrame.head()


brainFrame.head(10)


brainFrame.tail(8)

#Часть 2

brainFrame.describe()


import numpy as np
import matplotlib.pyplot as plt


menDf = brainFrame[brainFrame['Gender'] == 'Male']
womenDf = brainFrame[brainFrame['Gender'] == 'Female']

#Часть 3

womenMeanSmarts = womenDf[["PIQ", "FSIQ", "VIQ"]].mean(axis=1)
plt.scatter(womenMeanSmarts, womenDf["MRI_Count"])
plt.show()
%matplotlib inline


# Удаляем столбец 'Gender' и другие нечисловые столбцы (если есть)
numeric_brainFrame = brainFrame.drop(columns=['Gender'])


# Теперь вычисляем корреляцию
numeric_brainFrame.corr(method='pearson')

#Часть 4

womenDf = brainFrame[brainFrame['Gender'] == 'Female'].drop(columns=['Gender'])
womenDf.corr(method='pearson')


menDf = brainFrame[brainFrame['Gender'] == 'Male'].drop(columns=['Gender'])
menDf.corr(method='pearson')


mcorr = menDf.corr()
sns.heatmap(mcorr)
plt.show()


#Часть 3: Вопросы по корреляции
#1. Почему диагональ в таблице корреляции заполнена значениями 1?
#Диагональ таблицы корреляции всегда состоит из единиц, потому что каждая переменная идеально коррелирует сама с собой. Коэффициент корреляции Пирсона между одной и той же переменной равен 1 по определению.

#2. Почему значения в таблице корреляции зеркальны относительно диагонали?
#Корреляция между переменными симметрична,
#поэтому таблица корреляции симметрична относительно главной диагонали.

#3. Как вычислить корреляцию для мужского и женского подмножеств данных?
#Для этого используется метод .corr():

#Часть 4: Вопросы по визуализации и анализу
#1. Что означает корреляция, близкая к нулю?
#Корреляция около нуля означает, что между переменными нет линейной зависимости. Это не исключает возможной нелинейной связи, но в рамках корреляции Пирсона такая зависимость не учитывается.

#2.Зачем нужно разделение данных по полу?
#Разделение по полу позволяет исключить влияние половых различий на анализ. Например, мужчины и женщины могут иметь разное распределение по размеру мозга, весу или когнитивным показателям, что может исказить общую корреляцию.

#3.Какие переменные имеют сильную корреляцию с MRI_Count (размер мозга)? Ожидаемо ли это?
#Сильнее всего с MRI_Count, скорее всего, коррелируют физические параметры (например, рост или вес), так как размер мозга частично зависит от общего размера тела. Корреляция с когнитивными показателями (FSIQ, VIQ, PIQ) обычно слабее, поскольку интеллект зависит не только от объема мозга, но и от других факторов (нейронных связей, плотности серого вещества и т. д.).