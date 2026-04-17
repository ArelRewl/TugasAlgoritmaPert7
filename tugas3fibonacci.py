while True:
    print("\nNIM GANJIL")
    print("1. A pangkat B")
    print("2. Hitung deret")
    print("0. Keluar")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        a = int(input("Masukkan suatu bilangan bulat: "))
        b = int(input("Masukkan pangkat yang diinginkan: "))

        for i in range(1, b + 1):
            hasil = a ** i
            print(f"Hasil {a} pangkat {i} adalah {hasil}")

    elif pilihan == "2":
        n = int(input("Masukkan jumlah N: "))

        a, b = 1, 1  
        total = 0

        for i in range(1, n + 1):
            suku = a / b

            if i % 2 == 1:
                total += suku
            else:
                total -= suku

            a, b = b, a + b

        print("Hasil deret =", total)

    elif pilihan == "0":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")