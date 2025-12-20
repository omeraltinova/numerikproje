# Proje Tanıtımı ve Amacı – Öneri Seti

## Problem ve Motivasyon
- Doğrusal regresyonda \(\min_\theta \lVert X\theta - y \rVert^2\) çözülüyor.
- Kolinearite ve ölçek farkı varsa \(X^T X\) kötü koşullandı, sayısal hata büyüyebilir.

## Proje Amacı
- Least-squares çözümünde `inverse`, `solve`, `QR`, `GD` yöntemlerini kıyaslamak.
- Hangi yöntemin hangi koşulda daha güvenilir/hızlı olduğunu göstermek.

## Kullanılan Yöntemler
- Normal denklem: \((X^T X)\theta = X^T y\) (`inverse` / `solve`).
- QR tabanlı least squares (`np.linalg.lstsq`, explicit QR ayrıştırması).
- Gradient Descent: \(\theta_{k+1} = \theta_k - \alpha \nabla J(\theta)\).

## Deney Tasarımı
- Sentetik veri ile kolineariteyi \(p\) parametresiyle artırıp koşullanmayı kontrol ettik.
- Gerçek veri: California Housing (gerekirse Diabetes fallback).
- Standardizasyonun koşul sayısına etkisini inceledik.

## Uygulama ve Demo
- Python / Colab üzerinde tek notebook akışı.
- Her yöntemle \(\theta\) hesaplanıp validation RMSE yazdırılıyor.
- GD için yakınsama grafikleri (loss ve \(\lVert \nabla J \rVert\)) üretiliyor.

## Değerlendirme Ölçütleri
- Doğruluk: RMSE
- Kararlılık: \(cond(X^T X)\)
- Performans: runtime (çalışma süresi)
- Doğrulama: gradient checking (relative error)

---

# Sonuç Slaytları (Outputs/Figures) – Tüm Şekillerle Öneri

> Not: Eğer ders için **kesin 5 slayt sınırı** varsa bu bölümden bazılarını birleştirerek kullan.

## Sonuç Slaytı 1 – GD Hiperparametre ve Yakınsama (Sentetik)
**Görseller:** `alpha_sweep.png` + `gd_history.png`

- **Mesaj 1:** `alpha` çok küçük olursa yakınsama yavaşlar ve RMSE yüksek kalır.
- **Mesaj 2:** En iyi denge için seçilen değer: **GD_ALPHA ≈ 0.003**.
- **Mesaj 3:** `gd_history` grafikleri loss ve \(\lVert\nabla J\rVert\) azalmasını gösterir (yakınsama kanıtı).

## Sonuç Slaytı 2 – Koşullanma Deneyi: Kolinearite → Cond
**Görseller:** `p_vs_cond.png` + `cond_vs_rmse.png`

- **Mesaj 1:** `p` arttıkça (kolinearite) \(cond(X^T X)\) log ölçekte hızlı büyür.
- **Mesaj 2:** `solve/QR/GD` kötü koşullanmada daha stabil kalır.
- **Mesaj 3:** `inverse` yöntemi outlier üretip sayısal kararsızlığa düşebilir.

## Sonuç Slaytı 3 – Koşullanma Deneyi: p → Hata (RMSE)
**Görsel:** `p_vs_rmse.png`

- **Mesaj 1:** Stabil yöntemlerde RMSE değişimi sınırlı kalır (aynı probleme benzer doğruluk).
- **Mesaj 2:** `inverse` için bazı p değerlerinde RMSE log ölçeğe taşacak kadar büyüyebilir.
- **Mesaj 3:** Sonuç: kötü koşullanmada ters alma yerine `solve/QR` tercih edilir.

## Sonuç Slaytı 4 – Gradient Checking (Sayısal Türev Doğrulama)
**Görsel:** `epsilon_sweep.png`

- **Mesaj 1:** Epsilon çok küçük olursa **yuvarlama hatası**, çok büyük olursa **yaklaşım hatası** baskın olur.
- **Mesaj 2:** Bu yüzden hata eğrisi genelde U-şeklindedir (orta bir epsilon aralığında minimum).
- **Mesaj 3:** `float32` daha yüksek hata tabanına sahiptir (hassasiyet sınırlı).

## Sonuç Slaytı 5 – Runtime Ölçekleme (n ve d arttıkça)
**Görseller:** `runtime_n.png` + `runtime_d.png`

- **Mesaj 1:** `solve` küçük/orta boyutta çok hızlıdır (ms seviyesinde).
- **Mesaj 2:** `GD` iteratif olduğu için süre belirgin büyür (yaklaşık \(O(knd)\)).
- **Mesaj 3:** `d` büyüdükçe `solve` tarafında \(O(d^3)\) etkisi görünür hale gelir.

## Sonuç Slaytı 6 – Gerçek Veri Özeti (California Housing)
**Görseller:** `realdata_metrics.png` + `realdata_gd_history.png`

- **Mesaj 1:** Standardizasyon \(cond(X^T X)\) değerini dramatik biçimde düşürür (raw → standardized).
- **Mesaj 2:** `solve/QR` benzer RMSE üretir; GD benzer seviyeye yaklaşır ama maliyeti daha yüksektir.
- **Mesaj 3:** GD grafikleri iteratif yakınsamanın “nasıl” gerçekleştiğini gösterir (loss / grad norm).
