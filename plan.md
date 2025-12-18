# MAT353 Nümerik Analiz — Dönem Projesi Planı (Birleştirilmiş)
**Konu:** Doğrusal Regresyon’da *Normal Denklem* vs *Gradient Descent* + **Gradient Checking** (Sayısal vs Analitik Gradyan)  
**Teslim:** 21 Aralık 22:00 (Google Classroom)  
**Teslim edilecekler:** Rapor (8–15 sayfa), Sunum (≤10 slayt), Colab/Notebook + çalışan demo

---

## 1) Proje özeti (tek çatı)
Bu proje, doğrusal regresyonun en küçük kareler formülasyonu üzerinden:

1) **Kapalı form çözüm**: Normal denklem ile lineer sistem çözümü (inv / solve / QR)  
2) **İteratif çözüm**: Gradient Descent (GD) ile optimizasyon  
3) **Sayısal analiz odağı**:  
   - *Koşullanma (conditioning)* ve kolinear özellikler altında yöntemlerin davranışı  
   - GD’nin dayandığı **gradyanın doğrulanması**: merkezi fark ile **gradient checking**  
   - **ε taraması** ile *truncation vs rounding* hata tartışması

> “Mini araştırma” kısmı özellikle: (i) koşullanma deneyi, (ii) ε taraması ve sayısal hata yorumu.

---

## 2) Araştırma soruları (rapora direkt yazılabilir)
1. Özellikler kolinear hale geldikçe (kötü koşullanma arttıkça) normal denklem çözümü **sayısal olarak ne kadar bozulur**?  
2. Aynı koşullarda GD **daha mı dayanıklı** (stabil) yoksa sadece daha mı yavaş / hiperparametreye daha mı hassas?  
3. Gradient checking’de ε küçültmek her zaman daha iyi midir?  
   - Beklenen: Orta bir ε civarında hata minimum; çok küçük ε’de rounding baskınlaşır.

---

## 3) Ders içeriği ile ilişki (kısa eşleştirme)
- En küçük kareler / doğrusal regresyon: “En Küçük Kareler Yöntemi ile Grafik Oluşturma” çizgisine oturur.
- Normal denklem → **lineer sistem çözümü**: Gauss/Gauss-Jordan mantığı + sayısal kararlılık.
- Gradient checking → **sayısal türev**: ileri/geri/merkezi fark; merkezi farkın daha doğru olması.
- Sayısal hata tartışması → **kesme (truncation) / yuvarlama (rounding)** ayrımı.
- Matris sayısal özellikleri → rank, tekillik, kötü koşullanma, norm/cond.

---

## 4) Matematiksel çerçeve (raporun “Yöntem” bölümünün omurgası)

### 4.1 Amaç fonksiyonu (MSE tabanlı)
Veri: \(X \in \mathbb{R}^{n \times d}\), \(y \in \mathbb{R}^n\), parametre: \(\theta \in \mathbb{R}^d\)

\[
J(\theta)=\frac{1}{2n}\|X\theta-y\|_2^2
\]

### 4.2 Normal denklem
\[
\nabla_\theta J(\theta)=\frac{1}{n}X^T(X\theta-y)
\]
\[
\nabla_\theta J(\theta)=0 \Rightarrow X^TX\theta=X^Ty
\]

**Çözüm yaklaşımları (raporda karşılaştırılacak):**
- (Kötü pratik) \(\theta=(X^TX)^{-1}X^Ty\)  → *inv* ile
- (İyi pratik) \(\theta=\texttt{solve}(X^TX, X^Ty)\)
- (Opsiyonel, daha stabil) **QR/least squares**: \(\min_\theta \|X\theta-y\|\) doğrudan

> Not: Rapor dilinde “invert etmek yerine solve/QR ile çözmek daha stabil ve pratik” vurgusu.

### 4.3 Gradient Descent (batch GD)
\[
\theta_{k+1}=\theta_k-\alpha \nabla J(\theta_k)
\]
\[
\nabla J(\theta)=\frac{1}{n}X^T(X\theta-y)
\]

**Kayıt edilecek eğriler:**
- \(J(\theta_k)\) (loss)
- \(\|\nabla J(\theta_k)\|_2\) (gradyan normu)
- iterasyon sayısı, süre (runtime)

### 4.4 Gradient checking (sayısal gradyan — merkezi fark)
Tek bir parametre bileşeni için:
\[
\frac{\partial J(\theta)}{\partial \theta_i}\approx
\frac{J(\theta_i+\varepsilon)-J(\theta_i-\varepsilon)}{2\varepsilon}
\]

**Kesme hatası mertebesi:** merkezi fark için \(O(\varepsilon^2)\)

**Epsilon taraması:**
\[
\varepsilon \in \{10^{-1},10^{-2},\ldots,10^{-10}\}
\]
Beklenti: Çok büyük ε → truncation baskın; çok küçük ε → rounding baskın.

**Karşılaştırma metriği (öneri):**
\[
\text{relerr}=
\frac{|g_{\text{analytic}}-g_{\text{num}}|}
{\max(|g_{\text{analytic}}|,|g_{\text{num}}|)}
\]

---

## 5) Sayısal analiz odağı (projeyi “basit” olmaktan çıkaran bölüm)

### 5.1 Koşullanma (conditioning) ve kolinear özellik deneyi
Amaç: \(X^TX\) matrisini kötü koşullu hale getirmek.

Sentetik tasarım örneği:
- \(x_1 \sim \mathcal{N}(0,1)\)
- \(x_2 = x_1 + 10^{-p}\xi\), \(\xi \sim \mathcal{N}(0,1)\)
- p arttıkça \(x_1\) ve \(x_2\) daha kolinear → \(X^TX\) daha kötü koşullu

Ölç:
- \(\kappa(X^TX)=\text{cond}(X^TX)\)
- (sentetikte) \(\|\theta-\theta_{\text{true}}\|\)
- RMSE (train/val)
- Yöntemlere göre hata ve runtime

### 5.2 Stabilite varyantları
Karşılaştır:
1) inv ile çözüm (bilerek kötü pratik)
2) solve ile çözüm
3) (ops.) QR/least squares
4) GD (öğrenme oranı ve iterasyon etkisi)

---

## 6) Veri setleri
### 6.1 Sentetik veri (kontrollü)
**Amaç:** koşullanmayı doğrudan kontrol etmek, “θ_true” bildiğimiz için çözüm hatasını ölçmek.

Öneri parametreler:
- n: 2_000 (hızlı) / 10_000 (runtime testi)
- d: 5, 20, 100 (ölçekleme testi)
- noise σ: 0.1–1.0
- p: 0–12 arası tarama (kolinear şiddeti)

### 6.2 Gerçek veri (küçük)
Öneriler:
- California Housing (sklearn) veya benzeri küçük tablosal veri
- Gerekirse yedek: projeye gömülü küçük CSV

> Not: Gerçek veri tarafında “θ_true” yok; odak RMSE + runtime + genel yorum.

---

## 7) Deney tasarımı (tek tablo ile yönetim)

### Deney 1 — Sentetik, koşullanma taraması (mini araştırma)
**Değişken:** p  
**Sabitler:** n, d, noise, seed  
**Yöntemler:** inv / solve / (ops.) QR / GD  

Kayıtlar:
- cond(XTX)
- RMSE(train/val)
- (sentetik) ||θ − θ_true||
- runtime
- GD: iterasyon, loss eğrisi, ||grad|| eğrisi

### Deney 2 — n ve d ölçekleme (runtime analizi)
- n artışı: 1k → 10k → 50k (uygunsa)
- d artışı: 10 → 100 → 500 (uygunsa)
Çıktı: runtime karşılaştırması + Big-O ile yorum

### Deney 3 — Gradient checking + ε taraması
- Bir θ noktasında analitik ve sayısal gradyan karşılaştır
- ε sweep grafiği (log10 eksen önerilir)
- relerr minimum bölgeyi yorumla

---

## 8) Metrikler ve grafikler (raporda ve sunumda kullanılacak)
### 8.1 Başarı metrikleri
- MSE / RMSE (train/val)
- (sentetik) parametre hatası: \(\|\theta-\theta_{\text{true}}\|\)

### 8.2 GD metrikleri
- iterasyon sayısı
- loss eğrisi: \(J(\theta_k)\)
- gradyan normu eğrisi: \(\|\nabla J(\theta_k)\|\)

### 8.3 Sayısal analiz metrikleri
- cond(XTX) vs p grafiği
- yöntem hata farkları (inv vs solve vs QR)
- ε vs relerr grafiği (U-şekli beklenir)

---

## 9) Karmaşıklık (Big-O) — rapora konacak
- Normal denklem:
  - \(X^TX\) hesap: \(O(nd^2)\)
  - çözüm (genel): \(O(d^3)\)
- GD:
  - iterasyon başına: \(O(nd)\)
  - toplam: \(O(knd)\)

Yorum: d büyükse kapalı form pahalı olabilir; k küçükse GD avantajlı; koşullanma stabiliteyi belirler.

---

## 10) Uygulama planı (Colab + tek notebook)

### 10.1 Dosya/klasör yapısı (öneri)
```
project/
  README.md
  requirements.txt
  notebooks/
    01_experiments.ipynb   # tüm kod + tüm deneyler (tek tık)
  outputs/
    figures/
    tables/
  report/
    report.pdf
    references.bib   (ops.)
  slides/
    presentation.pptx
```

### 10.2 Fonksiyon listesi (çekirdek)
**Notebook (modül kodları hücresi)**
- `make_synthetic_linear(n, d, p, noise_std, seed) -> (X, y, theta_true)`
- `train_val_split(X, y, val_ratio, seed)`
- `standardize(X_train, X_val)` (GD için önerilir)
- `load_california_housing(val_ratio, seed, standardize_features)` (gerçek veri)

- `normal_eq_inverse(X, y)`
- `normal_eq_solve(X, y)`
- `least_squares_qr(X, y)` (ops.)
- `gradient_descent(X, y, alpha, max_iter, tol, log_every)`

- `J_mse(theta, X, y)`
- `grad_mse_analytic(theta, X, y)`
- `grad_numeric_central(J, theta, eps)`
- `epsilon_sweep(theta, X, y, eps_list)`

- `rmse(y_true, y_pred)`
- `cond_xtx(X)`

### 10.3 Reprodüksiyon (puan kazandırır)
- Her deneyde `seed` sabitle
- Sonuç tablolarına: n, d, p, noise, alpha, max_iter, tol yaz
- Notebook başında paket sürümleri çıktısı al (ops.)

---

## 11) Rapor planı (8–15 sayfa hedefli)
> Ders formatına uygun iskelet

1. **Kapak**
2. **Giriş (1–2 s.)**
   - Problem tanımı
   - Literatür (en az 3 bilimsel kaynak)
   - Neden bu yöntemler?
3. **Yöntem (2–4 s.)**
   - Amaç fonksiyonu
   - Normal denklem türetimi
   - GD türetimi
   - Gradient checking (merkezi fark) + \(O(\varepsilon^2)\)
   - Big-O
4. **Uygulama (2–4 s.)**
   - Veri üretimi (sentetik)
   - Gerçek veri
   - Adım adım pipeline
   - Hata analizi / koşullanma ölçümü
5. **Deneysel Sonuçlar (1–3 s.)**
   - tablolar + grafikler
   - runtime + iterasyon kıyasları
6. **Tartışma**
   - Koşullanma → inv vs solve vs QR
   - GD’nin davranışı (yakınsama, alpha hassasiyeti)
   - ε taraması: truncation vs rounding
7. **Sonuç ve Öneriler**
   - Bulguların özeti
   - Gelecek iş: Ridge, SGD, momentum/Adam (ops.)
8. **Kaynakça (IEEE)**
9. **Appendix**
   - kod parçaları, ek tablolar

---

## 12) Sunum planı (≤10 slayt)
1) Başlık + amaç  
2) Veri setleri (sentetik + gerçek)  
3) Amaç fonksiyonu + metrikler  
4) Normal denklem: inv vs solve vs QR  
5) GD: update + yakınsama kayıtları  
6) Koşullanma deneyi tasarımı (p parametresi)  
7) Sonuçlar: RMSE + runtime + cond etkisi  
8) Gradient checking: merkezi fark  
9) ε sweep grafiği + truncation/rounding yorumu  
10) Sonuç + öneriler + demo

> Demo çalışır olmalı: notebook tek tıkla grafik üretmeli.

---

## 13) 2 kişilik görev dağılımı (öneri)
**Kişi A (Normal denklem + koşullanma):**
- sentetik veri üretimi (p taraması)
- inv/solve/QR implementasyonu
- cond ölçümü + hata tabloları

**Kişi B (GD + gradient checking):**
- GD implementasyonu + logging (loss, grad norm)
- gradient checking + epsilon sweep
- truncation/rounding anlatımı + relerr grafiği

**Ortak:**
- gerçek veri deneyi
- rapor + sunum + demo provası

---

## 14) Zaman planı (17–21 Aralık)
- **17–18 Aralık:** Kod iskeleti + sentetik veri + normal denklem (inv/solve/QR)
- **19 Aralık:** GD + loglar + koşullanma deney koşuları
- **20 Aralık:** Gradient checking + ε sweep + tüm grafiklerin finalize edilmesi
- **21 Aralık:** Rapor (IEEE kaynakça) + 10 slayt + demo + paketleme (rapor+sunum+colab)

---

## 15) Riskler ve yedek planlar
- **Gerçek veri indirilemezse:** küçük CSV’yi repoya koy (offline güvence)
- **GD yakınsamazsa:** standardization + öğrenme oranı taraması + daha yüksek `max_iter`
- **inv patlarsa / NaN:** bu “beklenen” davranış; raporda bulgu olarak anlat, solve/QR ile düzelt
- **Zaman yetmezse:** QR opsiyonel; solve + inv + GD + gradient check yeterli

---

## 16) “Definition of Done” (teslim checklist)
### Notebook / Colab
- [ ] Sentetik koşullanma deneyi (p taraması) çalışıyor
- [ ] inv/solve/(ops QR) sonuçları aynı tabloya geliyor
- [ ] GD loss ve grad norm eğrileri çiziliyor
- [ ] ε sweep grafiği çiziliyor (relerr)
- [ ] `outputs/figures` altında tüm şekiller kaydediliyor

### Rapor
- [ ] 8–15 sayfa
- [ ] Yöntem kısmında türetimler + Big-O var
- [ ] Deney sonuçlarında tablo + grafik var
- [ ] Tartışma kısmında koşullanma + hata türleri yorumlanmış
- [ ] IEEE kaynakça + en az 3 bilimsel kaynak

### Sunum
- [ ] ≤ 10 slayt
- [ ] Görev dağılımı slaytı var
- [ ] Demo planı net

---

## 17) IEEE referans taslağı (örnek, düzenlenebilir)
> Aşağıdakiler “başlangıç” amaçlıdır; siz finalde IEEE formatını netleştirin.

[1] G. H. Golub and C. F. Van Loan, *Matrix Computations*, 4th ed.  
[2] S. Boyd and L. Vandenberghe, *Convex Optimization*.  
[3] Stanford CS231n Notes, “Gradient Checking” (ders notu/lecture note).  
[4] (İsteğe bağlı) Least squares / numerical stability üzerine bir makale veya ders notu.

---

## Ek: Önerilen deney parametre tablosu (rapora konabilir)
| Deney | n | d | p aralığı | noise | Yöntemler | Çıktılar |
|---|---:|---:|---:|---:|---|---|
| Sentetik koşullanma | 2000 | 20 | 0..12 | 0.5 | inv/solve/(QR)/GD | cond, RMSE, ||θ-θ_true||, runtime |
| Ölçekleme (n) | 1k..50k | 20 | sabit | 0.5 | solve/GD | runtime, RMSE |
| Ölçekleme (d) | 2000 | 10..500 | sabit | 0.5 | solve/GD | runtime, RMSE |
| Gradient check | 2000 | 20 | sabit | 0.5 | analytic vs numeric | relerr, ε sweep |

---
