# MAT353 Nümerik Analiz Projesi (Normal Denklem vs Gradient Descent + Gradient Checking)

Bu klasörde teslim için kullanılacak tek notebook ve rapor taslağı yer alır.

## İçerik
- `notebooks/colab_template.ipynb`: Tüm kodlar ve deneyler tek notebook içinde.
- `outputs/figures/`: Grafik çıktıları.
- `outputs/tables/`: Tablo çıktıları ve sürüm/metaveri logları.
- `overleaf.txt`: Rapor taslağı (LaTeX).
- `plan.md`, `prompt.md`: Proje planı ve notlar.
- `requirements.txt`: Lokal çalıştırma bağımlılıkları.

## Hızlı başlangıç
Colab:
- `notebooks/colab_template.ipynb` dosyasını yükleyip Run all.

Lokal:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook notebooks
```

## Üretilen çıktılar
- `conditioning_table.csv`, `cond_vs_rmse.png`, `p_vs_cond.png`, `p_vs_rmse.png`
- `alpha_sweep.csv`, `alpha_sweep.png`
- `gd_history.png`
- `epsilon_sweep.csv`, `epsilon_sweep.png`
- `runtime_n.csv`, `runtime_d.csv`, `runtime_n.png`, `runtime_d.png`
- `realdata_metrics.csv`, `realdata_metrics.png`
- `summary_metrics.csv`, `versions.json`

## Notlar
- Sentetik veri + gerçek veri (California Housing; internet yoksa Diabetes fallback).
- Tüm çıktılar `outputs/` altına kaydedilir.
- Teslim için notebook tüm hücreleri çalıştırılmış ve çıktılar üretilmiş olmalıdır.
