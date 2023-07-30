# Sign-Language
## Yapılan Çalışmaların Özeti:
### Veritabanı toplama:
Bu veritabanı, Türkçe dilindeki her harf için 500 fotoğraftan oluşmaktadır.
### Veritabanı analizi:
Bu fotoğrafları manuel olarak oluşturduğum için fotoğrafların ellerde ortalanmış olduğunu dikkate aldım ve fotoğraf boyutları da 224 x 224 'ye değiştirdim
### Model oluşturma:
Başlangıç olarak modelimiz MobileNet olacağını seçildi, çünkü küçük bir boyutu var ve aynı zamanda hızlı, ve sonra verileri normalleştirdik ve modeli eğitmek için kullandık ve pretrained bir model olduğu için büyük accuracy elde etmek için çok fazla epoch gerektirmedi\
### Modeli gerçek zamanlı bir şekilde çalıştırılması:
Video fotoğraflarını tek tek alıp analiz edeceğiz, ilk önce fotoğrafta el var mı yok mu ona bakacağız, varsa sadece elin(1 yada 2 el) görüntüsünü alacağız ve boyutlarını gerekli boyutlara çevireceğiz(224 x 224), ve fotoğrafı normalleştirdikten sonra onu sınıflandırmak için modele göndereceğiz, ve model bu fotoğraf için sınıflandırmasını bize geri getirecektir(hangi harfa ait), modelin bu sınıflandırmayı doğrulaması yüksekse, fotoğrafın bu harfi temsil ettiğini söyleyebiliriz.
### Kelime oluşturma:
Oluşturduğumuz harf dizisine karşılık gelen kelimeyi istiyoruz, bu nedenle, el hızlı hareket ettiğinde modelimiz hiçbir şey tahmin etmeyecektir çünkü el o sırada bir harften diğerine hareket etmektedir.El hareket konumundan dinlenme konumuna geçtiğinde, bu yeni bir harfe geçtiğimiz anlamına gelir ve bu nedenle dinlenme konumunda olduğu sürece model yeni harfi yalnızca bir kez tahmin edecektir.

---
![alt](https://github.com/anas-hamada-2000/Sign-Language/blob/4feab0fa060a44ef5728d2a417f70cd6f3793c32/readme%20images/Mobile_Fig_04.png)
## Örnekler:
