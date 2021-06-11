"""
@author : Muhamad Irvan Dimetrio
NIM     : 18360018
Teknik Informatika
Institut Sains dan Teknologi Nasional
"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

hipertensiDataset = pd.read_csv('hipertensi.csv', names=['Umur (Tahun)', 'Kegemukan (Kg)', 'label'], header=0, sep=",")

sns.scatterplot(x='Umur (Tahun)', y='Kegemukan (Kg)', hue='label', data=hipertensiDataset).set_title('Sehat Atau Hipertensi')
plt.figure(1) # n adalah nomor berbeda untuk setiap window gambar
plt.show()
