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



