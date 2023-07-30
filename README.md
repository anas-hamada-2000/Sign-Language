# Real-Time Sign-Language Recognizer
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
![Mobile Net Parameters](https://github.com/anas-hamada-2000/Sign-Language/blob/4feab0fa060a44ef5728d2a417f70cd6f3793c32/readme%20images/Mobile_Fig_04.png)
## Örnekler:
![Örnek 1](https://github.com/anas-hamada-2000/Sign-Language/blob/19c96038c18ff488a9b35dd23fbcb94e7f98be3b/readme%20images/Screenshot%202023-06-21%20113741.png)
![Örnek 2](https://github.com/anas-hamada-2000/Sign-Language/blob/28e4344bc326a4aabb3d485df974d2e455736b42/readme%20images/Screenshot%202023-06-21%20113808.png)

https://github.com/anas-hamada-2000/Sign-Language/assets/68608987/ae01e5fb-c382-4c7d-89ea-cedf13e1f8cf

https://github.com/anas-hamada-2000/Sign-Language/assets/68608987/448b3354-a2d0-4c0a-aaee-d04de31c49bc

## Kullanılan Materyal Ve Metotlar:
### a) Materyal Listesi:
 * kullanılan dataset: Kullanılan veri setinde Türk İşaret Dilindeki
her harf için 500 adet resim bulunmaktadır.
 * TensorFlow: makine öğrenimi için ücretsiz ve açık kaynaklı bir
yazılım kütüphanesidir
 * Matplotlib: 2 boyutlu grafikler hazırlamamızı sağlayan bir python
kütüphanesidir
 * NumPy: Python programlama dili için büyük, çok boyutlu dizileri
ve matrisleri destekleyen, bu diziler üzerinde çalışacak üst düzey
matematiksel işlevler ekleyen bir kitaplıktır
 * Pandas: veri işlemesi ve analizi için python programlama dilinde
yazılmış olan bir yazılım kütüphanesidir
 * OpenCV: bilgisayarla görü, makine öğrenimi, görüntü işleme,
video analizi gibi uygulamalar için kullanılan devasa bir açık
kaynak kodlu kütüphanedir
### b) Metoda Listesi:
 * HandDetector: Görüntüdeki ellerin konumlarını belirleyen bir
fonksiyon
 * cv2.resize: Ölçekleme(scaling) resmin yeniden boyutlandırılması
işlemidir
 * cv2.imread: Bir resmi okumak için cv2.imread () fonksiyonu
kullanılır. Resim çalışma dizininde olmalıdır veya tam bir resim
yolu verilmelidir
 * cv2.imwrite: Bir resmi kaydetmek için cv2.imwrite() fonksiyonu
kullanılır
 * cv2.imshow: parametre olarak verdiğimiz bir mat nesnesini resim
tipine dönüştürerek bir pencere içerisinde ekranda gösterir
 * ‘adam’ optimizer: w değerlerinin iyileştirilmesi için kullanılan bir
optimizasyon algoritması, ve her bir parametre için gerçek
zamanlı olarak öğrenme oranını günceller
 * fit() fonksiyonu: eğitim sırasında değişenlerin kaydını tutan bir
“geçmiş” objesi döndürmektedir

