# MAT353 Nümerik Analiz Projesi (Normal Denklem vs Gradient Descent + Gradient Checking)

Bu depo, rapor/sunum/Colab teslimi için gerekli deney iskeletini içerir.

## İçerik
- `src/data.py`: Sentetik veri üretimi, train/val ayrımı, standardizasyon.
- `src/solvers.py`: Normal denklem (inv, solve), QR (lstsq), Gradient Descent.
- `src/gradcheck.py`: Analitik gradyan, sayısal gradyan (merkezi fark), epsilon taraması.
- `src/experiments.py`: Koşullanma taraması, epsilon sweep, runtime testleri.
- `src/metrics.py`: RMSE ve cond(X^T X).
- `src/plots.py`: Koşullanma, GD geçmişi, epsilon sweep grafikleri.
- `notebooks/colab_template.py`: Colab’da çalıştırılabilir hücre iskeleti.
- `outputs/figures/`: Grafiklerin kaydedileceği klasör.

## Hızlı başlangıç (lokal veya Colab)
```bash
pip install -r requirements.txt
python notebooks/colab_template.py  # veya Colab’a kopyalayıp hücre hücre çalıştırın
```

## Üreteceğiniz figür ve tablolar
- p sweep (koşullanma) tablosu ve `cond_vs_rmse.png`
- GD loss / grad norm grafiği (`gd_history.png`)
- Epsilon–relerr U-eğrisi (`epsilon_sweep.png`)
- Runtime sweep çıktıları (print)

## Rapor ipuçları
- Özet: 200–250 kelime, referans yok.
- Giriş: min 3 IEEE kaynak (least squares, QR stabilitesi, sayısal hata, gradient checking).
- Yöntem: türetimler + Big-O + teknoloji gerekçesi.
- Deneyler: p-sweep sonuçlarını yorumla; epsilon U-eğrisi ile truncation vs rounding; GD yakınsama.
- Test süreci: gradient check ve çözücüler arası tutarlılık (inv/solve/QR farkları) belirt.
