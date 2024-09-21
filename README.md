# Instagram Bot

Bu proje, Instagram üzerindeki çeşitli etkileşimleri otomatikleştirmek için basit bir bot uygulamasıdır. Kullanıcılar, belirli komutlar aracılığıyla diğer kullanıcılarla etkileşimde bulunabilir, gönderilerini yönetebilir ve daha fazlasını yapabilir.

## Özellikler

- Belirtilen kullanıcılara mesaj gönderme
- Kullanıcıları takip etme ve takipten çıkarma
- Gönderilere yorum yapma ve beğenme
- Takipçi ve takip edilen listelerini görüntüleme
- Hikaye gönderme ve görüntüleme
- Konum gönderme
- Gönderileri planlama
- Daha fazlası!

## Gereksinimler

- Python 3.x
- `instabot` kütüphanesi
- `base64` ve `json` kütüphaneleri (Python ile birlikte gelir)

## Kurulum

1. Bu projeyi klonlayın veya indirin:
   ```bash
   git clone https://github.com/kullanici_adiniz/instagram-bot.git
   cd instagram-bot
Gerekli kütüphaneyi yükleyin:

```bash
Kodu kopyala
pip install instabot
```
bot.py dosyasını açın ve kullanıcı adınızı ve şifrenizi uygun şekilde ayarlayın.

Kullanım
Uygulamayı başlatın:

 ```bash
   git clone https://github.com/kullanici_adiniz/instagram-bot.git
   cd instagram-bot
```
Kodu kopyala
```bash
python3 bot.py
```
Komut istemine "help" yazarak mevcut komutları görüntüleyin.

İstediğiniz komutları girerek botu kullanmaya başlayın.

Komutlar
message @kullanici mesaj: Belirtilen kullanıcıya mesaj gönderir.
follow @kullanici: Belirtilen kullanıcıyı takip eder.
unfollow @kullanici: Belirtilen kullanıcıyı takipten çıkarır.
like @kullanici: Belirtilen kullanıcının son gönderisini beğenir.
get_followers: Hesabının takipçilerini listeler.
get_following: Takip ettiğin kullanıcıları listeler.
exit: Çıkış yapar.
Daha fazla komut için "help" yazarak yardım alabilirsiniz.

Lisans
Bu proje, MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakabilirsiniz.
