# Proje İlerleme Check-listesi

Tamamlandıkça kutucukları işaretleyin ve tarih/yorum ekleyin.

## Notebook
- [ ] p taraması sonuçlarını grafik/tablo olarak kaydet (`outputs/figures`, `outputs/tables`).
- [ ] n ölçekleme (1k..50k) deneylerini ekle ve kaydet.
- [ ] d ölçekleme (10..500) deneylerini ekle ve kaydet.
- [ ] Gerçek veri deneyi (ör. California Housing veya gömülü CSV) ekle.
- [ ] Hiperparametre/seed/log bilgilerini tablolaştır (alpha, max_iter, tol, seed vs).
- [ ] Paket sürümlerini kaydet (reprodüksiyon).
- [ ] Notebook TODO’larını temizle; tek tuşta çalışır hale getir.

## Kod
- [ ] Gerçek veri yükleme/ön işleme yardımcıları ekle (src/data.py veya yeni modül).
- [ ] Grafik/tablo kaydetme yardımcıları ekle (fig/tables için).
- [ ] Normal denklem ve GD için basit testler/regresyon testleri ekle.
- [ ] Gradient checking için otomatik doğrulama testi ekle.
- [ ] Hata kontrolleri: singular matris uyarısı, GD alpha/tol kontrolü vb.
- [ ] (Opsiyonel) CLI/script akışı ekle (notebook dışında çalışma).

## Dokümantasyon
- [ ] README’ye deneyleri çalıştırma adımları (örnek komutlar, figür kaydetme) ekle.
- [ ] Gerçek veri indirme/gömülü CSV kullanım notu ekle.
- [ ] outputs/figures ve outputs/tables kullanımını anlat.
- [ ] Rapor/sunum klasörleri için durum notu ekle.

## Teslim Kontrolü (plan.md “Definition of Done”)
- [ ] Sentetik koşullanma deneyi çalışıyor, sonuçlar tablo/grafik kaydediliyor.
- [ ] inv/solve/(ops. QR) aynı tabloya geliyor.
- [ ] GD loss ve grad norm eğrileri çiziliyor ve kaydediliyor.
- [ ] ε sweep grafiği çiziliyor ve kaydediliyor.
- [ ] Rapor: 8–15 sayfa, türetimler + Big-O, tablolar/grafikler, koşullanma + hata yorumları, IEEE kaynakça.
- [ ] Sunum: ≤10 slayt, görev dağılımı, demo planı.
