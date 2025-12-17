# MAT353 Nümerik Analiz — Doğrusal Regresyon Projesi

Bu repo, `plan.md`’deki gereksinimlere göre doğrusal regresyonun **normal denklem** ve **gradient descent** yaklaşımlarını sayısal analiz odağıyla karşılaştırmak için hazırlandı. Çekirdek hedefler:

- Normal denklem (inv / solve / opsiyonel QR) çözümleri ve koşullanma etkisi
- Gradient Descent ile iteratif çözüm ve yakınsama logları
- Gradient checking (analitik vs sayısal gradyan, ε taraması)
- Sentetik ve küçük gerçek veri deneyleri, grafik ve tablolar

## Yapı
- `requirements.txt`: Python bağımlılıkları (numpy, scipy, pandas, matplotlib, scikit-learn)
- `src/`: Modüler kod
  - `data.py`: Veri üretimi, bölme, standardizasyon
  - `solvers.py`: Normal denklem çözücüleri + GD
  - `gradcheck.py`: MSE fonksiyonu, analitik/sayısal gradyan, ε taraması
  - `metrics.py`: RMSE, koşullanma ölçümü
  - `utils.py`: Yardımcılar (seed, zamanlama vb.)
- `notebooks/`: Deney notebook’ları (`01_experiments.ipynb` taslak)
- `outputs/figures`, `outputs/tables`: Grafik ve tablo çıktıları
- `report/`, `slides/`: Rapor ve sunum materyalleri için klasörler

## Başlangıç
1) Ortamı kurun:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
2) Notebook çalıştırın:
```bash
jupyter notebook notebooks
```
3) Deney sonuçlarını `outputs/figures` ve `outputs/tables` altına kaydedin.

## Notlar
- Reprodüksiyon için `seed` sabitleyin.
- `plan.md` içindeki deney tablolarını referans alın (p taraması, n/d ölçekleme, ε sweep).
