Aşağıdaki plan, iki alt projeyi tek bir “mini araştırma” çatısında birleştirir ve MAT353’in proje beklentilerine (rapor yapısı, matematiksel içerik, hata analizi, grafikler, iterasyon/hata eğrileri, teknoloji vurgusu) doğrudan oturur. Proje teslim/format şartları da ders materyalinde açıkça geçiyor.  

## 1) Proje başlığı ve tek cümlelik amaç

Önerilen başlık:
“En Küçük Karelerde Çözüm ve Doğrulama: Normal Denklem, QR ve Gradient Descent’in Sayısal Kararlılık Analizi + Gradient Checking”

Tek cümle amaç:
Doğrusal regresyonda en küçük kareler problemini (i) kapalı form/doğrudan yöntemlerle ve (ii) iteratif yöntemlerle çözüp; koşullanma, floating-point hata türleri ve sayısal türev (central difference) üzerinden kararlılık ve doğruluk karşılaştırması yapmak.

Bu konu, dersin “En Küçük Kareler”, “matris işlemleri/çözüm”, “sayısal hata türleri” ve “sayısal türev” başlıklarıyla birebir uyumlu.    

## 2) Proje kapsamı: Tek hikâye içinde iki alt proje

### Bölüm A: Doğrusal regresyonu çözme (Normal Denklem vs GD)

Problem:
[
\min_{\theta} J(\theta)=\frac{1}{2n}|X\theta-y|_2^2
]
Çözümler:

1. “Kötü pratik” olarak inverse ile: (\theta=(X^TX)^{-1}X^Ty)
2. Daha doğru pratik: `np.linalg.solve((X.T@X),(X.T@y))`
3. Daha stabil varyant: QR ile least squares
4. İteratif: Batch Gradient Descent (isteğe bağlı momentum)

### Bölüm B: Gradient Checking (Sayısal vs Analitik gradyan)

Aynı (J(\theta)) için:

* Analitik gradyan: (\nabla J(\theta)=\frac{1}{n}X^T(X\theta-y))
* Sayısal gradyan: merkezi fark (central difference)
  Ders notunda merkezi farkın daha yüksek doğruluk verdiği vurgulanıyor. 
  Epsilon taraması ile truncation vs rounding tartışması yapılır (dersin hata türleriyle birebir). 

## 3) Veri planı (2 veri: sentetik + küçük gerçek)

### 3.1 Sentetik veri (kararlılık deneyleri için ana veri)

Amaç: koşullanmayı kontrollü biçimde bozmak.

* Boyutlar: (n=2000), (d=20) (d’yi ayrıca ölçekleyerek runtime analizi yapacaksın)
* Üretim:

  * (x_1 \sim \mathcal{N}(0,1))
  * Kolineer özellik:
    [
    x_2 = x_1 + 10^{-p},\xi,\quad \xi\sim\mathcal{N}(0,1)
    ]
  * (p\in{1,2,3,4,5,6,7,8}) (p arttıkça daha kötü koşul)
  * Diğer özellikler: normal dağılım veya (x_1)’in türevleri gibi hafif korelasyon
* Gerçek parametre: (\theta_{true}) seç (rastgele ama sabit seed)
* Çıktı: (y = X\theta_{true} + \eta), (\eta\sim\mathcal{N}(0,\sigma^2))

Burada “parametre hatası” ölçebilirsin: (|\theta-\theta_{true}|/|\theta_{true}|). (Gerçek veride bu metrik yok.)

### 3.2 Küçük gerçek veri (modelleme demosu)

* Öneri: `sklearn.datasets.fetch_california_housing` (train/val split, standardizasyon)
  Amaç: gerçek dünyada RMSE/MAE gibi metriklerle kıyas göstermek.

## 4) Yöntemler ve matematiksel içerik (raporun “Yöntem” bölümünün omurgası)

Rapor formatında “Yöntem” bölümünde matematiksel ifadeler, türevler, algoritmik adımlar ve kullanılan teknoloji gerekçesi isteniyor. 

### 4.1 Normal denklem türetimi (kısa ama net)

[
J(\theta)=\frac{1}{2n}(X\theta-y)^T(X\theta-y)
]
[
\nabla_\theta J(\theta)=\frac{1}{n}X^T(X\theta-y)
]
[
\nabla_\theta J(\theta)=0 \Rightarrow X^TX\theta=X^Ty
]

Uygulama notu: inverse yerine solve vurgusu (kararlılık).

### 4.2 QR ile least squares (stabil çözüm)

* (X = QR) (reduced QR)
* (\min|X\theta-y|_2 = \min|QR\theta-y|_2)
* Çözüm: (R\theta = Q^Ty) ve `solve(R, Q.T@y)`

Normal denklemlerin koşul sayısını kötüleştirmesi (kabaca (\kappa(X^TX)\approx \kappa(X)^2)) tartışma kısmına güçlü “nümerik analiz” içeriği sağlar.

### 4.3 Gradient Descent

Güncelleme:
[
\theta^{k+1} = \theta^k - \alpha \nabla J(\theta^k)
]
Durdurma kriteri (raporda göster):

* (|\nabla J(\theta^k)|_2 \le \tau) veya
* (|J_{k+1}-J_k|/J_k \le \epsilon)

## 5) “Nümerik analiz” çekirdeği: stabilite ve hata analizi

### 5.1 Koşullanma deneyi (projenin araştırma kısmı)

Her (p) için raporla:

* (\kappa(X)), (\kappa(X^TX))
* Çözüm yöntemlerine göre:

  * Train/Val RMSE
  * (|X\theta-y|) (residual norm)
  * Sentetikte parametre hatası

Beklenen gözlem:

* Inverse ile çözüm p büyüdükçe bozulur
* Normal denklem + solve inverse’den iyi ama ill-conditioning’de yine kırılgan
* QR daha stabil


### 5.2 Gradient checking ve epsilon taraması

Sayısal türev için merkezi fark:
[
g_i^{num}\approx \frac{J(\theta+\varepsilon e_i)-J(\theta-\varepsilon e_i)}{2\varepsilon}
]
Merkezi farkın daha doğru olduğu derste belirtilmiş. 

Karşılaştırma metriği (relative error):
[
relerr_i=\frac{|g_i^{analytic}-g_i^{num}|}{\max(|g_i^{analytic}|,|g_i^{num}|)}
]
Epsilon taraması:
(\varepsilon\in{10^{-1},10^{-2},...,10^{-10}})

Grafikte beklenen “U-şekli” yorumu:

* Büyük (\varepsilon): truncation error baskın
* Çok küçük (\varepsilon): rounding error baskın
  Bu ayrım, dersin “yuvarlama vs kesme hatası” sınıflamasıyla doğrudan örtüşür. 

## 6) Deney metrikleri ve raporlama çıktıları

Rapor formatı, deneysel sonuçlarda “iterasyon sayıları, hata eğrileri, yakınsama grafikleri” gibi çıktıları özellikle istiyor. 

Minimum metrik seti:

* Regresyon performansı: MSE, RMSE (train/val)
* Stabilite: condition number, residual norm, sentetik parametre hatası
* GD yakınsama: iterasyon sayısı, (J(\theta)) eğrisi, (|\nabla J|) eğrisi
* Gradient checking: epsilon–relerr grafiği (float32/float64 ayrı çiz)
* Runtime: (n) ve (d) büyürken süre (Normal eq/QR/GD)

## 7) Karmaşıklık (Big-O) bölümü

Yöntem bölümüne koyacağın net tablo:

* Normal denklemler:

  * (X^TX) hesap: (O(nd^2))
  * Çözüm (genel): (O(d^3))
* QR:

  * (O(nd^2))
* GD:

  * Her iterasyon (O(nd))
  * Toplam (O(knd))

## 8) Colab notebook planı (hücre sırası ve çıktı garantisi)

Teslimde Colab’ın “çalışır” olması ve çıktılarının üretilmiş olması beklentisini karşılayacak şekilde:

1. Setup

* imports, seed, helper fonksiyonlar, cihaz bilgisi (CPU/GPU)

2. Veri üretimi

* `make_synthetic(p, n, d, sigma)`
* gerçek veri yükleme + preprocessing (split, standardize)

3. Çözücüler (fonksiyonel yapı)

* `solve_normal_inverse(X,y)`
* `solve_normal_solve(X,y)`
* `solve_qr(X,y)`
* `solve_gd(X,y, alpha, max_iter, tol)`

4. Koşullanma deneyleri (sentetik)

* p döngüsü: cond, theta error, RMSE, residual
* tablo + 2–3 grafik

5. GD yakınsama analizleri

* iyi koşul vs kötü koşul için loss ve grad-norm grafikleri
* (opsiyonel) feature scaling etkisi

6. Gradient checking

* tek bir (\theta) noktasında analytic vs numeric gradient
* epsilon sweep grafikleri
* float32 vs float64 karşılaştırması

7. Runtime deneyi

* farklı (n,d) senaryoları
* süre tablosu + grafik

8. Son özet hücresi

* “bulgular” maddeleri (sunumda da kullanırsın)

## 9) Rapor planı (8–15 sayfayı dolduran net iskelet)

Rapor formatında özetin 200–250 kelime olması ve referans verilmemesi isteniyor. 

Sayfa bütçeli öneri:

1. Kapak (1 sayfa)

* Başlık, ad-soyad, no, GitHub linki

2. Özet (0.5 sayfa)

* Amaç + yöntemler + 3 ana bulgu (referans yok) 

3. Giriş (1–2 sayfa)

* Problem bağlamı (mühendislik/veri)
* Literatür: en az 3 bilimsel kaynakla “least squares çözümü, QR stabilitesi, sayısal hata” çerçevesi 
* Senin katkın: “koşullanma + epsilon taraması ile stabilite analizi”

4. Yöntem (2–4 sayfa)

* Problem formülasyonu
* Normal denklem türetimi
* QR çözümü
* GD algoritması + durdurma kriteri
* Gradient checking formülleri
* Big-O tablosu
* Kullanılan teknoloji gerekçesi (NumPy/SciPy/JAX opsiyon) 

5. Uygulama (2–4 sayfa)

* Veri üretimi (p ile kolinear özellik)
* Kod mimarisi (fonksiyonlar)
* Hassasiyet tercihleri (float32/64) ve nedenleri 

6. Deneysel Sonuçlar (1–3 sayfa)

* p’ye göre performans ve kararlılık
* GD yakınsama grafikleri
* epsilon–relerr grafikleri
* runtime grafikleri
  Bu bölümde tablo ve şekilleri mutlaka yorumla. 

7. Tartışma (1 sayfa)

* “Hangi koşulda hangi yöntem?”
* Normal denklem neden kırılgan?
* GD neden yavaş/duyarlı?
* epsilon taramasındaki U-şekli ne anlatıyor? 

8. Test Süreçleri (0.5 sayfa)

* Gradient check birim testi
* Çözücüler arası tutarlılık testleri 

9. Sonuç ve Öneriler (0.5 sayfa)

* 3–5 madde sonuç
* Gelecek iş: ridge, SVD, SGD, JAX hızlandırma 

10. Kaynakça (IEEE)

* Metin içi [1],[2]… kuralı 

## 10) Sunum planı (en fazla 10 slayt, 15 dk)

Ders slaytında sunumun 15 dk ve en fazla 10 slayt olması isteniyor. 

Slayt taslağı:

1. Başlık, amaç, katkı
2. Problem formülasyonu (J(θ))
3. Yöntem haritası (Normal eq / QR / GD / GradCheck)
4. Normal denklem türetimi (kısa)
5. Koşullanma deneyi: cond vs hata (tek ana grafik)
6. Stabilite: inverse vs solve vs QR (tablo/çubuk grafik)
7. GD yakınsama: loss ve grad-norm eğrisi
8. Gradient checking: epsilon–relerr grafiği (U-şekli)
9. Runtime + Big-O (tek slayt)
10. Sonuç, “hangi yöntemi ne zaman seçeriz?”, demo hücresi

Demo: Colab’da tek hücre çalıştırıp “ana grafiklerin” hazır çıktısını göster (demo çalışmazsa puan kırılma riski var). 

## 11) 17–21 Aralık çalışma planı (teslime kadar)

17 Aralık

* Notebook iskeleti + veri üretimi + 3 çözücü (inverse/solve/QR)
* Sentetik p-döngüsü ilk tablo/cond hesapları

18 Aralık

* GD implementasyonu + yakınsama grafikleri
* Feature scaling ve alpha hassasiyeti (en az 2 senaryo)

19 Aralık

* Gradient checking modülü + epsilon taraması
* float32 vs float64 karşılaştırması

20 Aralık

* Runtime deneyi (n,d sweep)
* Raporun “Yöntem/Uygulama/Sonuçlar” taslağı ve figürlerin numaralanması

21 Aralık

* Rapor final: Tartışma + Sonuç + Kaynakça IEEE
* Sunum 10 slayt final + Colab tüm hücreler çalıştırılmış, çıktı üretilmiş kontrol

## 12) Kaynak planı (en az 3 bilimsel kaynak)

Giriş bölümünde en az 3 bilimsel çalışma isteniyor. 
Bu projeye çok uygun, “akademik” ve savunulabilir 4 kaynak:

* J. Nocedal and S. J. Wright, Numerical Optimization, 2nd ed., Springer, 2006. ([Google Kitaplar][1])
* N. J. Higham, Accuracy and Stability of Numerical Algorithms, 2nd ed., SIAM, 2002. ([MathWorks][2])
* G. H. Golub and C. F. Van Loan, Matrix Computations, 4th ed., Johns Hopkins University Press, 2013. ([Nick Higham][3])
* CS231n Notes: “Gradient Checking” (pratik relerr tanımı ve epsilon davranışı anlatımı için). ([aman.ai][4])

Bu dört kaynak, “least squares/QR stabilitesi”, “nümerik hata/yuvarlama-kesme”, “optimizasyon ve GD” ve “gradient checking pratiği” eksenlerini akademik biçimde destekler.

## Sonuç: Bu proje MAT353 ile uyumlu mu?

Evet; çünkü proje:

* En küçük kareler ve matris tabanlı çözüm yaklaşımıyla dersin içerdiği lineer cebir/nümerik hesap kısmını kullanıyor.  
* Sayısal türev (central difference) ve doğruluk vurgusunu doğrudan uyguluyor. 
* Yuvarlama ve kesme hatalarını, epsilon taramasıyla deneysel olarak görünür kılıyor. 
* Rapor/sunumun istenen akademik yapısına ve “iterasyon/hata eğrileri” gibi çıktılara net biçimde karşılık veriyor.  

İstersen bir sonraki adım olarak, bu planı birebir uygulayacağın “Colab hücre başlıkları + fonksiyon isimleri + hangi grafikleri hangi hücrede üreteceğin” şeklinde, doğrudan notebook iskeleti (içindekiler) formatında da yazabilirim.

[1]: https://books.google.com/books/about/Numerical_Optimization.html?id=VbHYoSyelFcC&utm_source=chatgpt.com "Numerical Optimization - Jorge Nocedal, Stephen Wright - Google Books"
[2]: https://www.mathworks.com/academia/books/accuracy-and-stability-of-numerical-algorithms-higham.html?utm_source=chatgpt.com "Accuracy and Stability of Numerical Algorithms, 2e - MATLAB & Simulink Books"
[3]: https://nhigham.com/accuracy-and-stability-of-numerical-algorithms/?utm_source=chatgpt.com "Accuracy and Stability of Numerical Algorithms – Nick Higham"
[4]: https://aman.ai/cs231n/training-neural-nets-II/?utm_source=chatgpt.com "Aman's AI Journal • CS231n • Training Neural Networks II"
