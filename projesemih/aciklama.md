# Proje Açıklaması (Ders Anlatımı Formatı)

Bu dosya, `numerikproje/projesemih/notebooks/colab_template.ipynb` notebook’unu
ders anlatır gibi adım adım açıklamak için hazırlanmıştır. Hedef; kodun ne yaptığını,
hangi matematiksel temele dayandığını ve çıkan sonuçların nasıl yorumlanacağını
net ve anlaşılır şekilde göstermektir.

## 0) Bu dokümanı nasıl okumalı?
Önerilen sıra:
1) Problemin matematiksel tanımı (ne çözüyoruz?)
2) Kullanılan yöntemler (normal denklem, QR, GD)
3) Nümerik analiz kısmı (koşullanma, hata türleri)
4) Deneyler ve grafikler (hangi çıktı neyi gösteriyor?)
5) Raporla bağlama (hangi tablo/figür nerede kullanılır?)

## 0.1) Temel kavramlar (hiç bilmeyenler için kısa sözlük)
- **Özellik (feature):** X matrisindeki her sütun. Model bu sütunlardan bilgi alır.
- **Hedef (target):** y vektörü. Tahmin etmeye çalıştığımız gerçek değerler.
- **Parametreler (θ):** Modelin öğrenmesi gereken katsayılar.
- **Tahmin (y_hat):** Modelin ürettiği çıktı; `y_hat = Xθ`.
- **Hata (residual):** `r = Xθ - y`. Modelin ne kadar yanıldığını gösterir.
- **Kayıp (loss):** Hatanın tek bir sayıya özetlenmiş hali (bu projede MSE).

## 0.2) Notasyon ve boyutlar
Bu projede kullanılan boyutlar şu şekildedir:
- `X`: `(n, d+1)` boyutunda (ilk sütun bias).
- `θ`: `(d+1,)` boyutunda.
- `y`: `(n,)` boyutunda.
- `Xθ`: `(n,)` boyutunda tahmin.

Bias sütunu eklenince model şu hale gelir:
```
y_hat = θ0 + θ1 x1 + θ2 x2 + ... + θd xd
```
Burada `θ0` bias (sabit terim) katsayısıdır.

## 0.3) Bu projede hangi sorular cevaplanıyor?
1) **Normal denklem** ve **GD** aynı problemi çözüyor mu, doğrulukları benzer mi?
2) **Koşullanma** büyüdükçe hangi yöntemler bozuluyor?
3) **Gradyan hesapları doğru mu?** (Gradient checking ile doğrulama)

Bu üç soru, dersin “nümerik analiz” yönünü doğrudan ölçüyor.

## 1) Problemin matematiksel temeli
Amaç fonksiyonu:
```
J(θ) = (1 / 2n) * ||Xθ - y||^2
```
Burada:
- `X` veri matrisi (n satır, d özellik)
- `θ` parametre vektörü
- `y` hedef vektörü

Modelin ürettiği tahmin:
```
y_hat = Xθ
```
Bu nedenle hata (residual) şu şekilde tanımlanır:
```
r = Xθ - y
```
Kayıp fonksiyonu ise bu hatanın karesinin ortalamasıdır.

Neden `1 / 2n` var?
- Türevi sadeleştirir (2 katsayısı gider).
- Ölçekleme sağlar (n büyüdükçe loss büyümesin).

Bias (sabit terim) neden eklenir?
- Modelin orijinden geçmeye zorlanmasını engeller.
- Gerçek veri çoğu zaman sabit kayma (offset) içerir.
- Kodda bu, `X` matrisinin başına 1’ler sütunu eklenerek yapılır.

## 2) Analitik gradyan ve normal denklem
Gradyan:
```
∇J(θ) = (1 / n) * X^T (Xθ - y)
```
Optimum koşulu:
```
∇J(θ)=0  =>  X^T X θ = X^T y
```
Bu, lineer sistem çözümüdür.

Kısa türetim (sezgisel):
1) `J(θ)` bir kuadratik fonksiyondur.
2) Kuadratik fonksiyonun minimumu, gradyanın sıfır olduğu noktadadır.
3) Bu da bizi `X^T X θ = X^T y` denklemine götürür.

Not: `X^T X` matrisi, `X`’in koşul sayısını yaklaşık olarak **karesine** çıkarır:
```
cond(X^T X) ≈ cond(X)^2
```
Bu yüzden normal denklem sayısal olarak kırılgan hale gelebilir.

Notebook’ta bu denklemi çözen yöntemler:
- `normal_eq_inverse`: `(X^T X)^-1 X^T y` (bilerek kötü pratik)
- `normal_eq_solve`: `solve(X^T X, X^T y)` (önerilen)
- `least_squares_qr`: `np.linalg.lstsq` (stabil baseline)
- `least_squares_explicit_qr`: QR ayrışımını açıkça uygular

Neden inverse kötü pratik?
- `X^T X` koşul sayısını büyütür.
- Ters alma, yuvarlama hatalarını büyütür.
- Tekillik durumunda patlama riski vardır.

## 3) Gradient Descent (GD) mantığı
GD güncellemesi:
```
θ_{k+1} = θ_k - α * ∇J(θ_k)
```
Burada:
- `α` öğrenme oranı (adım büyüklüğü)
- `∇J(θ_k)` analitik gradyan

GD’nin iki kritik riski:
- **α çok küçükse:** çok yavaş öğrenir.
- **α çok büyükse:** sapar (diverge eder).

Bu nedenle notebook’ta **alpha sweep** yapılır ve en iyi α seçilir.

GD neden önemli?
- Büyük veri setlerinde kapalı form çözümler pahalı olabilir.
- Iteratif yöntemler, bellek ve hesaplama açısından esnek olabilir.

GD’de takip ettiğimiz metrikler:
- `loss` (J(θ)) azalıyor mu?
- `grad_norm` (||∇J||) düşüyor mu?
- `iter` sayısı (kaç adımda duruyor?)

## 4) Nümerik analiz odağı: koşullanma
Koşullanma nedir?
- Küçük bir girdi hatasının çıktıda ne kadar büyüdüğünü gösterir.
- `cond(X^T X)` büyüdükçe problem sayısal olarak “zor” hale gelir.

Koşul sayısı, en büyük ve en küçük tekil değerlerin oranıdır:
```
cond(X) = σ_max / σ_min
```
`σ_min` çok küçükse, sistem tekile yaklaşır ve çözüm kararsız hale gelir.

Sentetik veri ile koşullanmayı artırma:
```
x2 = x1 + 10^{-p} * ξ
```
`p` büyüdükçe `x1` ve `x2` daha kolinear olur, `cond(X^T X)` büyür.

Notebook’ta iki koşul sayısı hesaplanır:
- `cond_xtx`: ham veri
- `cond_xtx_std`: standardize edilmiş veri

Neden `cond_xtx_std` ekledik?
- Standardizasyon, GD’nin yakınsamasını iyileştirir.
- Koşul sayısındaki iyileşme görsel olarak raporlanabilir.

## 5) Standardizasyonun önemi (bias hariç)
Standardizasyon:
```
X_std = (X - mean) / std
```
Ama bias sütunu standartlaştırılmaz.

Neden?
- Bias sütunu sabittir (std = 0).
- Standardize edilirse sıfıra bölme hatası oluşur.

Bu yüzden kodda:
- İlk sütun (bias) korunur.
- Sadece özellikler ölçeklenir.

Adil karşılaştırma için önemli nokta:
- GD standardize edilmiş uzayda çalışır.
- Normal denklem çözümleri ham uzayda çalışırsa kıyas adil olmaz.
- Bu yüzden koşullanma tablosuna `cond_xtx_std` de eklenmiştir.

## 6) Gradient checking (sayısal türev)
Merkezi fark:
```
∂J/∂θ_i ≈ [J(θ + ε e_i) - J(θ - ε e_i)] / (2ε)
```
Bu yöntem:
- Truncation hatası: O(ε^2)
- Yuvarlama hatası: ε çok küçülünce baskın olur

Notebook’ta:
- `epsilon_sweep` ile ε = 10^-1 ... 10^-10 taranır.
- float64 ve float32 ayrı çizilir.

Yorum:
- Büyük ε → kesme hatası baskın
- Çok küçük ε → yuvarlama hatası baskın
- float32, hata tabanını daha erken gösterir

Bu bölüm, “sayısal türevler” konusunu doğrudan uyguladığı için raporun
nümerik analiz kısmında güçlü bir kanıttır.

## 7) Alpha sweep (öğrenme oranı seçimi)
GD’nin başarısı α seçimine çok duyarlıdır.
Bu yüzden:
- `alpha_sweep_gd` ile farklı α değerleri denenir.
- En düşük val RMSE veren α seçilir.
- `GD_ALPHA` olarak kaydedilir.

Bu adım, “GD sonucu keyfi α’ya bağlı” eleştirisini önler.

## 8) Deneyler ve hücreler ne yapıyor?
Notebook’un ana deneyleri:

1) **Alpha sweep**
- Çıktı: `alpha_sweep.csv`, `alpha_sweep.png`
- Amaç: GD için en iyi α’yı seçmek

2) **GD yakınsama grafiği**
- Çıktı: `gd_history.png`
- Amaç: loss ve grad_norm’un düşüşünü görmek

3) **Koşullanma taraması (p sweep)**
- Çıktı: `conditioning_table.csv`
- Grafikler: `cond_vs_rmse.png`, `p_vs_cond.png`, `p_vs_rmse.png`
- Amaç: ill‑conditioning arttıkça hangi yöntemin bozulduğunu göstermek

4) **Gradient checking (epsilon sweep)**
- Çıktı: `epsilon_sweep.csv`, `epsilon_sweep.png`
- Amaç: analitik gradyanı doğrulamak, truncation/rounding davranışı göstermek

5) **Runtime ölçekleme (n ve d)**
- Çıktı: `runtime_n.csv`, `runtime_d.csv`
- Grafikler: `runtime_n.png`, `runtime_d.png`
- Amaç: Big‑O teorisini pratikte görmek

6) **Gerçek veri deneyi**
- Çıktı: `realdata_metrics.csv`
- Grafikler: `realdata_metrics.png`, `realdata_gd_history.png`
- Amaç: gerçek veride yöntemlerin davranışını görmek

7) **Özet hücresi**
- Çıktı: `summary_metrics.csv`
- Rapor ve sunum için tek satırlık özet

Ek not:
- Bu CSV’ler raporda “sayısal kanıt” olarak kullanılır.
- Tekrar üretilebilirlik için tüm değerler seed’e bağlıdır.

## 9) Çıktıları nasıl yorumlamalı?
Grafik yorumlama rehberi:
- `cond_vs_rmse.png`: koşul sayısı büyüdükçe inverse bozulur mu?
- `p_vs_rmse.png`: p artarken hangi yöntem stabil kalıyor?
- `gd_history.png`: loss düzgün azalıyor mu?
- `epsilon_sweep.png`: U‑şekli var mı? float32 tabanı görünüyor mu?
- `runtime_n.png`, `runtime_d.png`: solve vs GD hız farkı net mi?

Yorum örnekleri:
- Eğer `cond_vs_rmse` grafiğinde inverse sapıyorsa, bu “kötü pratik” hipotezini doğrular.
- `gd_history` grafiğinde loss düzleşiyorsa, yakınsama gerçekleşmiş demektir.
- `epsilon_sweep` grafiğinde float32 eğrisi yukarıda kalıyorsa, yuvarlama hatası baskındır.

Tabloları raporda kullanma:
- `conditioning_table.csv`: yöntem karşılaştırma tablosu
- `alpha_sweep.csv`: GD parametre seçimi gerekçesi
- `summary_metrics.csv`: özet sayılar

## 10) Raporla bağlama (Overleaf)
Rapor dosyası:
- `numerikproje/projesemih/overleaf.txt`

Rapor bölümlerinde kullanacağın temel kaynaklar:
- Deneysel sonuçlar: `outputs/figures/*.png`
- Özet sayılar: `outputs/tables/*.csv`
- Koşullanma tartışması: `cond_vs_rmse.png` ve `p_vs_cond.png`
- Gradient checking tartışması: `epsilon_sweep.png`

Rapor yazarken öneri:
- Grafik altlarına mutlaka yorum yaz.
- “Bu grafikten ne çıkarıyorum?” cümlesi ekle.

## 11) Sık karşılaşılan sorunlar
1) Çıktılar yanlış klasöre gidiyor.
- Notebook içinde `OUTPUT_DIR` ve `TABLE_DIR` otomatik belirlenir.
- `notebooks` altından çalıştırırsan üst klasöre çıkar.

2) California Housing indirilemedi.
- Notebook otomatik olarak Diabetes datasetine düşer.

3) GD sonuçları kötü çıktı.
- `alpha_sweep` ile yeni α seç.
- Standardizasyonun aktif olduğundan emin ol.

4) inverse yöntemi hata veriyor.
- Bu beklenen bir durumdur (tekillik).
- Notebook NaN raporlar, raporda “inverse kırılgan” diye açıklanır.

## 12) Çalıştırma önerisi
Notebook’u “Run all” yap.
Sonunda:
- `outputs/figures` ve `outputs/tables` dolu olmalı.
- Test hücresi “Tests passed.” yazmalı.

Lokal çalışma için:
```
pip install -r requirements.txt
jupyter notebook notebooks
```
Colab için:
- Notebook’u yükle, üstten “Runtime → Run all” seç.

## 13) Projenin “nümerik analiz” vurgusu nerede?
- Koşullanma analizi (cond)
- İnverse vs solve farkı
- QR stabilitesi
- Central difference ile gradient checking
- Truncation vs rounding hatası

Bu başlıklar, dersin numerik analiz içeriğiyle birebir örtüşür.

---
## 14) Mini sayısal örnek (elle hesap)
Hiç bilmeyen biri için en küçük örnekle düşünelim.  
Tek bir özellik (`x`) ve bias eklenmiş model:
```
y_hat = θ0 + θ1 * x
```
Örnek veri:
```
x = [1, 2, 3]
y = [2, 3, 5]
```
Bias eklenmiş X matrisi:
```
X = [[1, 1],
     [1, 2],
     [1, 3]]
```

**Normal denklem:**
```
X^T X = [[3, 6],
         [6, 14]]

X^T y = [10, 23]
```
Çözüm:
```
θ = (X^T X)^-1 X^T y
```
2x2 ters ile:
```
det = 3*14 - 6*6 = 6
θ0 = (14*10 - 6*23)/6 = 2/6 = 0.333...
θ1 = (-6*10 + 3*23)/6 = 9/6 = 1.5
```
Yani:
```
θ0 ≈ 0.333,  θ1 = 1.5
```
Tahminler:
```
x=1 -> y_hat=1.833
x=2 -> y_hat=3.333
x=3 -> y_hat=4.833
```
Hatalar küçük olduğu için RMSE düşük çıkar.

**GD’nin ilk adımı (θ=0 başlangıç):**
```
grad = (1/3) * X^T (Xθ - y)
     = (1/3) * X^T ( -y )
     = -(1/3) * [10, 23]
     = [-3.333, -7.667]
```
Eğer α = 0.1 ise:
```
θ1 = θ0 - α * grad = [0,0] - 0.1 * [-3.333, -7.667]
   = [0.333, 0.767]
```
GD böyle adım adım optimuma yaklaşır.

Bu küçük örnek, notebook’ta yaptığımız işlemlerin
“büyük veri” için aynısının vektör-matris formu olduğunu gösterir.

---

## 15) Sık sorulan sorular (SSS)
**S: Bias neden şart?**  
C: Bias olmazsa model orijinden geçmeye zorlanır. Gerçek veride bu yanlış sonuç verir.

**S: Neden `solve` tercih ediliyor?**  
C: Inverse, sayısal hatayı büyütür. `solve`, daha stabil faktorizasyon kullanır.

**S: Koşullanma büyüyünce ne olur?**  
C: Küçük sayısal hatalar büyük parametre hatalarına dönüşür. Bu yüzden inverse bozulur.

**S: GD neden yavaş?**  
C: Her iterasyon O(nd). Kapalı form küçük/orta boyutta genelde daha hızlıdır.

**S: float32 neden daha kötü?**  
C: Hassasiyet daha düşük olduğu için rounding hatası erken baskın olur.

**S: Alpha sweep neden gerekli?**  
C: GD’nin sonucu α’ya çok duyarlıdır. Tek α seçimi “keyfi” görünür.

---
Bu dosya “ders anlatır gibi” yazıldı. Bir hücreyi veya sonucu beraber
incelemek istersen, hangi kısmı konuşmak istediğini söylemen yeterli.

---

# Ek A — Hücre Hücre Ders Anlatımı

Bu bölüm, notebook’u hücre hücre anlatır. Hedef: “Her hücre neden var, hangi
matematiksel fikri temsil ediyor ve çıktıdan ne öğreniyoruz?”

Not: Hücre numaraları notebook’taki sıralamaya göredir.

## Hücre 0 — Başlık ve amaç
**Markdown:** Projenin başlığı ve kısa tanımı.
- Okuyucuya “Bu notebook neyi çözecek?” sorusunun cevabını verir.

## Hücre 1 — Kurulum (pip)
**Kod:** Colab gibi temiz ortamlar için kütüphaneleri kurar.
- Lokal çalıştırmada zaten yüklüyse hızlı geçer.
- Ders açısından “çalıştırılabilirlik” vurgusu sağlar.

## Hücre 2 — Import + Seed + Çıktı klasörleri
**Kod:** Paketleri içe aktarır, seed ayarlar, çıktı klasörlerini oluşturur.
- `SEED`: tekrar üretilebilirlik için sabitlenir.
- `OUTPUT_DIR` / `TABLE_DIR`: figür ve tabloların kaydı.
- `versions.json`: sürüm logu.

## Hücre 3 — Yardımcı Fonksiyonlar (başlık)
Bir sonraki hücredeki fonksiyon bloğunu tanıtır.

## Hücre 4 — Fonksiyonlar (projenin kalbi)
Bu hücrede tüm temel fonksiyonlar vardır.

### 4.1 Veri üretimi
- `make_synthetic_linear`: sentetik veri üretir.
- Kolineerlik: `x2 = x1 + 10^{-p} * ξ`.

### 4.2 Train/val ayrımı
- `train_val_split`: eğitim/doğrulama ayrımı yapar.

### 4.3 Standardizasyon
- `standardize`: bias sütununu korur, özellikleri ölçekler.

### 4.4 Parametre geri ölçekleme
- `unscale_theta`: GD’nin bulduğu `θ`’yı ham uzaya taşır.

### 4.5 Metrikler
- `rmse`, `cond_xtx`, `cond_x`.

### 4.6 Kapalı form çözücüler
- `normal_eq_inverse`, `normal_eq_solve`, `least_squares_qr`,
  `least_squares_explicit_qr`.

### 4.7 Gradient Descent
GD güncellemesi:
```
θ_{k+1} = θ_k - α * (1/n) * X^T (Xθ - y)
```
Loglar: `loss`, `grad_norm`, `iter`.

### 4.8 Gradient checking
Merkezi fark:
```
(J(θ+εe_i) - J(θ-εe_i)) / (2ε)
```

### 4.9 Alpha sweep
GD için en iyi α’yı seçer.

### 4.10 Deney fonksiyonları
`run_conditioning_experiment`, `run_gradient_check_experiment`,
`run_runtime_experiment`.

### 4.11 Grafik fonksiyonları
Her deneyin figürleri burada çizilir ve kaydedilir.

### 4.12 Testler
`run_tests()` solve ≈ lstsq ve gradient check eşiğini kontrol eder.

## Hücre 5 — Sentetik veri + kapalı form çözümler (başlık)

## Hücre 6 — Kapalı form çözümler
Sentetik veride inverse/solve/QR çözümleri ve RMSE çıktıları.

## Hücre 7 — GD alpha sweep (başlık)

## Hücre 8 — Alpha sweep sonuçları
GD için en iyi α seçilir. Çıktılar:
- `alpha_sweep.csv`
- `alpha_sweep.png`

## Hücre 9 — GD yakınsama (başlık)

## Hücre 10 — GD yakınsama grafiği
`gd_history.png` üretir (loss ve grad_norm).

## Hücre 11 — Koşullanma deneyi (başlık)

## Hücre 12 — p taraması (ill-conditioning)
Çıktılar:
- `conditioning_table.csv`
- `cond_vs_rmse.png`
- `p_vs_cond.png`
- `p_vs_rmse.png`

## Hücre 14 — Gradient checking (başlık)

## Hücre 15–16 — Epsilon sweep
Çıktılar:
- `epsilon_sweep.csv`
- `epsilon_sweep.png`

## Hücre 17 — Deney meta bilgisi
`experiment_meta.json` yazılır.

## Hücre 18 — Runtime ölçekleme (başlık)

## Hücre 19 — Runtime deneyleri
Çıktılar:
- `runtime_n.csv`, `runtime_d.csv`
- `runtime_n.png`, `runtime_d.png`

## Hücre 20 — Gerçek veri deneyi (başlık)

## Hücre 21–22 — California Housing / Diabetes
Çıktılar:
- `realdata_metrics.csv`
- `realdata_metrics.png`
- `realdata_gd_history.png`

## Hücre 23 — Özet (başlık)

## Hücre 24 — Özet tablosu
`summary_metrics.csv` üretilir.

## Hücre 25 — Basit Testler (başlık)

## Hücre 26 — Testleri çalıştır
`run_tests()` çalıştırılır.

---

# Ek B — Sunum Notları (≤10 Slayt)

Bu bölüm, 15 dakikalık sunum için konuşma notlarını verir.

## Slayt 1 — Başlık ve Amaç
“Normal denklem ve GD’yi sayısal kararlılık açısından karşılaştırıyoruz.”

## Slayt 2 — Problem Tanımı
Amaç fonksiyonu:
```
J(θ) = (1 / 2n) * ||Xθ - y||^2
```
Normal denklem ve GD’nin temeli bu fonksiyondur.

## Slayt 3 — Yöntem Haritası
Inverse / Solve / QR / GD / Gradient checking.

## Slayt 4 — Koşullanma
`p_vs_cond.png` ile p arttıkça `cond(X^T X)` büyüdüğünü göster.

## Slayt 5 — Koşullanma vs RMSE
`cond_vs_rmse.png` ve `p_vs_rmse.png` ile inverse’in bozulduğunu vurgula.

## Slayt 6 — GD Yakınsama + Alpha Sweep
`gd_history.png` ve `alpha_sweep.png`.

## Slayt 7 — Gradient Checking
`epsilon_sweep.png` ile truncation vs rounding farkını anlat.

## Slayt 8 — Runtime Ölçekleme
`runtime_n.png` ve `runtime_d.png` ile Big‑O gözlemi.

## Slayt 9 — Gerçek Veri
`realdata_metrics.png` ile gerçek dünyada performans karşılaştırması.

## Slayt 10 — Sonuç ve Öneriler
- Inverse kötü pratik.
- Solve/QR stabil.
- GD esnek ama pahalı.
- Gradient checking doğrulama sağlar.

Demo: `cond_vs_rmse.png`, `gd_history.png`, `epsilon_sweep.png`.

---

## Hücre 7 — GD alpha sweep (başlık)
GD için öğrenme oranını bilimsel şekilde seçmek.

## Hücre 8 — Alpha sweep sonuçları
- Farklı α değerleri denenir.
- En iyi α seçilir → `GD_ALPHA`.
- Çıktılar: `alpha_sweep.csv` ve `alpha_sweep.png`.

Bu bölüm, “GD sonucu keyfi değil, seçilmiş parametreyle” mesajını verir.

---

## Hücre 9 — GD yakınsama (başlık)

## Hücre 10 — GD yakınsama grafiği
**Kod:** Standardize veri üzerinde GD çalıştırır.
**Çıktı:** `gd_history.png` (loss ve grad_norm).

Bu grafik raporda “yakınsama davranışı” kanıtıdır.

---

## Hücre 11 — Koşullanma deneyi (başlık)

## Hücre 12 — p taraması (ill‑conditioning)
**Kod:** `p` değerleri için koşullanma ölçer.
**Çıktılar:**
- `conditioning_table.csv`
- `cond_vs_rmse.png`
- `p_vs_cond.png`
- `p_vs_rmse.png`

Bu bölüm, projeyi “basit ödev” olmaktan çıkaran en kritik kısımdır.

---

## Hücre 14 — Gradient checking (başlık)

## Hücre 15–16 — Epsilon sweep
**Kod:** `ε` taraması (float64 + float32).
**Çıktı:** `epsilon_sweep.csv`, `epsilon_sweep.png`.

Grafik yorumlaması:
- Büyük ε → truncation hatası
- Küçük ε → rounding hatası
- float32 daha yüksek hata tabanına sahiptir

---

## Hücre 17 — Deney meta bilgisi
**Kod:** Deney parametreleri `experiment_meta.json` içine yazılır.
Bu, raporda “deney ayarları şeffaftır” mesajı verir.

---

## Hücre 18 — Runtime ölçekleme (başlık)

## Hücre 19 — Runtime deneyleri
- `n` büyütülür (1k → 50k)
- `d` büyütülür (10 → 500)
**Çıktılar:** `runtime_n.csv`, `runtime_d.csv`, `runtime_n.png`, `runtime_d.png`

Big‑O yorumunu bu grafiklerle bağlarız.

---

## Hücre 20 — Gerçek veri deneyi (başlık)

## Hücre 21–22 — California Housing (fallback: Diabetes)
**Kod:** Gerçek veri yüklenir, solve/QR/GD karşılaştırılır.
**Çıktılar:** `realdata_metrics.csv`, `realdata_metrics.png`, `realdata_gd_history.png`

Bu kısım, projenin “gerçek dünya” bağını kurar.

---

## Hücre 23 — Özet (başlık)

## Hücre 24 — Özet tablosu
**Kod:** Raporda kullanılacak tek satırlık özet (`summary_metrics.csv`) oluşturur.

---

## Hücre 25 — Basit Testler (başlık)

## Hücre 26 — Testleri çalıştır
**Kod:** `run_tests()` fonksiyonu çağrılır.
Çıktı: “Tests passed.”

Bu hücre, notebook’un güvenilirliğini gösterir.

---

## Sonuç: Notebook’tan rapora giden yol
- Figürler: `outputs/figures`
- Tablolar: `outputs/tables`
- Rapor dosyası: `overleaf.txt`

Notebook çıktıları doğrudan rapora kopyalanabilir. Bu yüzden tüm hücrelerin
“Run all” ile çalıştırılmış olması teslim için önemlidir.
# Sunum Notları (≤10 Slayt, 15 dk)

Bu dosya, sunumda konuşacağın metni “ders anlatır gibi” sunar.
Slayt başına önerilen süre ~1–1.5 dakika.

---

## Slayt 1 — Başlık ve Amaç (1 dk)
**Göster:** Başlık, isim, amaç.
**Mesaj:** “Doğrusal regresyonda normal denklem ve GD’yi, sayısal kararlılık açısından karşılaştırıyoruz.”
**Konuşma Notu:**
“Projede amaç, en küçük kareler problemini farklı yöntemlerle çözüp
koşullanma ve sayısal hata etkisini deneysel olarak göstermek.”

---

## Slayt 2 — Problem Tanımı (1 dk)
**Göster:** Amaç fonksiyonu.
```
J(θ) = (1 / 2n) * ||Xθ - y||^2
```
**Konuşma Notu:**
“Bu fonksiyonun gradyanı ve optimum koşulu bizi normal denkleme götürüyor.
Ama burada sayısal kararlılık farkları ortaya çıkıyor.”

---

## Slayt 3 — Yöntem Haritası (1 dk)
**Göster:** Çözüm yolları: inverse / solve / QR / GD / gradient check.
**Konuşma Notu:**
“Kapalı form çözümler hızlı ama koşullanmaya duyarlı.
GD daha esnek ama iterasyon maliyeti var.
Gradient checking ile gradyan doğruluğunu test ediyoruz.”

---

## Slayt 4 — Normal Denklem ve Koşullanma (1.5 dk)
**Göster:** `p_vs_cond.png`.
**Konuşma Notu:**
“Kolineerliği p ile artırıyoruz. p büyüdükçe `cond(X^T X)` hızla artıyor.
Bu, normal denklemleri sayısal olarak kırılgan hale getiriyor.”

---

## Slayt 5 — Koşullanma vs Doğruluk (1.5 dk)
**Göster:** `cond_vs_rmse.png` ve `p_vs_rmse.png`.
**Konuşma Notu:**
“Inverse yöntemi kötü koşulda bozuluyor.
Solve ve QR daha stabil. GD doğruya yaklaşsa da iterasyon maliyeti var.”

---

## Slayt 6 — GD Yakınsama ve Alpha Sweep (1.5 dk)
**Göster:** `gd_history.png` ve `alpha_sweep.png`.
**Konuşma Notu:**
“GD’de α seçimi çok kritik. Sweep yapıp en iyi α’yı seçiyoruz.
Loss ve grad_norm düzgün düşüyorsa yakınsama güvenilir demektir.”

---

## Slayt 7 — Gradient Checking (1.5 dk)
**Göster:** `epsilon_sweep.png`.
**Konuşma Notu:**
“Merkezi fark ile analitik gradyanı karşılaştırıyoruz.
Küçük ε’de rounding, büyük ε’de truncation baskın.
Float32’de hata tabanı erken oluşuyor.”

---

## Slayt 8 — Runtime Ölçekleme (1 dk)
**Göster:** `runtime_n.png` ve `runtime_d.png`.
**Konuşma Notu:**
“Solve küçük/orta boyutta çok hızlı.
GD iterasyon sayısı nedeniyle daha yavaş.
Bu, Big‑O analizinin pratikteki karşılığı.”

---

## Slayt 9 — Gerçek Veri Deneyi (1 dk)
**Göster:** `realdata_metrics.png`.
**Konuşma Notu:**
“California Housing verisinde solve/QR hızlı ve stabil.
GD benzer doğruluk verse de runtime daha yüksek.”

---

## Slayt 10 — Sonuç ve Öneriler (1 dk)
**Mesaj:**
- “Inverse: kötü pratik.”
- “Solve/QR: daha stabil.”
- “GD: esnek ama parametrik.”
- “Gradient checking: analitik gradyanın doğrulandığı gösterildi.”
**Konuşma Notu:**
“Gelecekte ridge, SVD ya da SGD gibi yöntemlerle genişletilebilir.”

---

## Demo (isteğe bağlı, 30–60 sn)
Notebook’ta tek bir hücre çalıştırıp:
- `cond_vs_rmse.png`
- `gd_history.png`
- `epsilon_sweep.png`
çıktılarını göstermek yeterli.

---

Bu notlar, sunum sırasında “ne göstereceğim ve ne söyleyeceğim” sorusuna hızlı cevap verir.
