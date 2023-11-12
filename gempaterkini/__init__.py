import request3
from bs4 import BeautifulSoup


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
    try:
        content = request3.get('https://bmkg.go.id')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        result = soup.find('span', {'class' : 'waktu'})
        result = result.text.split(', ')
        waktu = result[1]
        tanggal = result[0]


        result = soup.find('div', {'class' : 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None

        for res in result:
            print(i, res)
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i = i + 1



        hasil = dict()
        hasil['tanggal'] = tanggal #'11 November 2023'
        hasil['waktu'] = waktu #'08:16:02 WIB'
        hasil['magnitudo'] = magnitudo #3.9
        hasil['kedalaman'] = kedalaman #'2 km'
        hasil['koordinat'] = {'ls': ls, 'bt': bt}
        hasil['lokasi'] = lokasi #'Pusat gempa berada di darat 10 Km Tenggara Samosir'
        hasil['dirasakan'] = dirasakan #'Dirasakan (Skala MMI): III Samosir'
        return hasil
    else:
        return None

def tampilkan_data(result):
    if result is None:
        print('Data tidak ditemukan')
        return
    print("Gempa Terakhir Berdasarkan BMKG")
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"kedalaman {result['kedalaman']}")
    print(f"koordinat LS={result['koordinat']['ls']} BT={result['koordinat']['bt']}")
    print(f"Lokasi {result['lokasi']}")
    print(f"{result['dirasakan']}")
