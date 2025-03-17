# MNK-Game

## Projektstruktur
Das Spiel basiert auf mehreren Klassen, die die Kernfunktionen realisieren:

### 1. Board-Klasse
- Stellt das Spielfeld als `numpy`-Matrix (`np.zeros`) dar.
- Implementiert die `has_won`-Methode zur Gewinnüberprüfung.
- Herausfordernd war insbesondere die Überprüfung von diagonalen Gewinnbedingungen.

### 2. Player-Klasse
- Implementiert die Spieler-Logik.
- Enthält die `make_move`-Methode zur Überprüfung gültiger Spielzüge.

### 3. Game-Klasse
- Steuert den Spielablauf (Spieler gegen Spieler).
- Importiert und verwaltet die anderen Klassen.
- Nutzt `game_loop`, um den Spielfluss zu steuern.

### 4. MyBot-Klasse
Diese Klasse erweitert `Player` und repräsentiert einen KI-gesteuerten Spieler.
Je nach Schwierigkeitsgrad nutzt der Bot unterschiedliche Strategien:
- **Leichte KI**: Wählt zufällig ein freies Feld.
- **Mittlere KI**: Simuliert Spielzüge, um herauszufinden, ob ein Gewinnzug möglich ist.
- **Schwierige KI**: Berücksichtigt nicht nur eigene Gewinnmöglichkeiten, sondern auch mögliche Gewinnzüge des Gegners.

## Implementierung
- Das Spiel wurde zuerst ohne strenge OOP-Prinzipien entwickelt, was zu Problemen führte.
- Anschließend erfolgte eine Umstrukturierung mit klarer Trennung der Klassen und Verantwortlichkeiten.
- Hauptsächlich wurden `numpy` für die Spielfeldlogik und KI-Algorithmen wie `Minimax` genutzt.

## Anforderungen
- Python 3.x
- `numpy`

## Nutzung
1. Starte das Spiel durch das Ausführen der `Game.py`-Datei.
2. Wähle einen Spielmodus (Mensch vs. Mensch oder Mensch vs. KI).
3. Folge den Anweisungen auf der Konsole.

## Weiterentwicklung
- Verbesserung der KI durch effizientere Algorithmen.
- Implementierung einer grafischen Benutzeroberfläche.
- Erweiterung auf Online-Mehrspielermodus.

---
