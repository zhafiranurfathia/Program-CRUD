import mysql.connector as mysql
import os

class Connection:
    def __init__(self):
        self.con = mysql.connect(
            host="localhost",
            user="root",
            database="uasoop7101210019zhafiranurfathia",
            password="japira0503"
        )
        self.cursor = self.con.cursor()
        if self.con.is_connected():
            print("berhasil terhubung")
        else:
            print("gagal terhubung")

class pegawai(Connection):
    def __init__(self):
        super().__init__()
        self.tablename = "Pegawai"
        query = ("CREATE TABLE IF NOT EXISTS " + self.tablename +
                "(id INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, nip VARCHAR(30), nama VARCHAR(30), alamat TEXT, no_hp VARCHAR(25))")
        self.cursor.execute(query)
        
    def create(self):
        print("[CREATE PEGAWAI]")
        nip = input("masukan nip: ")
        nama = input("masukan nama: ")
        alamat = input("masukan alamat: ")
        no_hp = input("masukan no_hp: ")
        
        cursor = self.con.cursor()
        val = (nip, nama, alamat, no_hp)
        query = ("INSERT INTO " + self.tablename + 
                "(nip, nama, alamat, no_hp) VALUES (%s, %s, %s, %s)")
        try:
            cursor.execute(query, val)
            self.con.commit()
            print(cursor.rowcount, "data berhasil disimpan")
        except Exception as e:
            print(e,"Error : Tidak ada database yang tersedia")

    def read(self):
        query = f"SELECT * FROM `{self.tablename}`"
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            for data in result:
                print(data)
        except Exception as e:
            print(e, "data tidak tersedia")

    def update(self):
        nama_lama = input("masukkan nama pegawai : ")
        nama = input("update nama : ")
        alamat = input("update alamat : ")
        no_hp = input("update no_hp : ")
        quary = f"UPDATE `{self.tablename}` set `nama` = '{nama}', `alamat` = '{alamat}', `no_hp` = '{no_hp}' WHERE `nama` = '{nama_lama}'"
        try:
            self.cursor.execute(quary)
            self.con.commit()
            print('UPDATE PEGAWAI ' + nama + ' BERHASIL')
        except Exception as e:
            print(e, "Error : data tidak tersedia")

    def delete(self):
        nama = input("masukkan nama pegawai : ")
        quary = f"DELETE FROM `{self.tablename}` WHERE `nama` = '{nama}'"
        try:
            self.cursor.execute(quary)
            self.con.commit()
            print('Data berhasil dihapus')
        except Exception as e:
            print(e, "Error : data tidak tersedia")

class pengemudi(Connection):
    def __init__(self):
        super().__init__()
        self.tablename = "Driver"
        query = ("CREATE TABLE IF NOT EXISTS " + self.tablename +
                "(id INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, no_ktp INT(16), nama VARCHAR(30), alamat TEXT, no_hp VARCHAR(15), jenis_sim VARCHAR(10), no_sim VARCHAR(16), berlaku_sim DATE)")
        self.cursor.execute(query)

    def create(self):
        print("[CREATE Driver]")
        no_ktp = input("masukan no_ktp: ")
        nama = input("masukan nama: ")
        alamat = input("masukan alamat: ")
        no_hp = input("masukan no_hp: ")
        jenis_sim = input("masukan jenis_sim: ")
        no_sim = input("masukan no_sim: ")
        berlaku_sim = input("masukan masa berlaku_sim: ")
        
        cursor = self.con.cursor()
        val = (no_ktp, nama, alamat, no_hp, jenis_sim, no_sim, berlaku_sim)
        query = ("INSERT INTO " + self.tablename + 
                "(no_ktp, nama, alamat, no_hp, jenis_sim, no_sim, berlaku_sim) VALUES (%s, %s, %s, %s, %s, %s, %s)")
        try:
            cursor.execute(query, val)
            self.con.commit()
            print(cursor.rowcount, "data berhasil disimpan")
        except Exception as e:
            print(e, "Error : Database tidak tersedia")

    def read(self):
        query = f"SELECT * FROM `{self.tablename}`"
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            for data in result:
                print(data)
        except Exception as e:
            print(e, "data tidak tersedia")

    def update(self):
        nama_lama = input("masukkan nama driver : ")
        no_ktp = input("masukan no_ktp: ")
        nama = input("masukan nama: ")
        alamat = input("masukan alamat: ")
        no_hp = input("masukan no_hp: ")
        jenis_sim = input("masukan jenis_sim: ")
        berlaku_sim = input("masukan berlaku_sim: ")
        quary = f"UPDATE `{self.tablename}` set `no_ktp` = '{no_ktp}', `nama` = '{nama}', `alamat` = '{alamat}', `no_hp` = '{no_hp}', `jenis_sim` = '{jenis_sim}', `berlaku_sim` = '{berlaku_sim}' WHERE `nama` = '{nama_lama}'"
        try:
            self.cursor.execute(quary)
            self.con.commit()
            print('UPDATE DRIVER ' + nama + ' BERHASIL')
        except Exception as e:
            print(e, "Error : data tidak tersedia")

    def delete(self):
        nama = input("masukkan nama driver : ")
        quary = f"DELETE FROM `{self.tablename}` WHERE `nama` = '{nama}'"
        try:
            self.cursor.execute(quary)
            self.con.commit()
            print('Data berhasil dihapus')
        except Exception as e:
            print(e, "Data tidak tersedia")


class mobil(Connection):
    def __init__(self):
        super().__init__()
        self.tablename = "Mobil"
        query = ("CREATE TABLE IF NOT EXISTS " + self.tablename +
                "(id INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, nama_mobil VARCHAR(50), jenis_mobil VARCHAR(50), warna VARCHAR(50), tahun VARCHAR(20), stnk_atas_nama VARCHAR(50), no_rangka VARCHAR(50), no_mesin VARCHAR(50), no_polisi VARCHAR(50), status_pajak VARCHAR(20), berlaku_stnk DATE, harga_sewa INT(10), status VARCHAR(50))")
        self.cursor.execute(query)

    def create(self):
        print("[CREATE Mobil]")
        nama_mobil = input("masukan nama_mobil: ")
        jenis_mobil = input("masukan jenis_mobil: ")
        warna = input("masukan warna: ")
        tahun = input("masukan tahun: ")
        stnk_atas_nama = input("masukan stnk_atas_nama: ")
        no_rangka = input("masukan no_rangka: ")
        no_mesin = input("masukan no_mesin: ")
        no_polisi = input("masukan no_polisi: ")
        status_pajak = input("masukan status_pajak: ")
        berlaku_stnk = input("masukan berlaku_stnk: ")
        harga_sewa = input("masukan harga_sewa: ")
        status = input("masukan status: ")
        
        cursor = self.con.cursor()
        val = (nama_mobil, jenis_mobil, warna, tahun, stnk_atas_nama, no_rangka, no_mesin, no_polisi, status_pajak, berlaku_stnk, harga_sewa, status)
        query = ("INSERT INTO " + self.tablename + 
                "(nama_mobil, jenis_mobil, warna, tahun, stnk_atas_nama, no_rangka, no_mesin, no_polisi, status_pajak, berlaku_stnk, harga_sewa, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        try:
            cursor.execute(query, val)
            self.con.commit()
            print(cursor.rowcount, "data berhasil disimpan")
        except Exception as e:
            print(e, "Error : Database tidak tersedia")

    def read(self):
        query = f"SELECT * FROM `{self.tablename}`"
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            for data in result:
                print(data)
        except Exception as e:
            print(e, "data tidak tersedia")

    def update(self):
        nama_mobil_lama = input("masukkan nama_mobil : ")
        nama_mobil = input("masukan nama_mobil: ")
        jenis_mobil = input("masukan jenis_mobil: ")
        warna = input("masukan warna: ")
        tahun = input("masukan tahun: ")
        stnk_atas_nama = input("masukan stnk_atas_nama: ")
        no_rangka = input("masukan no_rangka: ")
        no_mesin = input("masukan no_mesin: ")
        no_polisi = input("masukan no_polisi: ")
        status_pajak = input("masukan status_pajak: ")
        berlaku_stnk = input("masukan berlaku_stnk: ")
        harga_sewa = input("masukan harga_sewa: ")
        status = input("masukan status: ")
        quary = f"UPDATE `{self.tablename}` set `nama_mobil` = '{nama_mobil}', `jenis_mobil` = '{jenis_mobil}', `warna` = '{warna}', `tahun` = '{tahun}', `stnk_atas_nama` = '{stnk_atas_nama}', `no_rangka` = '{no_rangka}, `no_mesin` = '{no_mesin}, `no_polisi` = '{no_polisi}, `status_pajak` = '{status_pajak}, `berlaku_stnk` = '{berlaku_stnk}, `harga_sewa` = '{harga_sewa}, `status` = '{status}' WHERE `nama_mobil` = '{nama_mobil_lama}'"
        try:
            self.cursor.execute(quary)
            self.con.commit()
            print('UPDATE MOBIL ' + nama_mobil + ' BERHASIL')
        except Exception as e:
            print(e, "Error : data tidak tersedia")

    def delete(self):
        nama_mobil = input("masukkan nama_mobil : ")
        quary = f"DELETE FROM `{self.tablename}` WHERE `nama_mobil` = '{nama_mobil}'"
        try:
            self.cursor.execute(quary)
            self.con.commit()
            print('Data berhasil dihapus')
        except Exception as e:
            print(e, "data tidak tersedia")

class konsumen(Connection):
    def __init__(self):
        super().__init__()
        self.tablename = "Konsumen"
        self._no_sim = None
        query = ("CREATE TABLE IF NOT EXISTS " + self.tablename +
                "(id INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, no_ktp INT(16), nama VARCHAR(30), alamat TEXT, no_hp VARCHAR(15), email VARCHAR(30), no_sim VARCHAR(16), status VARCHAR(15))")
        self.cursor.execute(query)  

    def create(self):
        print("[CREATE Konsumen]")
        no_ktp = input("masukan no_ktp: ")
        nama = input("masukan nama: ")
        alamat = input("masukan alamat: ")
        no_hp = input("masukan no_hp: ")
        email = input("masukan email: ")
        no_sim = input("masukan no_sim: ")
        status = input("masukan status: ")
        
        cursor = self.con.cursor()
        val = (no_ktp, nama, alamat, no_hp, email, no_sim, status)
        query = ("INSERT INTO " + self.tablename + 
                "(no_ktp, nama, alamat, no_hp, email, no_sim, status) VALUES (%s, %s, %s, %s, %s, %s, %s)")
        try:
            cursor.execute(query, val)
            self.con.commit()
            print(cursor.rowcount, "data berhasil disimpan")
        except Exception as e:
            print(e, "Error : databases tidak tersedia")

    def read(self):
        query = f"SELECT * FROM `{self.tablename}`"
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            for data in result:
                print(data)
        except Exception as e:
            print(e, "data tidak tersedia")

    def update(self):
        nama_lama = input("masukkan nama konsumen : ")
        no_ktp = input("masukan no_ktp: ")
        nama = input("masukan nama: ")
        alamat = input("masukan alamat: ")
        no_hp = input("masukan no_hp: ")
        email = input("masukan email: ")
        status = input("masukan status: ")
        quary = f"UPDATE `{self.tablename}` set `no_ktp` = '{no_ktp}', `nama` = '{nama}', `alamat` = '{alamat}', `no_hp` = '{no_hp}', `email` = '{email}', `status` = '{status}' WHERE `nama` = '{nama_lama}'"
        try:
            self.cursor.execute(quary)
            self.con.commit()
            print('UPDATE KONSUMEN ' + nama + ' BERHASIL')
        except Exception as e:
            print(e, "data tidak ada")

    def delete(self):
        nama = input("masukkan nama konsumen : ")
        quary = f"DELETE FROM `{self.tablename}` WHERE `nama` = '{nama}'"
        try:
            self.cursor.execute(quary)
            self.con.commit()
            print('Data berhasil dihapus')
        except Exception as e:
            print(e, "data tidak tersedia")

def menu():
    print("\n_____APLIKASI CRUD_____")
    print("silahkan pilih menu crud dibawah ini: ")
    print("1. CRUD PEGAWAI")
    print("2. CRUD DRIVER")
    print("3. CRUD MOBIL")
    print("4. CRUD KONSUMEN")
    print("0. EXIT")

    def menu_aplikasi():
        print(f"\n_____APLIKASI CRUD {db.tablename}_____")
        print("silahkan pilih menu dibawah ini: ")
        print("1. CREATE DATA")
        print("2. READ DATA")
        print("3. UPDATE DATA")
        print("4. DELETE DATA")
        print("5. KEMBALI KE MENU CRUD")
        print("0. EXIT")

        inmenu = input("Pilih menu> ")

        os.system("cls")

        if inmenu == "1":
            db.create()
        elif inmenu == "2":
            db.read()
        elif inmenu == "3":
            db.update()
        elif inmenu == "4":
            db.delete()
        elif inmenu == "5":
            menu()
        elif inmenu == "0":
            inmenu = input("apakah anda yakin ingin keluar [y/n]")
            if inmenu == "y":
                exit()
            else:
                print("selamat datang kembali di: ")
        else:
            print("menu yang anda pilih tidak tersedia")

    inmenu = input("Pilih menu>>>>> ")

    os.system("cls")

    if inmenu == "1":
        while(True):
            db = pegawai()
            menu_aplikasi()
            continue
    elif inmenu == "2":
        while(True):
            db = pengemudi()
            menu_aplikasi()
            continue
    elif inmenu == "3":
        while(True):
            db = mobil()
            menu_aplikasi()
            continue
    elif inmenu == "4":
        while(True):
            db = konsumen()
            menu_aplikasi()
            continue
    elif inmenu == "0":
        inmenu = input("apakah anda yakin ingin keluar >> ? [y/n]")
        if inmenu == "y":
            exit()
        else:
            print("selamat datang kembali di: ")
    else:
        print("menu yang anda pilih tidak tersedia")

if __name__ == "__main__":
    while(True):
        menu()
        continue