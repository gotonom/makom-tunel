# MAKOM · Faz 2 Tünel Otomasyonu

Mantar kompostu Faz 2 tüneli için otomasyon panosu ve süreç simülasyonu. Created by **GOTONOM**.

- **Canlı (Railway):** https://makom-tunel-production.up.railway.app
- **GitHub Pages:** https://gotonom.github.io/makom-tunel/

PLC bağlantısı kurulana kadar pano örnek veriyle çalışan bir simülasyon gösterir: 7 etaplı tarif, otomatik etap geçişleri, alarm senaryoları, fan ve damper için manuel müdahale, fan sesi.

## Yapı

| Yol | Ne |
|---|---|
| `src/dashboard.html` | Panonun kaynağı (stil, işaretleme ve simülasyon tek dosyada) |
| `build.py` | `src/dashboard.html`'i tam bir HTML belgesine çevirip `docs/index.html`'e yazar |
| `docs/index.html` | Yayınlanan sayfa (GitHub Pages bu klasörü sunar) |
| `server.js` | Railway'de `docs/index.html`'i `$PORT` üzerinden sunan bağımlılıksız Node sunucusu |

## Güncelleme

```bash
python3 build.py
git commit -am "..." && git push
railway up --service makom-tunel --detach
```

## Tesis değerleri

Fan %100: 18.000 m³/h, 4.000 Pa, 30 kW · Danfoss VLT HVAC FC 102 (37 kW) · Tünel 4 × 15 m · 16 × Ø160 PVC spigot hattı · Ø800 ana flanş.
