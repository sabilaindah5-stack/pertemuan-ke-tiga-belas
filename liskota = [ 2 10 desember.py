liskota = [
    'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
    'Jogjakarta', 'Semarang', 'Makasar'

]

kotaYangDicari= input('ketik nama kota yang kamu cari: ')

for i, kota in enumerate(listkota):
    # kita ubah katnya ke lowercase agar
    # menjadi case insensitive
    if kota.lower() == kotaYangDicari.lower():
        print('kota yang anda cari berada pada indeks', i)
        break

    else:
        print('Maaf, kota yang anda cari tidak ada')


