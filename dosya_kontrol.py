import hashlib
from pathlib import Path

def dosya_hash_hesapla(dosya_yolu):
    sha256=hashlib.sha256()
    with open(dosya_yolu, "rb") as dosya:
        while True:
            parca= dosya.read(4096)

            if not parca:
                break

            sha256.update(parca)

        return sha256.hexdigest()
dosya_yolu=input("Kontrol edilecek dosya yolunu giriniz:").strip().strip('"')
dosya=Path(dosya_yolu)

#bu noktada hash kaydını projemizin klasorunde tutuyoruz.
kayit_dosyasi=Path(__file__).with_name("hash_kaydi.txt")

if not dosya.is_file():
    print("Hata:Dosya bulunamadi!")
else:
    hash_degeri=dosya_hash_hesapla(dosya)
    tam_yol=str(dosya.resolve())

    print("\nDosya adi:",dosya.name)
    print("SHA-256:",hash_degeri)
if not kayit_dosyasi.exists():
    kayit_dosyasi.write_text(
        tam_yol+"\n"+hash_degeri,
        encoding="utf-8"
    )
    print("\nİlk kontrol tamamlandı.")
    print("Dosyanin referans hash değeri kaydedildi.")
else:
    kayitli_bilgiler=kayit_dosyasi.read_text(
        encoding="utf-8"
    ).splitlines()

    if len(kayitli_bilgiler) < 2:
     print("\n Hata:hash kaydi eksik veya bozuk")

    elif kayitli_bilgiler[0] != tam_yol:
        print("\nHata:Kayit baska bir dosyaya ait.")
        print("İlk kullanılan dosya yolunu giriniz.")

    elif hash_degeri == kayitli_bilgiler[1]:
        print("\nSONUC:Dosya değişmedi.")

    else:
          print("\nSONUC:Dosya değiştirilmiş olabilir.")
          print("Kayitli hash ile mevcut hash değerleri farklı.")