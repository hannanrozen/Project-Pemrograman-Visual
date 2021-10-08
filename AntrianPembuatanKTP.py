# Project-Pemrograman-Visual
queue = []
nomor_out=1
while True:
    print("\n\nMenu:\n\n1. Masukkan Data\n2. Memanggil\n3. Keluar Dari Program \n")
    ipt_menu = int(input("Pilih Menu: "))
    if ipt_menu == 1:
        ipt_Nama = str(input("\nMasukkan Nama: "))
        ipt_Alamat = str(input("Masukkan Alamat: "))
        ipt_Ttl = str(input("Masukkan Tempat, Tanggal Lahir: "))
        ipt_Agama = str(input("Masukkan Agama: "))
        ipt_Kelamin = str(input("Masukkan Kelamin: "))
        queue.append(ipt_Nama)
        queue.append(ipt_Alamat)
        queue.append(ipt_Ttl)
        queue.append(ipt_Agama)
        queue.append(ipt_Kelamin)
    elif ipt_menu == 2:
        if queue:
            print("Nomor "+str(nomor_out))
            print("Nama : "+ queue.pop(0))
            print("Alamat : "+ queue.pop(0))
            print("Ttl : "+ queue.pop(0))
            print("Agama : "+ queue.pop(0))
            print("Kelamin : "+ queue.pop(0))
            nomor_out +=1
            print()
        else:
            print("Data Telah Kosong\n")
    elif ipt_menu == 3:
        break
    else:
        print("Input Salah\n")
        input("Tekan Enter untuk keluar")
        break
