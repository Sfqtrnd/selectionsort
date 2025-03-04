#SELECTION SORT UMUR KARYAWAN
#KELOMPOK 3

usiaKaryawan = [45, 32, 29, 50, 41, 36, 28, 39, 30, 47, 33, 25, 54, 37, 42, 49, 31, 34, 38, 26]
print(f"Usia karyawan sebelum diurutkan:  {usiaKaryawan}")
n = len(usiaKaryawan)
for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
        if usiaKaryawan[j] < usiaKaryawan[min_idx]:
            min_idx = j
    usiaKaryawan[i], usiaKaryawan[min_idx] = usiaKaryawan[min_idx], usiaKaryawan[i]
    
print(f"Usia karyawan setelah diurutkan:   {usiaKaryawan}")