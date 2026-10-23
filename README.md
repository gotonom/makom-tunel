# MAKOM · Otomasyon Panelleri

Kompost sahası ve mantar üretim tesisi için otomasyon panelleri ve süreç simülasyonları. Created by **GOTONOM**.

| Sayfa | Kaynak | Ne |
|---|---|---|
| `/` | `src/index.html` | Saha planı ve panellere giriş |
| `/bunker.html` | `src/bunker.html` | Faz 1 · 3 bunker, fan 5/25 dk, 6–7 dk otomatik uzatma, 7 dk PLC sınırı |
| `/tunel.html` | `src/dashboard.html` | Faz 2 · tünel pastörizasyon ve kondisyonlama |
| `/oda.html` | `src/oda.html` | Üretim odaları · 20 oda, 52 günlük döngü |

- **Canlı (Railway):** https://makom-tunel-production.up.railway.app
- **GitHub Pages:** https://gotonom.github.io/makom-tunel/

PLC bağlantısı kurulana kadar her panel örnek veriyle çalışan bir simülasyon gösterir: etap geçişleri, alarm senaryoları, manuel müdahale, fan sesi.

## Yapı

| Yol | Ne |
|---|---|
| `src/*.html` | Sayfa kaynakları (stil, işaretleme ve simülasyon her sayfada tek dosyada) |
| `build.py` | Her kaynağı tam bir HTML belgesine çevirip `docs/`'a yazar |
| `docs/` | Yayınlanan sayfalar (GitHub Pages bu klasörü sunar) |
| `server.js` | Railway'de `docs/` sayfalarını `$PORT` üzerinden sunan bağımlılıksız Node sunucusu |

## Güncelleme

```bash
python3 build.py
git commit -am "..." && git push
railway up --service makom-tunel --detach
```

## Tesis değerleri

- **Faz 2 tünel:** fan %100: 18.000 m³/h, 4.000 Pa, 30 kW, 1.450 d/dk · Danfoss VLT HVAC FC 102 (37 kW) · Belimo 20 Nm damper servoları · tünel 4 × 15 m (T1–T4) · 16 × Ø160 PVC spigot hattı · Ø800 ana flanş.
- **Faz 1 bunker:** 3 bunker, 18,00 × 7,20 m iç ölçü. Fan modeli doğrulanacak (panelde 7,5 kW, 2.000 m³/h, 6.000 Pa örnek değer).
- **Üretim odaları:** 20 oda, 7,00 × 18,00 m (126 m²), 10 + 10 karşılıklı, 5 m koridor. Klima santrali değerleri doğrulanacak.
