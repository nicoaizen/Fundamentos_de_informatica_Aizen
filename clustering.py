#from networkx.algorithms.assortativity.correlation import numeric_assortativity_coefficient
import pandas as pd #Pandas para usar dataframes
import matplotlib.pyplot as plt #Para graficar
import matplotlib.cm as cm
from pandas.core.indexes.base import Index
from pandas.core.reshape.concat import concat #Para graficar el silhouette
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

#LIMPIEZA DE DATOS ->  NO HAY NAN NI DATOS DUPLICADOS
path = r"C:\Users\nicoa\Documents\Programacion\datos\dataset_clustering_teorico.csv"
stock_data = pd.read_csv(path)
#print(stock_data) #Hay 60 filas y 964 columnas
stock_data.rename(columns = {"Unnamed: 0":"Empresas"}, inplace = True)
#print(stock_data.info(max_cols= 1000)) #Todos los elementos son float
#print(stock_data.columns) #Va del 4/1/2010 hasta el 29/10/2014
print(stock_data.describe())
stock_data = stock_data.set_index("Empresas")
#print(stock_data) #Tenemos 963 columnas


#BUSCAMOS OUTLIERS, #Probar también con cuartiles
for i in stock_data.columns:
    lista1 = []
    lista2 = []
    for value in stock_data[i].values:
        #if value > (stock_data[i].mean() + (3 * stock_data[i].std())) or value < (stock_data[i].mean() - (3 * stock_data[i].std())):
        if value > stock_data[i].quantile(0.96) or value < stock_data[i].quantile(0.04) :
            lista1.append(value)
            lista2.append(stock_data[i].mean())
    stock_data[i] = stock_data[i].replace(lista1,lista2)

print(stock_data.describe())


#NORMALIZAR VALORES
valores_ya_normalizados = stock_data.copy()
lista = []
lista_1 = []
index_list = []
for i in stock_data.columns:
    z,pval = ss.normaltest(stock_data[i])
    if pval >= 0.3:
        lista.append(i)
    if pval < 0.3:
        lista_1.append(i)

for j in stock_data.index:
    index_list.append(j)

valores_ya_normalizados.drop(lista_1, axis =1, inplace = True )
print(valores_ya_normalizados)

stock_data.drop(lista, axis = 1, inplace = True)
scaler = StandardScaler()
stock_data_normal = scaler.fit_transform(stock_data)
new_stock_data = pd.DataFrame(data = stock_data_normal, index = index_list, columns = lista_1)
print(new_stock_data)
stock_final =pd.merge(valores_ya_normalizados,new_stock_data, how = "inner", left_index=True, right_index=True)
print(stock_final)
print(stock_final.describe())

#Elegir el mejor k para el  Kmeans -> Calculando silhouettes e Inercias
valores_de_k = [2,3,4,5,6,7,8,9,10,11,12,13,14,15] #No se puede calcular para 1 grupo
inercias = pd.DataFrame(index = valores_de_k)
lista_inercias = []
lista_silhouette = []
for i in valores_de_k:
    kmeans = KMeans(n_clusters = i, init="random", n_init=10, max_iter=10000, random_state=123657)
    kmeans.fit(stock_final)
    nro = kmeans.inertia_
    silo = silhouette_score(stock_final, kmeans.labels_) 
    lista_inercias.append(nro)
    lista_silhouette.append(silo)
inercias["inercia"]= lista_inercias
inercias["silhouette"]  = lista_silhouette
print(inercias)
#Tomar valores de k dónde el gráfico cambia notablemente (en este caso 3 y 4 serían)
fig, axes = plt.subplots(1, 2, figsize=(15, 5))
fig.suptitle("Estudio de k-means")
sns.pointplot( ax=axes[0], x = inercias.index, y = inercias["inercia"])
sns.pointplot( ax=axes[1], x = inercias.index, y = inercias["silhouette"])
plt.show()

#Veo como aparece para k = 3
kmeans = KMeans(n_clusters = 3, init="random", n_init=10, max_iter=10000, random_state=123457) #tomamos los centroides de forma aleatoria y definimos un máximo de 300 iteraciones
kmeans.fit(stock_final)  
print(kmeans.labels_)
print(kmeans.cluster_centers_)
print(silhouette_score(stock_final, kmeans.labels_)) 
print(kmeans.inertia_)
g = sns.scatterplot( x = stock_final.iloc[:,2], y = stock_final.iloc[:, 3], hue = kmeans.labels_, alpha = 0.5, palette= ["green", "yellow", "red"])
g = sns.scatterplot( x = kmeans.cluster_centers_[:,2], y = kmeans.cluster_centers_[:,3], zorder = 10, hue = [0,1,2], legend = False, marker=6, s=200, palette= ["green", "yellow", "red"])
plt.show()