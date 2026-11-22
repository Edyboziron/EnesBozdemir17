# Proje Bilgileri
- Ogrenci No: 23020021017
- Proje: EnesBozdemir17_H3
- Motor: Unreal Engine 5.8
- MCP Port: 8000 (/mcp)
- Klasor Yapisi: Content/23020021017/H03/

---

## Hafta 3: İleri Blueprint & Ganimet Sistemi

### 1. BP_LootChest (Ganimet Sandığı)
- **BeginPlay**:
  - `Seed` değişkeni (Instance Editable) kullanılarak `MakeRandomStream` ile `Stream` başlatılır.
  - `ChestBase` ve `ChestLid` bileşenlerine varsayılan gri renkli `MI_Chest` materyali atanır.
  - `GetPlayerController(0)` alınarak `EnableInput` çağrılır ve sandığın klavye girdilerini alması sağlanır.
- **E Tuşu Olayı**:
  - `bConsumeInput = false` yapılarak aynı tuşun sahnedeki tüm sandıklara iletilmesi sağlanır.
  - `GetDistanceTo(GetPlayerCharacter(0))` ile oyuncunun sandığa olan mesafesi ölçülür.
  - Mesafe `300.0 cm` veya daha yakınsa `OpenChest` fonksiyonu tetiklenir.
- **RollRarity**:
  - Stream'den 0.0 - 1.0 arası rastgele float çekilir.
  - `< 0.60` -> Common (%60)
  - `< 0.90` -> Rare (%30)
  - Diğer -> Legendary (%10)
- **RarityBonus**:
  - Common: 0.0, Rare: 0.5, Legendary: 1.5 çarpanı döndürür.
- **CalculatePower**:
  - Formül: `BasePower * (1.0 + RarityBonus) + Roll`
  - Roll: Stream üzerinden `0` ile `ChestLevel` (5) arasında rastgele tam sayıdır.
- **OpenChest**:
  - Nadirlik ve güç hesaplanır.
  - Güç (10..40) aralığı `MapRangeClamped` ile 0..1 arasına çekilip gri ve altın rengi arasında `Lerp` yapılır.
  - `ChestBase` ve `ChestLid` bileşenlerinin dinamik materyalindeki `Color` parametresi güncellenir.
  - Ekranın sol üst köşesine formatlı mesaj 5 saniye boyunca yazdırılır: `{Eşya} ({Nadirlik}) — Guc: {Güç}`.

---

### 2. L_H03_AkisParkuru (Akış Kontrolü)
- **İstasyon 1 (MultiGate)**: `BP_MaterialDisplay` ile E tuşuna her basışta sırayla Altın, Bakır ve Nikel materyallerine geçiş.
- **İstasyon 2 (Switch on Int)**: `BP_DifficultyPanel` ile 1-4 tuşlarına basarak oyun zorluğunu ayarlama ve ekranda gösterme.
- **İstasyon 3 (Gate)**: `BP_HealthStation` ile trigger içine girildiğinde Gate açılır, karakterin canı 100 olana kadar şarj tüketerek can basar.
- **İstasyon 4 (Do N & FlipFlop)**: `BP_ThirdPersonCharacter` üzerinde Shift tuşu ile 3 kez kalkan açıp kapama hakkı (Do 3) ve açık/kapalı geçişi (FlipFlop).
- **Tuzaklar**: `BP_Mine` ile WhileLoop üzerinden geri sayım ve patlama hasarı.
