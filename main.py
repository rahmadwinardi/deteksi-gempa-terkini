"""
Aplikasi deteksi gempa bumi
MODULARISASI DENGAN FUNCTION
"""


def ekstaksi_data():
    """
    Tanggal : 11 November 2023,
    Waktu : 08:16:02 WIB
    Magnitudo :3.9
    Kedalaman : 2 km
    Lokasi : LU = 2.53  BT = 98.71
    Pusat Gempa : Pusat gempa berada di darat 10 Km Tenggara Samosir
    Dirasakann : Dirasakan (Skala MMI): III Samosir
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '11 November 2023'
    hasil['waktu'] = '08:16:02 WIB'
    hasil['magnitudo'] = 3.9
    hasil['kedalaman'] = '2 km'
    hasil['lokasi'] = {'lu': 2.53, 'bt':98.71}
    hasil['pusat'] = 'Pusat gempa berada di darat 10 Km Tenggara Samosir'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): III Samosir'
    return hasil

def tampilkan_data(result):
    print("Gempa Terakhir Berdasarkan BMKG")
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"kedalaman {result['kedalaman']}")
    print(f"lokasi LU={result['lokasi']['lu']} BT={result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")

if __name__ == '__main__':
    print('Aplikasi Utama')
    result = ekstaksi_data()
    tampilkan_data(result)