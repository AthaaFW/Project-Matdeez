import heapq

def dijkstra(graf, awal, tujuan):
    # Priority queue untuk memproses simpul
    queue = []
    heapq.heappush(queue, (0, awal))  # (cost, simpul)
    jarak = {simpul: float('inf') for simpul in graf}
    jarak[awal] = 0
    simpul_sebelumnya = {simpul: None for simpul in graf}  # Penyimpanan jalur terpendek

    while queue:
        jarak_now, simpul_now = heapq.heappop(queue)

        # Lewati jika jarak lebih besar dari jarak terbaik yang diketahui
        if jarak_now > jarak[simpul_now]:
            continue

        # Periksa tetangga
        for tetangga, bobot in graf[simpul_now].items():
            jarak_baru = jarak_now + bobot

            # Sorting jarak dan simpan ke queue
            if jarak_baru < jarak[tetangga]:
                jarak[tetangga] = jarak_baru
                simpul_sebelumnya[tetangga] = simpul_now
                heapq.heappush(queue, (jarak_baru, tetangga))

    # Rekonstruksi lintasan terpendek
    lintasan, simpul_now = [], tujuan
    while simpul_now:
        lintasan.append(simpul_now)
        simpul_now = simpul_sebelumnya[simpul_now]
    lintasan = lintasan[::-1]  # Balikkan lintasan

    return lintasan, jarak[tujuan]

# Graf
graf = {
    "UPI Cibiru": {"Cibiru": 2.6, "Cileunyi": 2},
    "Cileunyi": {"UPI Cibiru": 2, "Cibiru": 3.4, "Rancaekek": 5.7},
    "Rancaekek": {"Cileunyi": 5.7},
    "Cibiru": {"UPI Cibiru": 2.6, "Cileunyi": 3.4, "Ujung Berung": 5.3, "Arcamanik": 5.8, "Cinambo": 4.5},
    "Ujung Berung": {"Cibiru": 5.3, "Cimenyan": 4.1},
    "Cimenyan": {"Ujung Berung": 4.1},
    "Arcamanik": {"Cibiru": 5.8, "Kiara Condong": 5.6, "Batu Nunggal": 5.3},
    "Kiara Condong": {"Arcamanik": 5.6, "Batu Nunggal": 1.7, "Bandung Wetan": 6.1},
    "Batu Nunggal": {"Arcamanik": 5.3, "Kiara Condong": 1.7, "Lengkong": 4.7, "Cibeunying Kidul": 4.6, "Rancasari": 6.1},
    "Lengkong": {"Batu Nunggal": 4.7, "Bandung Wetan": 4},
    "Bandung Wetan": {"Lengkong": 4, "Kiara Condong": 6.1, "Cibeunying Kidul": 4.9, "Coblong": 2.5},
    "Cibeunying Kidul": {"Batu Nunggal": 4.6, "Coblong": 5.1, "Cibeunying Kaler": 1.7, "Bandung Wetan": 4.9},
    "Cibeunying Kaler": {"Cibeunying Kidul": 1.7, "Coblong": 4},
    "Coblong": {"Cibeunying Kidul": 5.1, "Cibeunying Kaler": 4, "Geger Kalong": 7.9, "Bandung Wetan": 2.5},
    "Geger Kalong": {"Coblong": 7.9},
    "Cinambo": {"Cibiru": 4.5, "Rancasari": 3.8, "Gedebage": 2.2},
    "Rancasari": {"Batu Nunggal": 6.1, "Buah Batu": 5.6, "Cinambo": 3.8, "Gedebage": 1.2},
    "Buah Batu": {"Rancasari": 5.6},
    "Gedebage": {"Cinambo": 2.2, "Rancasari": 1.2}
}

# siswa dan kecamatan
siswa = {
    "Naufal": "Rancasari",
    "Bayu": "Geger Kalong",
    "Chandra": "Buah Batu",
    "Athaa": "Cibiru",
    "Nafian": "Cileunyi",
    "Rintan": "Cileunyi"
}

if __name__ == "__main__":
    while True:
        print(f"--Menu--\n")
        print(f"1. Dari lokasi mahasiswa\n")
        print(f"2. Dari Kecamatan\n")
        print(f"3. Tutup Program\n")
        pilih = int(input("Masukan pilihan: "))

        if pilih == 3:
            break

        if pilih == 1:
            print("Nama yang tersedia: ", list(siswa.keys()))
            nama = input("Masukkan nama: ").strip().lower()

            nama_found = None
            for key in siswa.keys():
                if key.lower() == nama:
                    nama_found = key
                    break

            if nama_found:
                awal = siswa[nama_found]
                lintasan, cost = dijkstra(graf, awal, "UPI Cibiru")
                print(f"\nLintasan terpendek dari {nama} ({awal}) ke UPI Cibiru: \n\n{' -> '.join(lintasan)}\n")
                print(f"Total jarak: {cost:.1f} km")
            else:
                print("Nama tidak valid!")
        
        if pilih == 2:
            print("Kecamatan yang tersedia: ", list(graf.keys()))
            awalInput = input("Masukan lokasi awal: ").strip().lower()

            lokasi_found = None
            for key in graf.keys():
                if key.lower() == awalInput:
                    lokasi_found = key
                    break
            if lokasi_found:
                lintasan, cost = dijkstra(graf, lokasi_found, "UPI Cibiru")
                print(f"\nLintasan terpendek dari {lokasi_found} ke UPI Cibiru: \n\n{' -> '.join(lintasan)}\n")
                print(f"Total jarak: {cost:.1f} km")
            else:
                print("Lokasi tidak valid")
        else:
            print("Pilihan tidak tersedia")
