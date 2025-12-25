# MAT353 Proje Sunum Raporu: Normal Denklem vs Gradient Descent

Bu rapor, proje kodlarını ve deney sonuçlarını bir sunumda anlatmak üzere hazırlanmıştır. Colab notebook'undaki her bir bölüm, kullanılan yöntemler, formülleri ve özellikle normalleştirmenin etkileri detaylandırılmıştır.

---

## 1. Giriş ve Projenin Amacı
Bu projenin amacı, Doğrusal Regresyon (Linear Regression) problemini çözerken kullanılan farklı nümerik yöntemleri karşılaştırmaktır.
Odaklandığımız üç temel soru şunlardır:
1.  **Normal Denklem** ve **Gradient Descent (GD)** aynı sonucu veriyor mu?
2.  Veri seti **kötü koşullu (ill-conditioned)** olduğunda hangi yöntemler çöküyor?
3.  Hesapladığımız gradyanlar matematiksel olarak doğru mu? (**Gradient Checking**)

---

## 2. Veri Üretimi ve Ön İşleme (Data Generation)

Kodun `make_synthetic_linear` fonksiyonunda sentetik veri üretiyoruz.
Modelimiz:
$$ y = X\theta + \epsilon $$
Burada $X$ özellik matrisi, $\theta$ katsayılar ve $\epsilon$ gürültüdür.

### Kolinearite (Eşdoğrusallık) Etkisi
Veriyi üretirken yapay bir zorluk ekliyoruz:
$$ x_2 = x_1 + 10^{-p} \cdot \xi $$
Burada $p$ değeri arttıkça, 1. ve 2. özellik birbirine çok benzer hale gelir. Bu durum matrisin **koşul sayısını (condition number)** artırır ve problemi sayısal olarak çözmesi zor bir hale getirir. Bu, yöntemlerin dayanıklılığını test etmemizi sağlar.

### Normalleştirme (Standardizasyon) Etkisi
Kodda `standardize` fonksiyonu ile veriler ölçeklenir.
*   **İşlem:** Her özellikten ortalaması çıkarılır ve standart sapmasına bölünür:
    $$ X_{new} = \frac{X - \mu}{\sigma} $$
*   **Önemli Detay:** **Bias sütunu (1'lerden oluşan ilk sütun) asla standardize edilmez.** Çünkü standart sapması 0'dır, bölme hatası yaratır. Kodda bias sütunu ayrılıp, diğerleri ölçeklendikten sonra tekrar birleştiriliyor.
*   **Etkisi (Öncesi vs Sonrası):**
    *   **Normalleştirme Öncesi:** Özelliklerin ölçekleri farklıysa (örn. biri 0-1, diğeri 0-1000), Gradient Descent'in hata yüzeyi çok basık elipsler şeklindedir. GD zikzak çizerek çok yavaş ilerler.
    *   **Normalleştirme Sonrası:** Hata yüzeyi küresel (spherical) hale gelir. GD doğrudan minimuma doğru hızlıca ilerler. Ayrıca matrisin koşul sayısı (`cond_xtx`) genellikle düşer, bu da sayısal kararlılığı artırır.

---

## 3. Kullanılan Yöntemler ve Formüller

### 3.1. Amaç Fonksiyonu (Loss Function)
Hata Kareler Ortalaması (MSE) kullanıyoruz:
$$ J(\theta) = \frac{1}{2n} ||X\theta - y||^2 $$
$1/2n$ terimi, türev alırken 2 katsayısının sadeleşmesi ve veri sayısından bağımsız olması için eklenmiştir.

### 3.2. Normal Denklem (Kapalı Form Çözümler)
Gradyanı sıfıra eşitlediğimizde elde ettiğimiz denklem:
$$ X^T X \theta = X^T y $$

Kodda bu denklemi çözen 4 farklı yaklaşım var:
1.  **Inverse (`normal_eq_inverse`):** $\theta = (X^T X)^{-1} X^T y$.
    *   *Yorum:* Teorik olarak doğru ama **sayısal olarak kötü pratik**. Matrisin koşul sayısını karesine çıkarır ($\text{cond}(X^T X) \approx \text{cond}(X)^2$).
2.  **Solve (`normal_eq_solve`):** $A\theta = b$ sistemini çözer.
    *   *Yorum:* Ters matris almaz, LU veya Cholesky ayrışımı kullanır. Daha kararlıdır.
3.  **QR Ayrışımı (`least_squares_qr`):** $X = QR$ yazar.
    *   *Yorum:* $X^T X$ çarpımını hiç yapmaz. En kararlı (stabil) yöntemdir.
4.  **Explicit QR:** QR formülünü elle uygular.

### 3.3. Gradient Descent (GD)
İteratif güncelleme kuralı:
$$ \theta_{k+1} = \theta_k - \alpha \frac{1}{n} X^T (X\theta_k - y) $$
Burada $\alpha$ öğrenme oranıdır (learning rate).

---

## 4. Deneyler ve Grafikler

### 4.1. Alpha Sweep (Öğrenme Oranı Taraması)
*   **Amaç:** GD için en iyi $\alpha$ değerini bulmak.
*   **Kod:** `alpha_sweep_gd` fonksiyonu farklı $\alpha$ değerlerini dener.
*   **Sonuç:** Çok küçük $\alpha$ yavaş yakınsar, çok büyük $\alpha$ (örn. 0.1) hatanın patlamasına (divergence) yol açar. Kod en düşük RMSE veren değeri seçer.

### 4.2. Koşullanma Deneyi (Conditioning Experiment)
*   **Amaç:** Kolinearite şiddeti ($p$) arttıkça yöntemlerin nasıl bozulduğunu görmek.
*   **Grafik Yorumu (`cond_vs_rmse`):**
    *   $p$ arttıkça koşul sayısı ($10^p$) artar.
    *   **Inverse** yöntemi, koşul sayısı $10^{15}$ civarına gelince hata üretmeye başlar ve patlar.
    *   **Solve** ve **QR** yöntemleri çok yüksek koşul sayılarında bile stabil kalır.
    *   Bu deney, neden "matris tersi alma" yerine "sistem çözme" veya "QR" kullanmamız gerektiğini kanıtlar.

### 4.3. Gradient Checking (Gradyan Kontrolü)
*   **Amaç:** Analitik gradyan kodumuzun (`grad_mse_analytic`) doğru olup olmadığını test etmek.
*   **Yöntem:** Merkezi Fark (Central Difference) formülü ile sayısal türev alınır:
    $$ \frac{\partial J}{\partial \theta_i} \approx \frac{J(\theta + \epsilon e_i) - J(\theta - \epsilon e_i)}{2\epsilon} $$
*   **Grafik Yorumu (`epsilon_sweep`):**
    *   Grafik "U" şeklindedir.
    *   **Sağ taraf (Büyük $\epsilon$):** Kesme hatası (Truncation error) baskındır. Türev tanımından uzaklaşılır.
    *   **Sol taraf (Çok küçük $\epsilon$):** Yuvarlama hatası (Rounding error) baskındır. Bilgisayarın basamak hassasiyeti yetmez.
    *   `float32` kullanıldığında hata tabanı `float64`'e göre çok daha erken yükselir.

### 4.4. Çalışma Süresi (Runtime)
*   **Amaç:** Veri boyutu ($n$) ve özellik sayısı ($d$) arttıkça hızları kıyaslamak.
*   **Sonuç:** Küçük ve orta boyutlu verilerde **Solve** en hızlısıdır. GD, iterasyon sayısı nedeniyle genellikle daha yavaştır ancak çok büyük verilerde bellek avantajı sağlar.

---

## 5. Sonuç
Bu proje ile şunları gösterdik:
1.  **Normalleştirme**, Gradient Descent'in çalışması için hayati önem taşır.
2.  **Inverse almak** sayısal olarak tehlikelidir; **Solve** veya **QR** tercih edilmelidir.
3.  **Gradient Checking**, türev hesaplarının doğruluğunu kanıtlamak için güçlü bir araçtır.
4.  Doğru parametrelerle (iyi $\alpha$, standardize veri) GD, kapalı form çözümlerle aynı sonucu verir.
