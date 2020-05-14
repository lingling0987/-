#coding:gbk
"""
利用决策树算法进行分类
作者：徐玲玲
日期：2020.5.14
"""
import pandas as pd           # 调入需要用的库
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sb
#%matplotlib inline
# 调入数据
df = pd.read_csv('frenchwine.csv')
df.columns = ['alcohol', 'malic_acid', 'ash', 'alcalinity ash', 'magnesium', 'species']
# 查看前5条数据
df.head()
print(df.head()) 
# 查看数据描述性统计信息
df.describe()
print(df.describe())

def scatter_plot_by_category(feat, x, y): #数据的可视化 
    alpha = 0.5
    gs = df.groupby(feat)
    cs = cm.rainbow(np.linspace(0, 1, len(gs)))
    for g, c in zip(gs, cs):
        plt.scatter(g[1][x], g[1][y], color=c, alpha=alpha)

plt.figure(figsize=(20,5))
plt.subplot(131)
scatter_plot_by_category('species', 'alcohol', 'malic_acid')
plt.xlabel('alcohol')
plt.ylabel('malic_acid')
plt.title('species')
plt.show()

plt.figure(figsize=(20, 10)) #利用seaborn库绘制三种葡萄不同参数图
for column_index, column in enumerate(df.columns):
    if column == 'species':
        continue
    plt.subplot(2, 3, column_index + 1)
    sb.violinplot(x='species', y=column, data=df)
plt.show()

# 首先对数据进行切分，即划分出训练集和测试集
from sklearn.model_selection import train_test_split #调入sklearn库中交叉检验，划分训练集和测试集
all_inputs = df[['alcohol', 'malic_acid',
                             'ash', 'alcalinity ash', 'magnesium']].values
all_species = df['species'].values

(X_train,
 X_test,
 Y_train,
 Y_test) = train_test_split(all_inputs, all_species, train_size=0.8, random_state=1)#80%的数据选为训练集


# 使用决策树算法进行训练
from sklearn.tree import DecisionTreeClassifier #调入sklearn库中的DecisionTreeClassifier来构建决策树
# 定义一个决策树对象
decision_tree_classifier = DecisionTreeClassifier()
# 训练模型
model = decision_tree_classifier.fit(X_train, Y_train)
# 输出模型的准确度
print(decision_tree_classifier.score(X_test, Y_test)) 

#from sklearn import datasets
#X_test,Y_test=datasets.make_regression

# 使用训练的模型进行预测，为了方便，
test1=[[13.52,3.17,2.72,23.5,97],
[12.42,2.55,2.27,22,90],
[13.76,1.53,2.7,19.5,132]] #输入测试的数据
print(test1[0:3])#利用3个数据进行测试，即取3个数据作为模型的输入端
model.predict(test1[0:3])
predict_result=[]
for i in model.predict(test1[0:3]):
	if i=='Sauvignon':
		i='赤霞珠'
		predict_result.append(i)
	elif i=='Syrah':
		i='西拉'
		predict_result.append(i)
	elif i=='Zinfandel':
		i='仙粉黛'
		predict_result.append(i)
print(predict_result)#输出测试的结果，即输出模型预测的结果

 
