# Lab 2 - Hardware Setup & Datensammlung Guide

## 📋 Benötigte Komponenten

### Hardware:
- [ ] Mikrocontroller (SparkFun) mit USB-Kabel
- [ ] EMG/EKG Sensor (blau)
- [ ] 4er-Kabel (schwarz/rot/weiß/gelb)
- [ ] 3× Jumper-Kabel
- [ ] 3× EKG-Elektroden (weiß, rot, schwarz)
- [ ] Klebeband (hautneutral) für Kabel-Fixierung

### Software:
- [ ] Arduino IDE (Lab2Code1.ino)
- [ ] Python mit Jupyter (serialRead.ipynb)
- [ ] Lab2Functions.py

---

## 🔌 Hardware Setup (15 Minuten)

### Schritt 1: Sensor mit Kabel verbinden

1. **4er-Kabel mit blauem EKG-Sensor verbinden:**
   - Schwarzes Kabel → GND
   - Rotes Kabel → VCC (Stromversorgung)
   - Gelbes Kabel → VOUT (Signal-Ausgang)
   - Weißes Kabel → nicht verwendet

2. **Jumper-Kabel einstecken:**
   - In die andere Seite des 4er-Kabels
   - 3 Jumper-Kabel (schwarz, rot, gelb)

### Schritt 2: Mit Arduino verbinden

```
Arduino Board Anschlüsse:
┌────────────────────────────┐
│                            │
│  3.3V  ← ROT (VCC)        │
│  A0    ← GELB (VOUT)      │
│  GND   ← SCHWARZ (GND)    │
│                            │
└────────────────────────────┘
```

**Wichtig:**
- ✅ Rot = 3.3V (NICHT 5V!)
- ✅ Gelb = A0 (Analog Input)
- ✅ Schwarz = GND

### Schritt 3: Kabel mit Elektroden verbinden

Das 4er-Kabel hat **Druckknopf-Anschlüsse** für Elektroden:
- **Schwarz** → Schwarze Elektrode (Referenz)
- **Rot** → Rote Elektrode (V6)
- **Weiß** → Weiße Elektrode (Manubrium)

**⚠️ Farben beachten!** Falsche Zuordnung = schlechtes Signal!

---

## 🎯 Elektroden-Platzierung (KRITISCH!)

### Vorbereitung (pro Person):

1. **Haut reinigen:**
   - Mit Wasser + Seife waschen
   - Gut trocknen lassen
   - Optional: Leicht mit Alkoholtupfer abreiben (entfettet)

2. **Haare entfernen** (falls nötig):
   - Besonders bei Brust-Elektroden
   - Besserer Hautkontakt = besseres Signal

### Elektrode 1: Weiß → Manubrium (Brustbein)

**Position:** Oberer Teil des Brustbeins (Sternum)

**Anleitung:**
1. Finde die Kuhle zwischen Halsansatz und Brustbein
2. 2-3 cm darunter, in der Mitte
3. Oberster Teil des Brustbeins

```
     Kopf
       |
   [Kuhle]  ← Hier tastbar
       |
   [ Weiß ] ← Elektrode hier!
       |
   Brustbein
```

📹 **Video-Hilfe:** [Link aus Praktikumsunterlagen]

### Elektrode 2: Rot → V6 (linke Seite)

**Position:** Mittlere Axillarlinie, 5. Interkostalraum

**Anleitung:**
1. Finde die 5. Rippe (ca. auf Brustwarzenhöhe)
2. Folge der Rippe zur linken Seite
3. Mittlere Axillarlinie = Linie unter der Achsel
4. Dort wo sich beides kreuzt

```
       Vorne
         |
    +----+----+
    |  Herz  |
    +----+----+
         |
      [5.Rippe]
         ↓
    Seite: [ Rot ] ← Hier!
```

📹 **Video-Hilfe:** [Link aus Praktikumsunterlagen]

### Elektrode 3: Schwarz → C7 (Nacken-Referenz)

**Position:** 7. Halswirbel (C7), Referenzelektrode

**Anleitung:**
1. Kopf nach vorne beugen
2. Fühle den prominentesten Wirbel im Nacken
3. Das ist C7
4. Elektrode direkt auf den Wirbel

```
    Kopf
     ||
    [C7]  ← Prominent! Fühlbar!
     ||   [ Schwarz ] ← Hier!
  Rücken
```

**⚠️ WICHTIG:** 
- Referenzelektrode muss **ruhig bleiben**!
- Keine Bewegung → sonst Artefakte
- Bei liegender Position: Polster unter Nacken (nicht auf Elektrode drücken!)

📹 **Video-Hilfe:** [Link aus Praktikumsunterlagen]

### Kabel fixieren:

**Nach Elektroden-Anbringen:**
1. Kabel mit Klebeband fixieren
2. **2-3 cm Abstand** von der Elektrode
3. Reduziert Bewegungsartefakte
4. Hautneutrales Klebeband verwenden!

```
[Elektrode]--2cm--[Klebeband]===Kabel===
```

---

## 💻 Software Setup (10 Minuten)

### Arduino-Code hochladen:

1. **Arduino IDE öffnen**
2. **Lab2Code1.ino öffnen**
3. **Board wählen:** Tools → Board → Arduino Uno (oder SparkFun RedBoard)
4. **Port wählen:** Tools → Port → COM* (Windows) oder /dev/ttyUSB* (Linux)
5. **Hochladen:** Upload-Button (→)
6. **Warten** bis "Done uploading"

**Code-Einstellungen:**
```cpp
const int sampleRateHz = 700;  // ~1000 Hz effektiv
Serial.begin(500000);           // Baud Rate 500000
```

### serialRead.ipynb vorbereiten:

1. **Jupyter Notebook öffnen**
2. **serialRead.ipynb öffnen**
3. **Parameter anpassen:**

```python
PORT = 'COM6'          # ← DEIN PORT! Prüfen!
BAUD_RATE = 500000     # ← Muss gleich wie Arduino sein!
T_RECORD = 10          # ← 10 Minuten (0.1 = 6 Sekunden für Test)
OUTPUT_FILE = 'rest_person1.csv'  # ← Name anpassen!
```

**Port herausfinden:**
- **Windows:** Arduino IDE → Tools → Port → COM6 (oder ähnlich)
- **Linux/Mac:** `ls /dev/tty*` im Terminal

---

## 📊 Datensammlung - Workflow

### Test-Aufnahme (IMMER ZUERST!):

**Bevor ihr 10 Minuten aufnehmt, testet das System:**

1. **serialRead.ipynb öffnen**
2. **`T_RECORD = 0.1` setzen** (= 6 Sekunden)
3. **Zelle ausführen**
4. **Signal prüfen:**
   - Plot in Zelle 2 anschauen
   - EKG-Form erkennbar? (QRS-Komplex sichtbar?)
   - Zu viel Rauschen? → Elektroden neu platzieren

**Nur wenn Test OK → Weiter zur vollen Aufnahme!**

### Ruhe-Experiment (10 Min pro Person):

#### Vorbereitung:
1. **Raum vorbereiten:**
   - Ruhiger Ort (keine Störungen!)
   - Liegemöglichkeit (Bett, Sofa, Yogamatte + Decke)
   - Polster für Nacken (Referenzelektrode nicht belasten!)

2. **Laptop vorbereiten:**
   - **Vollständig aufladen!**
   - **Stromsparmodus deaktivieren:**
     - Windows: Einstellungen → Energie → "Nie"
     - Mac: Systemeinstellungen → Energie → "Bildschirm aus: Nie"
   - **Laptop vom Netzteil trennen** (reduziert 50 Hz Rauschen!)

3. **Elektroden anbringen:**
   - Siehe Elektroden-Platzierung oben
   - Kabel fixieren
   - Test-Aufnahme machen!

#### Durchführung:
1. **Proband legt sich hin**
   - Entspannte Position
   - Polster unter Nacken (beidseitig der schwarzen Elektrode)
   - Nicht auf Referenzelektrode drücken!

2. **serialRead.ipynb starten:**
   ```python
   T_RECORD = 10  # 10 Minuten
   OUTPUT_FILE = 'rest_person1.csv'
   ```
   - Zelle ausführen
   - Konsole zeigt Fortschritt

3. **10 Minuten warten:**
   - Proband bleibt ruhig liegen
   - Nicht sprechen
   - Nicht bewegen
   - Entspannt atmen

4. **Nach 10 Minuten:**
   - Script stoppt automatisch
   - CSV-Datei gespeichert: `rest_person1.csv`
   - Datei umbenennen falls nötig

5. **Wiederholen für Person 2 & 3:**
   - `OUTPUT_FILE = 'rest_person2.csv'`
   - `OUTPUT_FILE = 'rest_person3.csv'`

**Zeit pro Person:** ~15 Min (5 Min Setup + 10 Min Messung)

---

### Bewegungs-Experiment (10 Min, 1 Person):

#### Zusätzliche Hardware:
- Fahrrad-Ergometer (Tacx + Mountainbike)
- ⚠️ **Tacx muss am Stromnetz sein** → **mehr Rauschen erwartet!**

#### Vorbereitung:
1. **Verkabelung gut fixieren!**
   - Mehrere Klebeband-Stellen
   - Kabel nicht unter Spannung
   - Bewegungsartefakte minimieren

2. **Ergometer positionieren:**
   - Laptop in Reichweite
   - Stabil aufstellen

3. **Elektroden prüfen:**
   - Test-Aufnahme während Sitzen
   - Signal OK?

#### Durchführung:

**Protokoll (genau einhalten!):**

```
 0:00 - 2:00 Min: RUHE (auf Ergometer sitzen, NICHT treten)
 2:00 - 5:00 Min: RAMP (konstant treten, mittlere bis schwere Anstrengung*)
 5:00 -10:00 Min: RECOVERY (stoppen, erholen, ruhig sitzen)

* Proband soll sich nach 3 Min erschöpft fühlen!
```

1. **serialRead.ipynb starten:**
   ```python
   T_RECORD = 10
   OUTPUT_FILE = 'exercise_person1.csv'
   ```

2. **0:00-2:00 Min: Ruhe**
   - Auf Ergometer sitzen
   - NICHT treten!
   - Puls ruhen lassen

3. **2:00 Min: START TRETEN**
   - Konstante Leistung
   - Mittlere bis schwere Anstrengung
   - Ziel: Nach 3 Min erschöpft

4. **5:00 Min: STOPPEN**
   - Sofort aufhören zu treten
   - Ruhig sitzen bleiben
   - Erholen

5. **10:00 Min: Ende**
   - Script stoppt automatisch
   - CSV gespeichert: `exercise_person1.csv`

**⚠️ Sicherheit:**
- Bei Unwohlsein → sofort abbrechen!
- Genug trinken vorher
- Nicht bei Erkältung/Krankheit

---

## 🔍 Qualitätskontrolle

### Gutes EKG-Signal erkennen:

✅ **Gut:**
```
     R
    /|\
   / | \
  /  |  \
 P   |   T
     Q S
```
- Klare QRS-Komplexe
- R-Zacke deutlich höher als Rest
- Regelmäßiger Rhythmus
- Wenig Rauschen

❌ **Schlecht:**
```
 ~~~≈≈≈~~~≈≈≈~~~  (nur Rauschen)
```
- Keine klaren Peaks
- Sehr verrauscht
- Unregelmäßig

### Was tun bei schlechtem Signal?

**Problem: 50 Hz Netzbrummen (regelmäßige Wellen)**
→ Laptop vom Stromnetz trennen!

**Problem: Flache, kaum sichtbare QRS-Komplexe**
→ Elektroden neu platzieren (besserer Hautkontakt)

**Problem: Spikes / Artefakte**
→ Kabel besser fixieren (Bewegungsartefakte)

**Problem: Baseline wandert**
→ Referenzelektrode bewegt sich (C7 prüfen!)

---

## 📁 Datenformat

**Output-Format von serialRead.ipynb:**

```csv
index;value
1;512
2;515
3;518
...
```

- **Separator:** Semikolon (`;`)
- **Spalte 1:** Index (Sample-Nummer)
- **Spalte 2:** EKG-Rohwert (0-1023, 10-bit ADC)
- **Sampling Rate:** ~1000 Hz
- **Dauer:** 10 Min = ~600.000 Samples

**Umbenennen nach:**
- `rest_person1.csv`
- `rest_person2.csv`
- `rest_person3.csv`
- `exercise_person1.csv`

---

## 🛠️ Troubleshooting

### Problem: Arduino nicht gefunden
```
Error: Serial port COM6 not found
```

**Lösung:**
1. Arduino IDE öffnen → Tools → Port prüfen
2. USB-Kabel neu einstecken
3. Richtigen Port in serialRead.ipynb eintragen
4. Windows: Geräte-Manager prüfen (COM-Ports)

---

### Problem: Datenübertragung zu langsam
```
Sampling rate: 234 samples/second (sollte ~1000 sein!)
```

**Lösung:**
1. Baud Rate prüfen: Arduino = 500000, serialRead = 500000
2. Andere Programme schließen (CPU-Last reduzieren)
3. Besseres USB-Kabel verwenden

---

### Problem: Laptop schaltet sich aus
**Lösung:**
1. Vollständig aufladen vorher
2. Energiespareinstellungen deaktivieren
3. Extern

e Maus bewegen → verhindert Standby

---

### Problem: Keine R-Zacken detektiert (später im Notebook)
**Lösung:**
1. Rohdaten visuell prüfen (serialRead Zelle 2)
2. Wenn Signal gut → Parameter tunen:
   - `HEIGHT_THRESHOLD` (0.3-0.5)
   - `DISTANCE_THRESHOLD` (0.4-0.6)
3. Wenn Signal schlecht → neu messen!

---

## ⏱️ Zeitplan für Messungen

### Empfohlener Ablauf (2 Stunden total):

**0:00-0:15** - Setup
- Hardware aufbauen
- Software testen
- Test-Aufnahme (6s)

**0:15-0:30** - Person 1 Ruhe
- Elektroden anbringen
- 10 Min Messung
- Elektroden entfernen

**0:30-0:45** - Person 2 Ruhe
- Elektroden anbringen
- 10 Min Messung
- Elektroden entfernen

**0:45-1:00** - Person 3 Ruhe
- Elektroden anbringen
- 10 Min Messung
- Elektroden entfernen

**1:00-1:10** - Pause & Setup Ergometer

**1:10-1:25** - Person 1 Bewegung
- Elektroden anbringen (fester!)
- 10 Min Protokoll
- Elektroden entfernen

**1:25-1:30** - Aufräumen & Dateien prüfen

---

## 📋 Checkliste pro Messung

Vor Start:
- [ ] Haut gereinigt & getrocknet
- [ ] Elektroden korrekt platziert (Farben!)
- [ ] Kabel fixiert (2-3cm Abstand)
- [ ] Arduino hochgeladen (Lab2Code1.ino)
- [ ] COM-Port korrekt (serialRead.ipynb)
- [ ] Test-Aufnahme erfolgreich (6s)
- [ ] Laptop aufgeladen & Standby aus
- [ ] Laptop vom Netzteil getrennt (Ruhe-EKG)

Während Messung:
- [ ] Proband liegt/sitzt ruhig
- [ ] Script läuft (Fortschritt sichtbar)
- [ ] Keine Unterbrechungen

Nach Messung:
- [ ] CSV-Datei vorhanden
- [ ] Datei korrekt benannt
- [ ] Signal visuell geprüft (Zelle 2)
- [ ] Falls schlecht → neu messen!

---

## 💡 Profi-Tipps

### Für bestes Signal:
1. **Morgens messen** (weniger Koffein/Stress)
2. **Nicht direkt nach Essen** (verdauungsbedingte HR-Änderung)
3. **Raum temperieren** (nicht zu kalt → Zittern)
4. **Handy auf lautlos** (keine Ablenkung)

### Für effiziente Messungen:
1. **Alle Elektroden vorher öffnen** (spart Zeit)
2. **Reihenfolge überlegen** (wer macht Bewegung?)
3. **Parallel arbeiten** (eine Person macht Code, andere bereiten vor)
4. **Sofort prüfen** (nicht erst alle 4 messen, dann merken Signal schlecht)

### Für den Bewegungstest:
1. **Aufwärmen vorher** (2 Min leicht treten, DANN erst Messung)
2. **Intensität besprechen** (mittelschwer = kann noch reden)
3. **Wasserflasche bereitstellen**
4. **Nach Test:** 5 Min zusätzlich sitzen (optional, für eigenes Interesse)

---

## ✅ Erfolg prüfen

**Nach allen Messungen solltet ihr haben:**

```
✓ rest_person1.csv (~600.000 Zeilen, ~10 MB)
✓ rest_person2.csv (~600.000 Zeilen, ~10 MB)
✓ rest_person3.csv (~600.000 Zeilen, ~10 MB)
✓ exercise_person1.csv (~600.000 Zeilen, ~10 MB)
```

**Visueller Check (serialRead Zelle 2):**
- Klare QRS-Komplexe sichtbar? ✅
- Regelmäßiger Rhythmus? ✅
- Wenig Rauschen? ✅

**Wenn JA → Bereit für MainCode2.ipynb! 🎉**

**Wenn NEIN → Neu messen! (Besser 30 Min nochmal als tagelang mit schlechten Daten kämpfen)**

---

Viel Erfolg bei den Messungen! 💪❤️

Bei Problemen → README_LAB2.md lesen oder Lukas fragen!
