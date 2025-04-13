# Matriks A 5 x 5

A = [
    [2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2]
]

# Matriks B 5 X 5

B = [
    [4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4],
    [4, 4, 4, 4 ,4],
    [4, 4, 4, 4, 4]
]

# Inisialisasi matriks hasil 5 x 5 dengan nilai 0
hasil = [[0 for _ in range(5)] for _ in range(5)]

# Proses perkalian
for i in range(5):
    for j in range(5):
        for k in range(5):
            hasil[i][j] += A[i][k] * B[k][j]
            
# Menampilkan hasil 
print("Hasil Perkalian Matriks A X B: ")
for baris in hasil:
    print(baris)
    