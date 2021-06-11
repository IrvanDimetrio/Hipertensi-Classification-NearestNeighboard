# Kasus Hipertensi Klasifikasi Nearest Neighbor

Kasus kita adalah memodelkan data Hipertensi yang memiliki fitur serta label(class). Langkah-langkah machine learning yang kita develop adalah :

Step 1:
Memvisualisasi sebaran data hipertensi untuk melihat gambaran datanya dengan tujuan :
•	Algoritma apa yang cocok untuk dataset yang diberikan.
•	Dalam kasus ini kita akan pakai algoritma K Nearest Neighbor.

Step 2:
Membuat model dan menguji (Validasi) model dengan tahapan :
•	Memecah dataset menjadi data training dan data testing.
•	Membuat model dengan data training.
•	Sekaligus model di-validasi dengan data testing
o	metode defaultnya adalah dengan K-fold subsampling.
•	Menghitung seberapa akurasi dari model yang dibuat.

Step 3:
Jika model telah "akurat" maka langkah berikutnya :
•	Terapkan dataset dengan algoritma tadi agar menjadi model yang akan dipakai
•	Buat langkah kode untuk memasukkan data yang akan di prediksi oleh model tadi

## Library Yang Dibutuhkan

```
pip install seaborn
pip install matplotlib
pip install pandas
pip install scikit-learn
```

## Step 1 Hipertensi Plot
Dengan output sebagai berikut :

![Figure_1](https://user-images.githubusercontent.com/52452132/121645227-24819080-cabe-11eb-88e7-f54a623bdbd8.png)

## Step 2 Menghitung Akurasi Model
Dengan output sebagai berikut :

![image](https://user-images.githubusercontent.com/52452132/121645496-762a1b00-cabe-11eb-84d0-26a99059a108.png)

## Step 3 Memprediksi Apakah Orang Terkena Hirpentensi Dengan KNN
Dengan output sebagai berikut :

![image](https://user-images.githubusercontent.com/52452132/121645780-c99c6900-cabe-11eb-9ae5-c054e8f122ee.png)




