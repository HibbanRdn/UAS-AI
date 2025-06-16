# 🤖 Proyek Kecerdasan Buatan - A* Search dan ID3 Decision Tree

Repositori ini berisi dua implementasi algoritma dari buku *Artificial Intelligence: A Modern Approach (AIMA)*, yaitu:

1. **A\* Search** untuk pencarian jalur terpendek dalam grid 2D.
2. **Decision Tree (ID3)** untuk klasifikasi kelayakan kredit berdasarkan data nasabah.

Proyek ini dibuat sebagai bagian dari Ujian Akhir Semester mata kuliah **Kecerdasan Buatan**.

---

## 🔹 Bagian 1: A\* Search - Pencarian Jalur Terpendek

### 📌 Deskripsi  
A\* (A-Star) merupakan algoritma pencarian jalur (pathfinding) berbasis **heuristic** dan **cost**. Dalam proyek ini, A\* digunakan untuk mencari jalur terpendek dari titik awal ke tujuan pada grid 2D dengan rintangan, menggunakan **Manhattan Distance** sebagai heuristik.

### 🧠 Fungsi Algoritma  
- Menentukan rute tercepat dengan mempertimbangkan biaya saat ini dan estimasi ke tujuan.
- Cocok digunakan untuk pencarian jalur seperti pada peta, game, atau robotika.

### 📥 Contoh Grid

```python
grid = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [1, 1, 0, 0]
]
start = (0, 0)
goal = (0, 3)
````

### ✅ Output

```
Jalur terpendek: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (0, 3)]
```

### ▶️ Cara Menjalankan

Jika menggunakan Jupyter Notebook
1. Upload file di Jupyter Notebook
2. Run program (Ctrl + Enter/Command + Enter)

Jika menggunakan Vscode
1. Buka file python
2. Buat terminal baru
3. Run program dengan command di terminal:
```bash
python a_star.py
```

---

## 🔹 Bagian 2: Decision Tree (ID3) - Klasifikasi Kelayakan Kredit

### 📌 Deskripsi

Algoritma **ID3 (Iterative Dichotomiser 3)** digunakan untuk membangun pohon keputusan berdasarkan **information gain** dari setiap atribut. Dalam proyek ini, ID3 digunakan untuk menentukan apakah seorang nasabah **layak atau tidak layak** mendapatkan kredit berdasarkan atribut seperti:

* Usia
* Pendapatan
* Jenis pekerjaan
* Status pernikahan

### 🧠 Fungsi Algoritma

* Menghasilkan aturan keputusan berbentuk pohon.
* Digunakan dalam klasifikasi berbasis data historis.

### 📊 Contoh Data

* Dataset dari kaggle:
https://www.kaggle.com/datasets/vikasukani/loan-eligible-dataset

```
usia,pendapatan,pekerjaan,status,kelayakan
muda,tinggi,tetap,belum,tidak
tua,tinggi,kontrak,menikah,tidak
...
```

### ✅ Output

Program akan mencetak struktur pohon ke terminal dan menghasilkan diagram visual (jika diaktifkan).

### ▶️ Cara Menjalankan

Jika menggunakan Jupyter Notebook
1. Upload file di Jupyter Notebook
2. Sesuaikan Path data csv-mu
3. Run program (Ctrl + Enter/Command + Enter)

Jika menggunakan Vscode
1. Sesuaikan Path data csv-mu
2. Buat terminal baru
3. Run program dengan command di terminal:
```bash
python id3_tree.py
```

---

## 🎯 Tujuan Pembelajaran

* Menerapkan algoritma pencarian (A\*) untuk studi kasus pathfinding
* Membangun sistem klasifikasi berbasis pohon keputusan (ID3)
* Menghubungkan teori AI dengan kasus nyata

---

## 🧑‍🎓 Dibuat Oleh

> **Nama:** M. Hibban Ramadhan
> **Mata Kuliah:** Kecerdasan Buatan
> **Kelas:** PSTI B
> **Tahun Ajaran:** 2025
> **Dosen Pengampu:** Rio Ardi Ferdian

---
