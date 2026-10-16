
# Dosya Bütünlüğü Kontrolü

Bu proje, Python kullanılarak geliştirilmiş basit bir dosya bütünlüğü kontrol uygulamasıdır. SHA-256 algoritmasıyla dosyanın hash değeri hesaplanır ve daha önce kaydedilen değerle karşılaştırılır.

## Projenin Amacı

Dosya üzerinde sonradan bir değişiklik yapılıp yapılmadığını tespit etmeyi öğrenmek ve hash algoritmalarının siber güvenlikteki kullanımını anlamak.

## Kullanılan Teknolojiler

- Python
- hashlib modülü
- pathlib modülü
- SHA-256 hash algoritması

## Nasıl Çalışır?

1. Kullanıcı kontrol edilecek dosyanın yolunu girer.
2. Program dosyanın SHA-256 değerini hesaplar.
3. İlk kontrolde hash değeri referans olarak kaydedilir.
4. Sonraki kontrollerde yeni değer kayıtlı değerle karşılaştırılır.
5. Değerler farklıysa program dosyanın değiştirilmiş olabileceği konusunda uyarı verir.

## Nasıl Çalıştırılır?

Terminalde proje klasörüne gelin ve şu komutu çalıştırın:

```bash
python dosya_kontrol.py
```

Programın istediği yere kontrol edilecek dosyanın tam yolunu girin.

## Öğrendiklerim

- Python ile dosya okuma
- SHA-256 ile hash hesaplama
- Dosya yollarını yönetme
- Dosya bütünlüğü kontrolünün temel mantığı