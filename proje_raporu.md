# PROJE ADINIZ (İLGİ ÇEKİCİ VE KONUYU İÇEREN BİR BAŞLIK)
**Önerilen başlık:** *En Küçük Kareler Regresyonunda Normal Denklem, QR Ayrıştırması ve Gradient Descent Karşılaştırması: Koşullanma, Yakınsama ve Sayısal Kararlılık Analizi*

## MAT353 NÜMERİK ANALİZ DERSİ PROJE RAPORU

**Ad Soyad (Öğrenci No):** …  
**Ad Soyad (Öğrenci No):** …  
**Tarih:** …  
**Ders:** MAT353 Nümerik Analiz

---

# ÖZET
Bu çalışmada doğrusal regresyon için en küçük kareler (least squares) probleminin sayısal çözümünde kullanılan farklı yaklaşımlar, sayısal kararlılık ve performans ölçütleri açısından karşılaştırılmıştır. Tasarım matrisi \(X\) ve gözlem vektörü \(y\) verildiğinde amaç, \(J(\theta)=\frac{1}{2n}\lVert X\theta-y\rVert_2^2\) maliyetini minimize eden parametre vektörü \(\theta\)’yı bulmaktır. Kapalı form çözümler olarak normal denklem üzerinden (i) açık ters alma (inverse), (ii) doğrusal sistem çözümü (solve) ve (iii) QR ayrıştırmasına dayalı iki varyant uygulanmıştır. İteratif yaklaşım olarak gradyan inişi (Gradient Descent, GD) geliştirilmiş, yakınsama davranışı kayıp (loss) ve gradyan normu eğrileri ile değerlendirilmiştir. Ayrıca analitik gradyanın doğrulanması amacıyla merkez fark ile gradyan denetimi (gradient checking) yapılmış; epsilon seçiminin ve kayan nokta hassasiyetinin (float64–float32) göreli hataya etkisi deneysel olarak incelenmiştir. Sentetik veride özellikler arası kolineariteyi kontrol eden bir parametre ile koşullanma arttırılarak yöntemlerin hata duyarlılığı gözlemlenmiştir. Sonuçlar, iyi koşullandırılmış senaryolarda solve ve QR çözümlerinin neredeyse aynı doğruluğu verdiğini, açık ters almanın ise kötü koşullandırmada daha kırılgan olabileceğini göstermektedir. Gerçek veri (California Housing) üzerinde standardizasyonun \(cond(X^T X)\) değerini \(5.76\times 10^{10}\) seviyesinden \(44.95\)’e düşürdüğü; tüm çözücülerin benzer RMSE üretirken GD’nin çalışma süresi açısından belirgin şekilde daha maliyetli olduğu bulunmuştur.

---

# GİRİŞ
En küçük kareler yöntemi; ölçüm hataları içeren verilerden parametre kestirimi, model kalibrasyonu ve regresyon gibi birçok mühendislik ve bilim probleminde temel bir araçtır. Doğrusal regresyon özelinde hedef; gözlemler ile model çıktısı arasındaki karesel hatayı minimize eden parametreleri bulmaktır. Bu problem teorik olarak basit görünse de pratikte **sayısal kararlılık (numerical stability)** ve **koşullanma (conditioning)** nedeniyle çözüm kalitesi ciddi biçimde etkilenebilir. Özellikle özellikler arası **kolinearite** veya ölçek farklılıkları \(X^T X\) matrisinin koşul sayısını büyüterek küçük sayısal hataların çözümde büyümesine yol açabilir [1], [2].

Literatürde en küçük kareler problemi; normal denklemler, QR ayrıştırması ve tekil değer ayrıştırması (SVD) gibi farklı yaklaşımlarla ele alınır. Genel kabul, **açık ters alma** işleminin sayısal olarak riskli olduğu; bunun yerine doğrusal sistem çözücüleri veya QR/SVD tabanlı yöntemlerin tercih edilmesi gerektiğidir [1], [2]. Öte yandan büyük ölçekli problemlerde kapalı form çözümler yerine gradyan tabanlı optimizasyon yöntemleri (örn. GD) sıkça kullanılmaktadır [3]. Bu yöntemlerde adım büyüklüğü seçimi ve yakınsama davranışı doğrudan performansı belirler.

Bu projede amaç; (i) normal denklem tabanlı farklı çözümleri (inverse/solve/QR) ve (ii) iteratif GD yaklaşımını **doğruluk, kararlılık ve çalışma süresi** açısından karşılaştırmaktır. Ek olarak (iii) kötü koşullanma senaryoları sentetik veri ile kontrollü biçimde üretilmiş ve (iv) analitik gradyanın doğruluğu gradient checking ile incelenmiştir. Böylece “hangi yöntemin hangi koşullarda daha uygun olduğu” deneysel olarak tartışılabilir hale getirilmiştir.

---

# YÖNTEM
## Problemin Matematiksel Modeli
Doğrusal regresyonun en küçük kareler formülasyonu:

\[
\min_{\theta\in\mathbb{R}^d} J(\theta) = \frac{1}{2n}\sum_{i=1}^{n} (x_i^T\theta - y_i)^2
= \frac{1}{2n}\lVert X\theta - y\rVert_2^2
\]

Burada \(X\in\mathbb{R}^{n\times d}\) tasarım matrisi (bias sütunu dahil), \(y\in\mathbb{R}^n\) hedef vektörüdür.

## Normal Denklem ve Kapalı Form Çözümler
Türevi sıfıra eşitleyerek:

\[
\nabla J(\theta)=\frac{1}{n}X^T(X\theta-y)=0 \quad\Rightarrow\quad X^T X\theta = X^T y
\]

Bu doğrusal sistem farklı yollarla çözülebilir:
- **Inverse (açık ters alma):** \(\theta = (X^T X)^{-1}X^T y\)  
  Sayısal kararlılık açısından genelde **önerilmez** (ters alma, hataları büyütebilir) [2].
- **Solve (doğrusal sistem çözümü):** \((X^T X)\theta = X^T y\) sistemi doğrudan çözücü ile çözülür.
- **QR tabanlı least squares:** \(X=QR\) (Q ortonormal, R üst üçgensel) ile

  \[
  \min_\theta\lVert X\theta-y\rVert_2 \Rightarrow R\theta = Q^T y
  \]

  QR, özellikle kötü koşullandırmada daha güvenilir kabul edilir [1].

## Koşullanma (Condition Number) ve Etkisi
Bir matrisin 2-norm koşul sayısı:

\[
cond(A)=\lVert A\rVert_2\lVert A^{-1}\rVert_2
\]

Koşul sayısı büyüdükçe, girdideki küçük sayısal hatalar çözümde büyüyebilir. Ayrıca 2-norm altında yaklaşık olarak \(cond(X^T X)\approx cond(X)^2\) ilişkisinin oluşması normal denklemleri daha hassas hale getirebilir [1], [2].

## Gradient Descent (GD)
GD, maliyet fonksiyonunu iteratif minimize eder:

\[
\theta^{(k+1)}=\theta^{(k)}-\alpha \nabla J(\theta^{(k)})
\]

Analitik gradyan:

\[
\nabla J(\theta)=\frac{1}{n}X^T(X\theta-y)
\]

Durdurma ölçütü olarak; göreli kayıp değişimi veya gradyan normu eşiği kullanılabilir.

## Standardizasyon (Ölçekleme)
Uygulamada (bias sütunu korunarak) özellikler standardize edilir:

\[
x_j \leftarrow \frac{x_j-\mu_j}{\sigma_j}
\]

Bu adım, koşul sayısını düşürerek hem kapalı form çözümlerde hem GD’de sayısal davranışı iyileştirebilir.

## Gradient Checking (Merkez Fark)
Analitik gradyanın doğruluğunu denetlemek için merkez fark yaklaşımı:

\[
\frac{\partial J}{\partial \theta_i} \approx \frac{J(\theta+\varepsilon e_i)-J(\theta-\varepsilon e_i)}{2\varepsilon}
\]

Epsilon çok büyük seçilirse yaklaşım hatası (truncation), çok küçük seçilirse yuvarlama hatası (round-off) baskın hale gelir; bu nedenle göreli hata tipik olarak “U-şekilli” davranış gösterebilir [2].

## Akış (Algoritmik Adımlar)
Aşağıdaki adımlar raporda Word’de akış diyagramına dönüştürülebilir:
1. Veri yükle/üret → train/val ayır
2. (Opsiyonel) Standardize et
3. Çözücü seç: inverse / solve / QR / GD
4. \(\theta\) hesapla
5. Tahmin yap: \(\hat{y}=X\theta\)
6. Metrikleri hesapla: RMSE, \(cond(X^T X)\), iterasyon vb.
7. Grafik/tabloları üret ve kaydet
8. Testleri çalıştır

## Karmaşıklık Analizi (Big-O)
- **Normal denklemler:** \(X^T X\) oluşturma \(O(nd^2)\), çözümleme \(O(d^3)\)
- **QR (genel):** yaklaşık \(O(nd^2)\)
- **GD:** her iterasyon \(O(nd)\), toplam \(O(knd)\) (k: iterasyon sayısı)
- **Standardizasyon:** \(O(nd)\)

## Kullanılan Teknolojiler
Python ekosisteminde:
- NumPy (vektörleştirilmiş lineer cebir)
- Pandas (tablo/CSV)
- Matplotlib & Seaborn (grafikler)
- scikit-learn (gerçek veri seti; erişim olmazsa fallback)

---

# UYGULAMA
Bu projede tüm uygulama tek bir Colab/Notebook akışı olarak tasarlanmıştır. Üretilen figürler `outputs/figures/`, tablolar `outputs/tables/` klasörlerine kaydedilecek şekilde düzenlenmiştir.

## Veri Setleri
### Sentetik Veri
Sentetik doğrusal veri üretiminde:
- Bias sütunu eklenmiş tasarım matrisi oluşturulmuştur.
- Kolinearite kontrolü için ikinci özellik yaklaşık olarak birinci özelliğin kopyası yapılmış ve aradaki fark \(10^{-p}\) ile ölçeklenerek \(p\) arttıkça kolinearite yükseltilmiştir.
- Böylece koşullanma kontrollü biçimde büyütülerek yöntemlerin kırılganlığı ölçülmüştür.

### Gerçek Veri
California Housing veri seti kullanılmıştır; veri indirilemezse Diabetes veri setine düşen bir “fallback” akışı mevcuttur. Ham veri üzerinde \(cond(X^T X)\) çok büyük çıkabildiği için standardizasyon uygulanmış ve etkisi raporlanmıştır.

## Metrikler ve Değerlendirme
- **RMSE:** doğruluk ölçütü
- **Koşul sayısı:** \(cond(X)\), \(cond(X^T X)\)
- **Yakınsama:** GD için loss ve \(\|\nabla J\|\) eğrileri
- **Performans:** çalışma süresi (runtime) ve ölçekleme analizi (n ve d’ye göre)

---

# DENEYSEL SONUÇLAR
Bu bölümde tablolar/şekiller metin içerisinde yorumlanmıştır. Tüm sayısal sonuçlar notebook çalıştırılarak yeniden üretilebilir.

## 1) Sentetik veri – baz senaryo (n=2000, d=20, p=6)
**Tablo 1.** Yöntemlere göre doğruluk (validation RMSE)

| Yöntem | Val RMSE |
|---|---:|
| inverse | 0.5003108201 |
| solve | 0.5002656534 |
| qr_lstsq | 0.5002657606 |
| qr_explicit | 0.5002657606 |
| gd (standardize) | 0.5000206703 |

**Yorum:** Kapalı form yöntemlerde `solve` ve QR tabanlı çözümler neredeyse aynı RMSE değerini üretmektedir. Açık ters alma (`inverse`) çok küçük bir farkla daha kötü sonuç vermiştir; bu fark, ters alma işleminin sayısal hataları büyütebilmesiyle uyumludur. GD ise standardizasyon sonrası benzer doğruluk seviyesine ulaşabilmiş, ancak iterasyon ve süre maliyeti nedeniyle kapalı form çözümlere göre daha pahalıdır.

## 2) GD yakınsaması
**Şekil (yerleştirilecek):** `outputs/figures/gd_history.png`  
**Yorum:** Loss eğrisinin düşmesi ve \(\|\nabla J\|\) normunun azalması, GD’nin beklenen şekilde yakınsadığını gösterir. Yakınsama hızı adım büyüklüğü \(\alpha\) ve standardizasyondan güçlü biçimde etkilenmektedir.

## 3) Koşullanma deneyi (p taraması)
**Şekil (yerleştirilecek):**
- `outputs/figures/cond_vs_rmse.png`
- `outputs/figures/p_vs_cond.png`
- `outputs/figures/p_vs_rmse.png`

**Yorum:** \(p\) arttıkça özellikler daha kolinear hale gelmekte ve \(cond(X^T X)\) yükselmektedir. Bu durumda normal denklemlerde sayısal hataların büyümesi beklenir. Grafikler, koşullanma büyüdükçe bazı çözücülerin hata duyarlılığının arttığını gözlemlemeyi sağlar. Özellikle açık ters alma yaklaşımı teorik olarak en kırılgan adaydır [2].

## 4) Gradient checking — epsilon taraması
**Şekil (yerleştirilecek):** `outputs/figures/epsilon_sweep.png`  
**Yorum:** Göreli hata, epsilon çok küçükken yuvarlama hatası nedeniyle büyür; epsilon çok büyükken yaklaşım hatası baskın hale gelir. Float32’nin makine epsilon’u daha büyük olduğundan optimum epsilon aralığı float64’e göre daha “kaba” bir bölgede oluşur.

## 5) Runtime ölçekleme (solve vs GD)
**Tablo 2.** n arttıkça runtime (s)

| n | solve (s) | gd (s) |
|---:|---:|---:|
| 1000 | 0.000067 | 0.005169 |
| 5000 | 0.000166 | 0.021330 |
| 10000 | 0.000242 | 0.034118 |
| 20000 | 0.000423 | 0.060054 |
| 50000 | 0.001029 | 0.123622 |

**Tablo 3.** d arttıkça runtime (s)

| d | solve (s) | gd (s) |
|---:|---:|---:|
| 10 | 0.000072 | 0.005821 |
| 50 | 0.000186 | 0.012625 |
| 100 | 0.000481 | 0.022056 |
| 200 | 0.001415 | 0.038875 |
| 500 | 0.003841 | 0.124917 |

**Yorum:** `solve` yöntemi küçük/orta boyutlarda son derece hızlıdır; GD ise iteratif yapısı nedeniyle belirgin biçimde daha uzun sürmektedir. n veya d büyüdükçe GD’nin maliyeti yaklaşık olarak \(O(knd)\) davranışıyla artar; `solve` tarafında ise d büyüdükçe kübik terim \(O(d^3)\) daha görünür hale gelir (tabloda d=500’de solve süresinin artması bu beklentiyle uyumludur).

## 6) Gerçek veri (California Housing)
Ham veri üzerinde:
- \(cond(X^T X)\) (raw) = **57584282139.84404**
- \(cond(X^T X)\) (standardized) = **44.94809183102631**

**Tablo 4.** Gerçek veri metrikleri

| Yöntem | Train RMSE | Val RMSE | Runtime (s) | GD iter |
|---|---:|---:|---:|---:|
| solve | 0.724133 | 0.724508 | 0.000190 | — |
| qr_lstsq | 0.724133 | 0.724508 | 0.000842 | — |
| qr_explicit | 0.724133 | 0.724508 | 0.001693 | — |
| gd | 0.724263 | 0.723957 | 0.368939 | 4999 |

**Yorum:** Standardizasyonun koşul sayısını dramatik biçimde düşürmesi, modelin sayısal açıdan “çözülebilirliğini” artırmıştır. Doğruluk açısından yöntemler benzer RMSE değerleri üretirken GD’nin çalışma süresi kapalı form yöntemlere kıyasla çok daha yüksektir. Bu bulgu, orta boyutlu problemlerde `solve/QR` kullanımının pratikte daha avantajlı olabileceğine işaret eder.

---

# TARTIŞMA
Bu projede elde edilen bulgular, en küçük kareler probleminin çözümünde yöntem seçiminin **problem ölçeği** ve özellikle **koşullanma** ile doğrudan ilişkili olduğunu göstermektedir. Sentetik veri deneylerinde kolinearite şiddeti arttıkça \(cond(X^T X)\) büyümekte ve bu durum normal denklem tabanlı çözümlerde sayısal hassasiyeti zorlayabilmektedir. Teorik olarak \(cond(X^T X)\approx cond(X)^2\) ilişkisinin etkisiyle, normal denklemler üzerinden çözüm almak kötü koşullandırılmış durumlarda daha kırılgan hale gelebilir. Bu nedenle ters alma yaklaşımının (inverse) pratikte riskli olması beklenir; daha güvenilir alternatifler olarak doğrusal sistem çözümü (`solve`) veya doğrudan least squares/QR tabanlı yöntemler öne çıkar [1], [2].

GD’nin (batch gradient descent) avantajı; kapalı form çözümlerin hesaplanmasının pahalılaştığı veya verinin akış halinde geldiği senaryolarda iteratif biçimde çözüm üretebilmesidir. Ancak bu projede görüldüğü üzere GD’nin maliyeti, iterasyon sayısına bağlı olduğundan küçük/orta boyutlarda kapalı form çözümlere kıyasla belirgin biçimde daha yüksek olabilmektedir. Ayrıca GD’nin başarımı; adım büyüklüğü \(\alpha\), durdurma kriteri ve özellikle ölçekleme/standardizasyon gibi ön işlemlerden etkilenir [3]. Bu nedenle GD, “her durumda daha iyi” değil; uygun koşullarda ve doğru ayarlarla anlamlı bir alternatiftir.

Gradient checking deneyi, analitik gradyanın doğrulanması açısından pratikte çok yararlı olmakla birlikte, epsilon seçiminin kritik olduğunu ortaya koymaktadır. Epsilon çok küçük olduğunda yuvarlama hatası; çok büyük olduğunda yaklaşım hatası baskın hale gelir. Bu nedenle göreli hata genellikle “orta” bir epsilon aralığında minimuma iner. Ayrıca float32’nin daha sınırlı hassasiyetinden dolayı float64’e kıyasla daha yüksek bir hata tabanı görülmesi beklenir. Bu bulgu, özellikle optimizasyon tabanlı yöntemlerde (GD gibi) dtype seçiminin ve sayısal hassasiyetin önemini vurgular.

Gerçek veri deneyinde standardizasyonun \(cond(X^T X)\) değerini çok büyük bir seviyeden (yaklaşık \(5.76\times 10^{10}\)) küçük bir seviyeye (yaklaşık \(44.95\)) indirmesi, koşullanma probleminin pratikte ne kadar etkili olabileceğini göstermektedir. Standardizasyon sonrası kapalı form çözümlerle GD’nin RMSE açısından benzer sonuçlar üretmesi, problemi iyi koşullandırmanın çözüm yönteminden bağımsız olarak doğruluğu stabilize edebileceğini göstermektedir. Öte yandan GD’nin çalışma süresi maliyeti, bu veri ölçeğinde kapalı form yöntemlere göre daha yüksek kalmıştır.

Bu çalışmanın sınırlılıklarından biri; SVD tabanlı en küçük kareler çözümünün ayrı bir yöntem olarak karşılaştırmaya dahil edilmemiş olmasıdır. Ayrıca GD tarafında momentum/Adam gibi hızlandırılmış optimizasyon teknikleri kullanılmamıştır. Buna rağmen, temel yöntemlerin (inverse/solve/QR/GD) ve koşullanma–hassasiyet ilişkilerinin aynı çerçevede gösterilmesi, raporun ana hedefi olan nümerik analiz perspektifini karşılamaktadır.

---

# TEST SÜREÇLERİ
Bu projede yazılımın doğrulanması ve hatalardan arındırılması için aşağıdaki test yaklaşımı izlenmiştir.

- **Birim testleri (unit tests)**  
  Kod içerisinde `run_tests()` fonksiyonu aracılığıyla iki temel doğrulama yapılmıştır:  
  1. **Çözücü tutarlılığı testi:** Rastgele üretilmiş sentetik veri üzerinde `normal_eq_solve` ile QR tabanlı çözümün (`np.linalg.lstsq`) aynı parametre vektörünü (sayısal tolerans içinde) üretmesi beklenir. Bu amaçla `np.allclose(..., atol=1e-6)` ile eşdeğerlik kontrol edilmiştir.  
  2. **Gradient checking testi:** Analitik gradyan ile merkez farktan elde edilen sayısal gradyan arasındaki göreli hatanın belirli bir eşik değerinin altında olması beklenir. Bu testte örnek bir epsilon seçimi için göreli hata `relerr < 1e-5` koşulu ile doğrulanmıştır.

- **Tekrarlanabilirlik (reproducibility)**  
  Deneylerde sabit bir `seed` kullanılarak (ör. `SEED=42`) sentetik veri üretimi ve eğitim/doğrulama ayrımı tekrarlandığında aynı sonuçların elde edilmesi hedeflenmiştir. Ayrıca kütüphane sürümleri JSON olarak kaydedilerek ortam bağımlılığının izlenmesi sağlanmıştır.

- **Hata yakalama ve güvenli başarısız olma (fail-safe)**  
  Normal denklem çözümlerinde ters alma veya doğrusal sistem çözümü bazı sayısal durumlarda hata verebileceğinden, ilgili fonksiyonlar `try/except` yapısı ile korunmuştur. Hata durumunda uyarı mesajı üretilmiş ve sonuç vektörü NaN ile doldurularak deney akışının tamamen durması engellenmiştir.

- **Veri seti yükleme dayanıklılığı**  
  Gerçek veri deneyinde California Housing verisi indirilemezse otomatik olarak Diabetes veri setine düşen (fallback) bir akış tasarlanmıştır. Bu sayede internet/izin kısıtı gibi dış etkenlerde dahi deneyin çalışabilir kalması amaçlanmıştır.

> Not: Eğer rapora “ekran görüntüsü” istenirse, notebook’taki “Tests passed.” çıktısının ekran görüntüsü Word’e eklenebilir.

---

# SONUÇ VE ÖNERİLER
Bu projede en küçük kareler regresyon probleminin çözümünde normal denklem tabanlı yaklaşımlar ile GD tabanlı yaklaşım, doğruluk–kararlılık–performans açısından karşılaştırılmıştır. Elde edilen sonuçlar aşağıdaki şekilde özetlenebilir:

- **Kapalı form çözümlerde öneri:**  
  Pratikte açık ters alma (`inverse`) yerine `solve` veya QR tabanlı least squares çözümleri tercih edilmelidir. Bu seçim, sayısal kararlılığı artırır ve genellikle daha güvenilir sonuçlar üretir [1], [2].

- **Koşullanma ve ölçekleme:**  
  Özellik standardizasyonu, \(cond(X^T X)\) değerini dramatik biçimde düşürerek hem kapalı form çözümlerde hem GD’de daha stabil ve tutarlı sonuçlar elde edilmesini sağlar. Gerçek veri deneyinde standardizasyonun etkisi açıkça gözlenmiştir.

- **GD kullanımı için öneri:**  
  GD, özellikle büyük ölçekli problemlerde veya çevrimiçi/akış verilerinde uygun bir seçenek olabilir; ancak iterasyon maliyeti, hiperparametre seçimi ve yakınsama takibi nedeniyle dikkatli ayar gerektirir [3]. Bu proje bağlamında küçük/orta ölçeklerde kapalı form yöntemler daha verimli görünmüştür.

- **Gradient checking çıktısı:**  
  Analitik gradyanın doğrulanması, optimizasyon tabanlı yöntemlerin güvenilirliği için kritik bir adımdır. Epsilon seçimi ve dtype (float64 vs float32) gradient checking kalitesini belirgin biçimde etkiler.

**Geliştirme önerileri (gelecek çalışma):**
- Ridge (L2) regularization eklenerek kötü koşullandırmada çözümün stabilitesi artırılabilir.
- SVD tabanlı least squares çözümü de karşılaştırmaya eklenebilir.
- GD için momentum/Adam gibi hızlandırma teknikleri denenebilir.
- Parametre taraması (grid search) ile \(\alpha\) ve durdurma ölçütlerinin etkisi sistematik incelenebilir.

---

# KAYNAKÇA (IEEE)
[1] G. H. Golub and C. F. Van Loan, *Matrix Computations*, 4th ed. Baltimore, MD, USA: Johns Hopkins University Press, 2013.  
[2] N. J. Higham, *Accuracy and Stability of Numerical Algorithms*, 2nd ed. Philadelphia, PA, USA: SIAM, 2002.  
[3] J. Nocedal and S. J. Wright, *Numerical Optimization*, 2nd ed. New York, NY, USA: Springer, 2006.

---

# Markdown → Word’e Aktarım Notları (pratik)
- **Başlık hiyerarşisi:** Word’de “Heading 1/2/3” stillerini kullan (Kapak/Özet/Giriş/… ana başlıklar Heading 1).
- **Denklemler:** Word: *Insert → Equation* ile denklemleri yaz; Word çoğu LaTeX ifadesini kabul ediyor.
- **Şekil/Tablo numarası:** *References → Insert Caption* ile “Şekil 1”, “Tablo 1” üret; metin içinde mutlaka “Şekil 2’de…” diye yorumla.
- **Özet kuralı:** Özet 200–250 kelime olsun ve **atıf/kaynak referansı içermesin**.
- **IEEE atıf düzeni:** Metinde `[1]`, `[2]`, `[3]` şeklinde numaralı atıf; Kaynakça’da aynı numaralarla liste.
