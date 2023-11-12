"""
Aplikasi deteksi gempa bumi
MODULARISASI DENGAN FUNCTION
"""
import gempaterkini

if __name__ == '__main__':
    print('Aplikasi Utama')
    result = gempaterkini.ekstaksi_data()
    gempaterkini.tampilkan_data(result)
