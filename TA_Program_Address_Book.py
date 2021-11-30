import os 
from prettytable import PrettyTable
from prettytable.prettytable import NONE
buku_alamat = PrettyTable()

#LIST KARYAWAN
data_karyawan=[
["A001A", "Wilthem Nassourth", "081255990065", "winatttt12@gmail.com", "Jl. Decarabian No.13, RT 3 RW 4, Kelurahan Mondstadt"],
["B002B", "Huang Luo Ann'","083599237509", "xannn888@gmail.com", "Jl. Mountain Shaper No.101, RT 7 RW 6, Kelurahan Liyue"],
["C003C", "Hirozumi Arata", "083924979034", "hrrzmm23@gmail.com", "Jl. Balladeer No.23, RT 5 RW 7, Kelurahan Inazuma"],
["D004D", "Elfiana Ristbert", "082246892301", "elfinnn122@gmail.com", "Perumahan Yggdrasil, Jalan Eland'orr No.44, RT.1 RW.3, Kelurahan Afata "],
["E005E", "Alamia Nur Indriani", "082327948921", "alamianr@gmail.com", "Apatemen Diamond Sky Lantai 31 No. 1, Jl. Decabarian, Kelurahan Mondstadt"],
["F006F", "Antajaya Senopati", "085528092415", "antajadja000@gamil.com", "Jl. Kertanegara No. 23, RT 2 RW 13, Kelurahan Akarayanegara"],
["G007G", "Liliana Darmawati", "082327091067", "llana8888@gmail.com", "Jl. Carano Academy No. 52, RT 1 RW 8, Kelurahan Okka"],
["H008H", "Emilia Nor Ihsan", "081266037910", "emilnr112233@gmail.com", "Jl. Amber Witch No.23, RT 21 RW 1, Kelurahan Lugnica"],
["I009I", "Ramalia Nor Ihsan", "082278016002", "rmmmanr098012@gmail.com", "Jl. Amber Witch No.23, RT 21 RW 1, Kelurahan Lugnica"],
["J010J", "Aredina Nor Ihsan", "085217903680", "aredinnnr@gmail.com", "Jl. Amber Witch No.23, RT 21 RW 1, Kelurahan Lugnica"],
["K011K", "lumières de bonté", "082346093681", "lmuiredebnt13@gmail.com", "Jl. Pangeran Antasari No.12, RT 2 RW 1, Kelurahan Jatinegara"]
]

#AKUN HRD
akun = ["12id34"]
password = ["ab123cd"]

def clear_screen ():
    os.system("cls")

 #LOGIN
def login():
    clear_screen()
    print("""
===== SELAMAT DATANG PROGRAM ADDRESS BOOKS KARYAWAN KAFE ====== 
          ◈◈◈◈ Silakan Login terlebih dahulu ◈◈◈◈     
    """)
    while True  :
        uname = input("Masukkan nama pengguna: ")
        pw = input("Masukkan password: ")
        if uname == akun[0] and pw == password[0] :
            print("Login berhasil!")
            break
        else:
            print("Gagal login, silahkan coba kembali! ")
            input("Tekan Enter untuk melanjutkan ")
            login()
            break

#PILIHAN MENU
def show_menu():
    clear_screen()
    print("""
+============================================+
|            Pilih menu di bawah             |
+============================================+
| 1. Tambah data karyawan                    |
| 2. Lihat data karyawan                     |
| 3. Edit data karyawan                      |
| 4. Hapus data karyawan                     |
| 5. Keluar dari program                     |
+============================================+
""")

#Function Data
#TAMPIL
def tampil_data():
    clear_screen()
    print("DATA YANG TERSIMPAN : ")
    buku_alamat = PrettyTable(["NO.","KODE. KARYAWAN","NAMA", "NO. PONSEL", "E-MAIL", "ALAMAT"])
    for index in range (len(data_karyawan)):
        index+=1
        buku_alamat.add_row([index,data_karyawan[index-1][0],data_karyawan[index-1][1],data_karyawan[index-1][2],data_karyawan[index-1][3],data_karyawan[index-1][4]])
    print(buku_alamat)

#TAMBAH
def tambah_data():
    y = "y"
    while y=="y":
        tampil_data()
        data_baru =  [input("Masukkan kode Karyawan: "), input("Masukkan Nama karyawan: "), input("Masukkan No. Telepon: "), input("Masukkan e-mail: "), input("Masukkan alamat: ")]
        data_karyawan.append(data_baru)
        print("Data karyawan baru berhasil ditambahkan")
        y = input("Tekan Enter untuk melanjutkan")
        tampil_data()
        input("Tekan Enter untuk kembali ke menu pilihan")            
        clear_screen()

#UBAH
def ubah_data():
    y="y"
    while y=="y":
        tampil_data()
        urutan=int(input("Tuliskan nomor yang ingin diubah: "))
        if urutan is not 0 :
            if data_karyawan[urutan-1]:
                data_karyawan[urutan-1][1]=input("Nama Karyawan: ")
                data_karyawan[urutan-1][2]=input("No. Ponsel: ")
                data_karyawan[urutan-1][3]=input("E-mail baru: ")
                data_karyawan[urutan-1][4]=input("Alamat baru: ")
                print("Menu berhasil diubah")
                input("Tekan enter untuk melanjutkan")
                break
            else :
                print("Data tidak ada!")
                
# HAPUS
def hapus_data():
    tampil_data()
    urutan = int(input("Data karyawan ke berapa yang ingin dihapus? "))
    if urutan is not 0 :
        print((data_karyawan[urutan-1]))
        del data_karyawan[urutan-1]
        tampil_data()
        print("Data sudah di hapus")
        input("Tekan enter untuk melanjutkan")

#UTAMA

login()
i = "y"
while i=="y":
    show_menu()
    menu = input("Pilih menu : ")
    try :
        if menu == "1":
            tambah_data()
        
        elif menu == "2":
            tampil_data()
            input("Tekan Enter untuk kembali ke menu pilihan")
        elif menu == "3":
            ubah_data()
    
        elif menu == "4":
            hapus_data()
    
        elif menu == "5":
            i = "t"
        else:
            print("Kode tidak tersedia")
            input("Tekan Enter untuk kembali ke menu pilihan") 
    except :
        print("Mohon perhatikan inputan")
        input("Tekan Enter untuk kembali ke menu pilihan") 
print ("◈◈◈◈ Terima kasih sudah menggunakan program, semoga hari anda menyenangkan ◈◈◈◈")
exit()
