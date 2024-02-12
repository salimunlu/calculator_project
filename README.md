# Hesap Makinesi Uygulaması

Bu uygulama, PyQt6 kullanılarak geliştirilmiş basit bir hesap makinesi uygulamasıdır. Uygulama, temel aritmetik işlemleri gerçekleştirebilir ve kullanıcı dostu bir arayüze sahiptir.

## Kullanılan PyQt6 Özellikleri

Bu projede aşağıdaki önemli PyQt6 özellikleri kullanılmıştır:

### QMainWindow
Uygulamanın ana penceresini temsil eder. Pencerenin başlığı, boyutu ve düzeni bu sınıf aracılığıyla ayarlanır.

### QLineEdit
Sonuçları görüntülemek için kullanılan, sadece okunabilir bir QLineEdit öğesidir.

### QPushButton
Uygulamadaki tüm butonlar bu sınıf kullanılarak oluşturulmuştur. Butonlara tıklama olayları bu sınıf aracılığıyla yönetilir.

### QVBoxLayout ve QHBoxLayout
Dikey ve yatay düzenleri oluşturmak için kullanılmıştır. Bu düzenler, butonlar, temizleme butonu ve sonuç alanını organize etmek için kullanılmıştır.

### QFont
Metin fontunu ayarlamak için kullanılmıştır. Sonuç alanındaki metni büyük ve kalın yapmak için QFont sınıfı kullanılmıştır.

### QMenuBar ve QAction
Uygulamanın menü çubuğunu ve içerisindeki eylemleri (tema değiştirme, çıkış yapma) yönetmek için kullanılmıştır.

### Stil Dosyası (QSS)
Uygulamanın görsel temasını ve widget stillerini belirlemek için `style.qss` dosyası kullanılmıştır.

### Hata Yönetimi
Hesaplama sırasında olası hataları ele almak için try-except blokları kullanılmıştır. Eğer bir hata oluşursa, kullanıcıya anlaşılır bir hata mesajı gösterilir.

## Kurulum

Projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları takip edin:

1. Proje dizinine gidin:
   ```
   cd hesap-makinesi-uygulamasi
   ```

2. Sanal bir ortam oluşturun:
   ```
   python -m venv venv
   ```

3. Sanal ortamı etkinleştirin:
   - Windows:
     ```
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```
     source venv/bin/activate
     ```

4. Gerekli paketleri yükleyin:
   ```
   pip install PyQt6
   ```

## Kullanım

Uygulamayı çalıştırmak için terminalde aşağıdaki komutu kullanın:

```bash
python main.py
```

Uygulamayı başlatmak için yukarıdaki komutu kullanın. Ardından, aritmetik işlemler yapmak için kullanıcı arayüzündeki butonları kullanabilirsiniz.

## Uygulama Temasını Değiştirme

Uygulama varsayılan olarak açık tema ile başlar. Menü çubuğundaki `Settings > App Theme` seçeneğini kullanarak tema arasında geçiş yapabilirsiniz.

