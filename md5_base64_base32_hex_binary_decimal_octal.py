import hashlib
import base64

if __name__ == "__main__":
    
    try:
        print("==========PROGRAM KRIPTOGRAFI STRING DAN KONVERSI BILANGAN==========\n")
        print("1. Kriptografi String \n2. Konversi Bilangan Desimal")
        pilihMenu = int(input("Pilih [1-2]?"))
        
        if(pilihMenu==1):
            print("\nPilih jenis kriptografi :\n1. md5 \n2. Base64 \n3. Base32")
            pilihString = int(input("Pilih [1-3]?"))

            if(pilihString==1):
                text = input("\nMasukkan string : ")
                textUTF8 = text.encode("utf-8")
                hash = hashlib.md5(textUTF8)
                md5 = hash.hexdigest()
                print("md5 \t\t: %s"%md5)

            elif(pilihString==2):
                text = input("\nMasukkan string : ")
                textUTF8 = text.encode("utf-8")
                base64_bytes = base64.b64encode(textUTF8)
                base64 = base64_bytes.decode("utf-8")
                print("Base 64 \t: %s"%base64)

            elif(pilihString==3):
                text = input("\nMasukkan string : ")
                textUTF8 = text.encode("utf-8")
                base32_bytes = base64.b32encode(textUTF8)
                base32 = base32_bytes.decode("utf-8")
                print("Base 32 \t: %s"%base32)

            else:
                print("\nERROR : Input tidak valid")

        elif(pilihMenu==2):
            print("\nPilih jenis bilangan :\n1. Hexadecimal \n2. Octal \n3. Biner")
            pilihBilangan = int(input("Pilih [1-3]?"))

            if(pilihBilangan==1):
                bilangan = int(input("\nMasukkan bilangan desimal \t: "))
                hexadecimal = hex(bilangan)
                print("Hexadecimal \t\t\t: %s"%hexadecimal)

            elif(pilihBilangan==2):
                bilangan = int(input("\nMasukkan bilangan desimal \t: "))
                octal = oct(bilangan)
                print("Octal \t\t\t\t: %s"%octal)

            elif(pilihBilangan==3):
                bilangan = int(input("\nMasukkan bilangan desimal \t: "))
                binary = bin(bilangan)
                print("Biner \t\t\t\t: %s"%binary)

            else:
                print("\nERROR : Input tidak valid")
        else:
            print("\nERROR : Input tidak valid")
    
    except Exception:
        print("ERROR : Input tidak valid")