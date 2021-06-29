import pandas as pd #Pandas para usar dataframes
import matplotlib.pyplot as plt #Para graficar
import matplotlib.cm as cm #Para graficar el silhouette
import seaborn as sns #Para graficar
import numpy as np #Para realizar operaciones númericas con matrices y arrays
from sklearn import datasets #sklearn es LA biblioteca de machine learning de python
from sklearn.cluster import KMeans, DBSCAN #Para usar kmeans
from sklearn.preprocessing import StandardScaler #Para estandarizar nuestros datos
from sklearn.metrics import silhouette_samples, silhouette_score #Para el coeficiente de silhouette
from sklearn.cluster import AgglomerativeClustering #Para clustering jerárquico
from sklearn.metrics import pairwise_distances #Para las distancias a pares
from scipy.cluster.hierarchy import dendrogram, cophenet, linkage #Para graficar los dendrogramas y calcular el coeficiente cofenetico
from scipy.cluster import hierarchy #Para graficar los dendrogramas
from scipy.spatial.distance import pdist #Para calcular la distancia con el coeficiente cofenetico
import scipy.stats as ss
#import community as community_louvain #Para louvain
#import networkx as nx #Para grafos

path = r"C:\Users\nicoa\Documents\Programacion\datos\dataset_clustering_teorico.csv"
stock_data = pd.read_csv(path, sep=",")
print(stock_data.head())
print(stock_data.describe())
print(stock_data.info(max_cols=1000))
print(stock_data.drop_duplicates())
print(stock_data.dropna())
stock_data = stock_data.rename(columns={"Unnamed: 0": "Empresas"})
stock_data = stock_data.set_index("Empresas")
#outliers = stock_data[stock_data[col] > stock_data[col].mean() + 3 * stock_data[col].std()]
Q1 = stock_data["2010-01-04"].quantile(0.07) #-0.4435993499999751
Q2 = stock_data["2010-01-04"].quantile(0.93) # 0.9708959100000023

#Q1 = df.quantile(0.25)
#Q3 = df.quantile(0.75)
#IQR = Q3 - Q1
#print(df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))

# datos de la variacion de precio de 60 acciones desde el 4/1/2010
# hasta el 29/10/2012

scaler = StandardScaler()
stock_data_normalizado = scaler.fit_transform(stock_data)
stock_data_normalizado = pd.DataFrame(stock_data_normalizado)
print(stock_data_normalizado)

"""
valores_ya_normalizados = stock_data.copy()
lista = []
lista2 = []
index_list = []
for i in stock_data.columns:
    z,pval = ss.normaltest(stock_data[i])
    if pval >= 0.3:
        lista.append(i)
    if pval < 0.3:
        lista2.append(i)

for j in stock_data.index:
    index_list.append(j)

valores_ya_normalizados.drop(lista2, axis =1, inplace = True )
print(valores_ya_normalizados)

stock_data.drop(lista, axis = 1, inplace = True)
scaler = StandardScaler()
stock_data_normal = scaler.fit_transform(stock_data)
new_stock_data = pd.DataFrame(data = stock_data_normal, index = index_list, columns = lista2)
print(new_stock_data)
stock_final =pd.merge(valores_ya_normalizados,new_stock_data, how = "inner", left_index=True, right_index=True)
print(stock_final)
print(stock_final.describe())

for i in stock_data.columns:
    listaaa = []
    listaasa = []
    for value in stock_data[i].values:
        if value > (stock_data[i].mean() + (2 * stock_data[i].std())) or value < (stock_data[i].mean() - (2 * stock_data[i].std())):
            listaaa.append(value)
            listaasa.append(stock_data[i].mean())
    stock_data[i] = stock_data[i].replace(listaaa,listaasa)

print(stock_data.describe())

"""

valores_de_k = [2,3,4,5,6,7,8,9,10,11,12,13,14,15] #No se puede calcular para 1 grupo
inercias = pd.DataFrame(index = valores_de_k)
lista_inercias = []
lista_silhouette = []
for i in valores_de_k:
    kmeans = KMeans(n_clusters = i, init="random", n_init=10, max_iter=10000, random_state=123657)
    kmeans.fit(stock_data_normalizado)
    nro = kmeans.inertia_
    silo = silhouette_score(stock_data_normalizado, kmeans.labels_) 
    lista_inercias.append(nro)
    lista_silhouette.append(silo)
inercias["inercia"] = lista_inercias
inercias["silhouette"]  = lista_silhouette
print(inercias)
#Tomar valores de k dónde el gráfico cambia notablemente (en este caso 3 y 4 serían)
fig, axes = plt.subplots(1, 2, figsize=(15, 5))
fig.suptitle("Estudio de k-means")
sns.pointplot( ax=axes[0], x = inercias.index, y = inercias["inercia"])
sns.pointplot( ax=axes[1], x = inercias.index, y = inercias["silhouette"])
plt.show()