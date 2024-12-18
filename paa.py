import time
def knapsack_divide_and_conquer(items, budget, n):
    # Basis: jika tidak ada barang atau anggaran habis
    if n == 0 or budget == 0:
        return 0

    # Jika harga barang lebih besar dari anggaran, lewati barang ini
    if items[n - 1]["price"] > budget:
        return knapsack_divide_and_conquer(items, budget, n - 1)

    # Pilih antara memasukkan atau tidak memasukkan barang ke keranjang
    else:
        # Nilai jika barang dimasukkan
        include = items[n - 1]["value"] + knapsack_divide_and_conquer(
            items, budget - items[n - 1]["price"], n - 1
        )

        # Nilai jika barang tidak dimasukkan
        exclude = knapsack_divide_and_conquer(items, budget, n - 1)

        # Kembalikan nilai maksimum
        return max(include, exclude)


# Daftar barang dengan harga dan manfaatnya
items = [
    {"name": "Susu", "price": 20, "value": 60},
    {"name": "Roti", "price": 10, "value": 40},
    {"name": "Keju", "price": 30, "value": 90},
    {"name": "Telur", "price": 40, "value": 100},
    {"name": "Buah", "price": 50, "value": 120},
]

# Anggaran yang tersedia
budget = 50

# Catat waktu sebelum eksekusi
start_time = time.time()

# Hitung nilai maksimum menggunakan algoritma Knapsack
max_value = knapsack_divide_and_conquer(items, budget, len(items))

# Catat waktu setelah eksekusi
end_time = time.time()

# Hitung waktu eksekusi
execution_time = end_time - start_time

print(f"Nilai maksimum yang dapat diperoleh: {max_value}")
print(f"Waktu eksekusi: {execution_time:.6f} detik")
