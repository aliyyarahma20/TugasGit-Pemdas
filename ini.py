data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

#Tampilkan seluruh data dari data_panen termasuk nama lokasi dan hasil panen masing-masing
for lokasi in data_panen:
    Lokasi = data_panen[lokasi]
    print(f"Lokasi Panen: {Lokasi['nama_lokasi']}")
    print(f"Padi: {Lokasi['hasil_panen']['padi']} kg")
    print(f"Jagung: {Lokasi['hasil_panen']['jagung']} kg")
    print(f"Kedelai: {Lokasi['hasil_panen']['kedelai']} kg")
    print("-" * 25) 


#Tampilkan jumlah hasil panen jagung dari lokasi2
lokasi_dua = data_panen['lokasi2']
hasil_panen_jagung = lokasi_dua['hasil_panen']['jagung']
print(f"Jumlah hasil panen jagung di lokasi2 adalah  {hasil_panen_jagung} kg")
print("-" * 25) 

#Tampilkan nama lokasi dari lokasi3
lokasi_tiga = data_panen['lokasi3']
print(f"Nama lokasinya adalah {lokasi_tiga['nama_lokasi']}")
print("-" * 25) 

# Menghitung total hasil panen padi dan kedelai untuk setiap lokasi
for lokasi, hasil in data_panen.items():
    padi_aja = hasil['hasil_panen']['padi']
    kedelai_aja = hasil['hasil_panen']['kedelai']
    total = padi_aja + kedelai_aja
    print(f"Total hasil panen padi dan kedelai di {lokasi} adalah {total}")
print("-" * 25) 

# Percabangan
for a, b in data_panen.items():
    padii = b['hasil_panen']['padi']
    jaguung =  b['hasil_panen']['jagung']
    lokasinya = b['nama_lokasi']
    
    if padii > 1300 or jaguung > 800:
        print(f"Lokasi {lokasinya} memiliki hasil panen padi dan jagung yang banyak, jadi memerlukan perhatian khusus")
    else:
        print(f"Lokasi {lokasinya} memiliki hasil panen padi dan jagung yang tidak banyak, jadi kondisi baik")