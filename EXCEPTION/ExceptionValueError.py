
try:
    umur_user = int(input("Berapa umur anda?\n"))
    print(f"Umur anda adalah {umur_user}.Terima kasih telah menggunakan program ini.")
except ValueError:
    print("Isi dengan angka!")