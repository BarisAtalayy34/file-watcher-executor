# File Watcher & Executor

Bu proje, işletim sistemlerinde belirli bir dizini **gerçek zamanlı** olarak izleyerek
yeni bir dosya oluşturulduğunda **otomatik olarak bir script çalıştıran**
event-tabanlı bir otomasyon sistemidir.

Proje, dosya sistemi olayları (file system events) ve süreç yönetimi (process execution)
mantığını uygulamalı olarak göstermeyi amaçlamaktadır.

---

## 🎯 Projenin Amacı

- Dosya sistemi olaylarını izlemek
- Yeni dosya oluştuğunda otomatik işlem başlatmak
- İşletim sistemi seviyesinde otomasyon mantığını göstermek
- Event-based (olay tabanlı) çalışma prensibini uygulamak

---

## 🛠 Kullanılan Teknolojiler

- **Python 3**
- **Watchdog (inotify benzeri dosya izleme kütüphanesi)**
- **Windows Batch Script (.bat)**
- Git & GitHub

> Not: Linux ortamında `.sh`, Windows ortamında `.bat` executor kullanılarak
> platform uyumlu bir yapı hedeflenmiştir.

---

## 📂 Proje Klasör Yapısı

