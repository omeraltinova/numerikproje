# MAT353 Nümerik Analiz — Doğrusal Regresyon Projesi

Bu repo, `plan.md`’deki gereksinimlere göre doğrusal regresyonun **normal denklem** ve **gradient descent** yaklaşımlarını sayısal analiz odağıyla karşılaştırmak için hazırlandı. Çekirdek hedefler:

- Normal denklem (inv / solve / opsiyonel QR) çözümleri ve koşullanma etkisi
- Gradient Descent ile iteratif çözüm ve yakınsama logları
- Gradient checking (analitik vs sayısal gradyan, ε taraması)
- Sentetik ve küçük gerçek veri deneyleri, grafik ve tablolar

## Yapı
- `requirements.txt`: Python bağımlılıkları (numpy, scipy, pandas, matplotlib, scikit-learn)
- `notebooks/`: Projenin tamamı notebook içindedir
  - `notebooks/01_experiments.ipynb`: Tek tıkla çalışan ana demo/deney notebook’u (tüm fonksiyonlar hücre içinde)
- `outputs/figures`, `outputs/tables`: Grafik ve tablo çıktıları
- `report/`, `slides/`: Rapor ve sunum materyalleri için klasörler

## Başlangıç
1) Google Colab: `notebooks/01_experiments.ipynb` dosyasını yükleyip çalıştırın.

2) Lokal: herhangi bir Python ortamında bağımlılıkları kurup notebook’u açın:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook notebooks
```
3) Ana notebook’u (`notebooks/01_experiments.ipynb`) baştan sona çalıştırın; çıktılar `outputs/figures` ve `outputs/tables` altına kaydedilir.

## Notlar
- Reprodüksiyon için `seed` sabitleyin.
- `plan.md` içindeki deney tablolarını referans alın (p taraması, n/d ölçekleme, ε sweep).
- Bu repoda `.py` kaynak dosyası yok; tüm kod notebook hücreleri içindedir.
- Repo içinde `.venv` oluşturursanız disk üzerinde çok sayıda `.py` dosyası oluşur; git’e eklenmez ama “tamamen temiz klasör” istiyorsanız ortamı repo dışında kurun.
