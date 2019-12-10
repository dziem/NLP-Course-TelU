# NER

Tugas opsional NER

## Data

Karena data tugas bigram dan postag kemarin beda jauh dengan data yang akan dilabeli di tugas ini, maka data latih yang digunakan adalah data test dan train yang sudah berlabel.

## List Lookup / Gazeteer

Karena data latih kurang untuk melabeli kalimat tugas, oleh karena itu digunakan list lookup/gazeteer sebagai salah satu fitur di classification (naive bayes) dan CRF. List berisi semua (mungkin kurang 1 atau 2) entitas PER, ORG, dan LOC yang ada di data latih dan data yang akan dilabeli.

Penggunaan list lookup adalah dengan edit distance dengan nilai cost yang berbeda untuk setiap operasi, berikut cost lengkap untuk setiap operasi:

| Operasi | Cost |
| ------- | ---- |
| Insertion spasi atau tanda hubung | 10 |
| Insertion karakter lain | 100 |
| Deletion spasi atau tanda hubung | 10 |
| Deletion karakter lain | 100 |
| Substituion suatu karakter dengan karakter yang sama | 0 |
| Substituion suatu angka dengan angka lain | 10 |
| Substituion spasi dengan tanda hubung | 10 |
| Substituion tanda hubung dengan spasi | 10 |
| Substituion suatu huruf kapital dengan huruf kecilnya | 10 |
| Substituion suatu huruf kecil dengan huruf kapitalnya | 10 |
| Substituion karakter lain | 50 |


Setelah itu nilai edit distance dinormalisasikan dengan rumus:
```
normalized_cost = (total_cost + 0.4) / panjang_frasa_di_list
``` 

List lookup akan mencari frasa dalam window size 2 (2 kata sebelah kiri dan kanan) dari suatu kata, apabila ada salah satu frasa menghasilkan nilai normalized_cost sebesar 20 maka fitur ini bernilai true.

## Rule Based

Hal yang digunakan untuk membuat rule adalah:

1. POSTAG NNP
2. Apakah token/kata diawali huruf kapital (untuk LOC dan PER)
3. Apakah semua karakter token/kata berupa huruf kapital (untuk ORG)
4. Apakah token/kata sebelum berupa 'di', 'ke', atau 'dari' (untuk LOC)

Nama file hasil adalah rulebased_output.txt

## Classification

Fitur yang digunakan untuk classification adalah:
1. Apakah karakter pertama kata/token merupakan huruf kapital
2. Apakah semua karakter token/kata berupa huruf kapital
3. Apakah semua karakter token/kata berupa angka
4. POSTAG token/kata
5. Hasil list lookup pada suatu token/kata, token/kata sebelum, dan token/kata sesudah. List lookup dilakukan pada semua entitas

Fitur token/kata dalam bentuk lowercase tidak digunakan karena data latih kurang banyak dan hasilnya sangat jelek.

Nama file hasil adalah klasifikasi_output.txt

## CRF

Fitur yang digunakan untuk CRF masih sama dengan kodingan asli, hanya saja ditambah list lookup untuk setiap kata. List lookup dilakukan pada semua entitas.

Nama file hasil adalah crf_output.txt