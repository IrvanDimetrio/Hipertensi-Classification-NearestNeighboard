"""
@author : Muhamad Irvan Dimetrio
NIM     : 18360018
Teknik Informatika
Institut Sains dan Teknologi Nasional
"""
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# Meload Dataset dari file csv dan mengekstrak fitur dan label classnya
hipertensiDataset = pd.read_csv('hipertensi.csv', names=['Umur', 'Kegemukan', 'class'], header=0)
fitur = hipertensiDataset.iloc[:, 0:2].values
label = hipertensiDataset.iloc[:, -1].values

# Mengambil algoritma K Nearest Neigbor sebagai model
model = KNeighborsClassifier(n_neighbors=3)

# Latih model menggunakan dataset
model.fit(fitur, label)

#Prediksi dengan data yang dimasukkan
umurInput = input("Umur anda ? \n"+ ">>>")
beratInput = input("Berat badan anda ? \n"+">>>")
umurData = float(umurInput)
beratData = float(beratInput)

prediksinya = model.predict([[umurData, beratData]])
if prediksinya == 0:
    print("Anda Sehat")
elif prediksinya == 1:
    print("Anda Terkena Hipertensi")
else:
    print("Maaf tidak tau. Masukin data yang bener dongg")