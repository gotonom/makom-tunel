# MAKOM · Otomasyon Panelleri

Kompost sahası ve mantar üretim tesisi için otomasyon panelleri ve süreç simülasyonları. Created by **GOTONOM**.

| Sayfa | Kaynak | Ne |
|---|---|---|
| `/` | `src/index.html` | Tesis kontrol merkezi: 27 ünitenin canlı saha planı, kompost yolculuğu, üretim takvimi, enerji, alarmlar |
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

## Paylaşım kartları (Open Graph)

Her sayfanın 1200 × 630 paylaşım görseli `docs/og/` içinde. Kaynağı `og/og.html` (#index, #bunker, #tunel, #oda); `python3 og/render.py` headless Chrome ile yeniden üretir. Meta etiketlerini `build.py` ekler.

## Güncelleme

```bash
python3 build.py
git commit -am "..." && git push
railway up --service makom-tunel --detach
```

## Tesis değerleri

- **Faz 2 tünel (MAKOM):** fan %100: 18.000 m³/h, 4.000 Pa, 30 kW, 1.450 d/dk · Danfoss VLT HVAC FC 102 (37 kW) · Belimo 20 Nm damper servoları · tünel 4 × 15 m (T1–T4) · 16 × Ø160 PVC spigot hattı · Ø800 ana flanş.
- **Faz 1 bunker:** 3 bunker, 18,00 × 7,20 m iç ölçü.
- **Üretim odaları:** 20 oda, 7,00 × 18,00 m (126 m²), 10 + 10 karşılıklı, 5 m koridor.

## Ekipman araştırması (Ekim 2026, doğrulanacak)

Panellerde kullanılan ve MAKOM tarafından henüz onaylanmamış değerler:

| Parametre | Değer | Dayanak |
|---|---|---|
| Bunker kompost kütlesi | ~210 t (2,5 m × 650 kg/m³; 170–250 t) | Spa Hills Faz I bin verisi |
| Bunker fanı | 12.000 m³/h, ~5.000 Pa, ~24 kW mil gücü, 30 kW 2 kutuplu motor (2.950 d/dk) | Dalsem: Faz I 10–15 m³/h·t ve 3.500–6.000 Pa; 5/30 çevrimde ortalama 10 m³/h·t için çalışırken ~60 m³/h·t (Penn State 61,3) |
| Bunker invertörü | Danfoss FC-102P30KT4 (22 kW motorla P22K) | Danfoss FC 102 güç sınıfları |
| Oda yatak alanı / kompost | ~112 m² (1,4 m × 16 m × 5 kat, tek sıra) / ~10 t (90 kg/m²) | Mushroom Office, WUR |
| Oda klima santrali | 6.000 m³/h, ~800 Pa toplam (450 Pa dış), ~2,2 kW EC fan, 25 kW soğutma, 12 kW ısıtma | WUR (~190 m³/h·t besleme), EVROPROM (1,5–2 kW/t soğutma) |
| Damper servosu | Belimo SM24A-SR (20 Nm, 0–10 V, 150 s); küçük oda damperlerinde NM24A-SR (10 Nm) yeterli | Belimo bayi verileri |
| Tünel invertörü | FC-102P30KT4 (61 A) yeterli; seçilen P37K (73 A) sıcak ortam için pay bırakır | Danfoss FC 102 |
| Tünel fanı kontrolü | 5 m³/s × 4.000 Pa = 20 kW hava gücü → 30 kW milde η ≈ %67; 1.450 d/dk ile ~1,1 m çark makul | hesap |

Oda 7 m genişlikte iki sıra raf varsa yatak alanı ve oda değerleri yaklaşık iki katına çıkar.
