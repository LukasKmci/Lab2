"""
PLOT EXPORT SCRIPT FÜR LAB 2 LATEX-BERICHT
==========================================

Dieses Script exportiert automatisch alle generierten Plots aus dem 
MainCode2.ipynb Notebook mit den korrekten Dateinamen für LaTeX.

VERWENDUNG:
-----------
Füge diese Zelle am Ende von MainCode2.ipynb ein und führe sie aus.
Alle Plots werden im 'figures/' Ordner gespeichert.

ODER: Speichere als 'export_plots.py' und führe aus:
    python export_plots.py
"""

import matplotlib.pyplot as plt
import os

# ============================================================================
# KONFIGURATION
# ============================================================================

# Output-Verzeichnis
OUTPUT_DIR = 'figures'

# Mapping von Figure-Nummern zu LaTeX-Dateinamen
# Passe die Nummern an, falls deine Plots andere Figure-IDs haben!
PLOT_MAPPING = {
    # Task 3: Gefilterte EKG-Signale mit P-QRS-T Markierungen
    1: 'task3_person1_marked.png',
    2: 'task3_person2_marked.png',
    3: 'task3_person3_marked.png',
    
    # Task 5: R-Zacken-Detektion
    4: 'task5_person1_rwaves.png',
    5: 'task5_person2_rwaves.png',
    6: 'task5_person3_rwaves.png',
    
    # Task 7: Histogramme (erst nach Datenveröffentlichung)
    7: 'task7_histogram_hr.png',
    8: 'task7_histogram_hrv.png',
    
    # Task 8: Vollständiges Belastungsexperiment
    9: 'task8_full_exercise.png',
    
    # Task 9: Rampenphase (0-3 min)
    10: 'task9_ramp_phase.png',
    
    # Task 10: Erholungsphase (3-7 min)
    11: 'task10_recovery_phase.png',
    
    # Task 11: Energieverbrauch über Zeit
    12: 'task11_energy_expenditure.png',
}

# Export-Einstellungen
DPI = 300  # Hohe Auflösung für Druck
BBOX = 'tight'  # Kein Leerraum am Rand
FACECOLOR = 'white'  # Weißer Hintergrund

# ============================================================================
# FUNKTIONEN
# ============================================================================

def create_output_directory(directory):
    """Erstellt Output-Verzeichnis falls nicht vorhanden."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"✓ Verzeichnis erstellt: {directory}/")
    else:
        print(f"✓ Verzeichnis existiert: {directory}/")

def export_all_plots(mapping, output_dir, dpi=300, bbox='tight', facecolor='white'):
    """
    Exportiert alle aktiven Matplotlib-Figuren.
    
    Parameters:
    -----------
    mapping : dict
        Dictionary mit {figure_number: filename}
    output_dir : str
        Zielverzeichnis für Plots
    dpi : int
        Auflösung in dots per inch
    bbox : str
        Bounding box ('tight' = kein Rand)
    facecolor : str
        Hintergrundfarbe
    
    Returns:
    --------
    int : Anzahl erfolgreich exportierter Plots
    """
    
    # Verfügbare Figure-Nummern
    available_figures = plt.get_fignums()
    
    print(f"\n{'='*60}")
    print(f"PLOT EXPORT GESTARTET")
    print(f"{'='*60}")
    print(f"Verfügbare Figures: {available_figures}")
    print(f"Erwartete Plots: {len(mapping)}")
    print(f"Output: {output_dir}/")
    print(f"Einstellungen: DPI={dpi}, bbox='{bbox}', facecolor='{facecolor}'")
    print(f"{'='*60}\n")
    
    exported_count = 0
    missing_figures = []
    
    # Alle gemappten Plots exportieren
    for fig_num, filename in sorted(mapping.items()):
        filepath = os.path.join(output_dir, filename)
        
        if fig_num in available_figures:
            try:
                # Figure aktivieren
                plt.figure(fig_num)
                
                # Als PNG exportieren
                plt.savefig(
                    filepath,
                    dpi=dpi,
                    bbox_inches=bbox,
                    facecolor=facecolor,
                    edgecolor='none'
                )
                
                # Dateigröße ermitteln
                file_size = os.path.getsize(filepath) / 1024  # KB
                
                print(f"✓ Figure {fig_num:2d} → {filename:35s} ({file_size:6.1f} KB)")
                exported_count += 1
                
            except Exception as e:
                print(f"✗ Figure {fig_num:2d} → FEHLER: {e}")
        else:
            print(f"⚠ Figure {fig_num:2d} → NICHT GEFUNDEN (erwartet: {filename})")
            missing_figures.append(fig_num)
    
    # Zusammenfassung
    print(f"\n{'='*60}")
    print(f"EXPORT ABGESCHLOSSEN")
    print(f"{'='*60}")
    print(f"✓ Erfolgreich exportiert: {exported_count}/{len(mapping)}")
    
    if missing_figures:
        print(f"⚠ Fehlende Figures: {missing_figures}")
        print(f"\nMögliche Gründe:")
        print(f"  - Plot wurde nicht erstellt (Code nicht ausgeführt)")
        print(f"  - Figure-Nummer stimmt nicht (Mapping anpassen)")
        print(f"  - Plot wurde geschlossen (plt.close() aufgerufen)")
    
    # Nicht-gemappte Figures
    unmapped = set(available_figures) - set(mapping.keys())
    if unmapped:
        print(f"\n⚠ Nicht-gemappte Figures: {sorted(unmapped)}")
        print(f"  → Füge diese zu PLOT_MAPPING hinzu falls benötigt")
    
    print(f"{'='*60}\n")
    
    return exported_count

def export_current_figure(filename, output_dir=OUTPUT_DIR):
    """
    Exportiert die aktuell aktive Figure.
    
    VERWENDUNG IN NOTEBOOK-ZELLEN:
    -------------------------------
    plt.figure()
    plt.plot(...)
    export_current_figure('mein_plot.png')
    plt.show()
    """
    filepath = os.path.join(output_dir, filename)
    plt.savefig(filepath, dpi=DPI, bbox_inches=BBOX, facecolor=FACECOLOR)
    file_size = os.path.getsize(filepath) / 1024
    print(f"✓ Gespeichert: {filename} ({file_size:.1f} KB)")

# ============================================================================
# HAUPTPROGRAMM
# ============================================================================

if __name__ == "__main__":
    # Output-Verzeichnis erstellen
    create_output_directory(OUTPUT_DIR)
    
    # Alle Plots exportieren
    count = export_all_plots(
        mapping=PLOT_MAPPING,
        output_dir=OUTPUT_DIR,
        dpi=DPI,
        bbox=BBOX,
        facecolor=FACECOLOR
    )
    
    # Erfolgsmeldung
    if count == len(PLOT_MAPPING):
        print("🎉 ALLE PLOTS ERFOLGREICH EXPORTIERT!")
        print(f"   → {count} Dateien in '{OUTPUT_DIR}/' bereit für LaTeX")
    else:
        print(f"⚠️  NUR {count}/{len(PLOT_MAPPING)} PLOTS EXPORTIERT")
        print("   → Prüfe fehlende Plots und führe erneut aus")

# ============================================================================
# ALTERNATIVE: MANUELLE PLOT-SPEICHERUNG
# ============================================================================

"""
OPTION B: Direkt beim Plotten speichern
----------------------------------------

Füge nach jedem plt.show() in MainCode2.ipynb ein:

    plt.savefig(f'{OUTPUT_DIR}/task3_person1_marked.png', 
                dpi=300, bbox_inches='tight', facecolor='white')

Vorteil: Vollständige Kontrolle über Dateinamen
Nachteil: Manuell für jeden Plot

BEISPIEL FÜR TASK 3:
--------------------

# Person 1
fig = plt.figure(figsize=(12, 6))
plt.plot(time_5s, ecg_person1_5s, label='EKG Signal', linewidth=1)
# ... weitere Plotting-Befehle ...
plt.title('Gefiltertes EKG - Person 1 mit P-QRS-T Markierungen')
plt.legend()
plt.grid(True, alpha=0.3)

# EXPORT
plt.savefig('figures/task3_person1_marked.png', dpi=300, bbox_inches='tight', facecolor='white')

plt.show()
"""

# ============================================================================
# DEBUGGING-FUNKTIONEN
# ============================================================================

def list_all_figures():
    """Zeigt alle aktuell offenen Matplotlib-Figuren."""
    figs = plt.get_fignums()
    print(f"\n{'='*60}")
    print(f"AKTIVE MATPLOTLIB FIGURES")
    print(f"{'='*60}")
    
    if not figs:
        print("Keine Figures gefunden!")
        print("\nMögliche Gründe:")
        print("  - Code noch nicht ausgeführt")
        print("  - Alle Figures geschlossen (plt.close('all'))")
        return
    
    print(f"Anzahl: {len(figs)}\n")
    
    for i, fig_num in enumerate(figs, 1):
        fig = plt.figure(fig_num)
        ax = fig.get_axes()
        
        # Figure-Info
        print(f"{i}. Figure {fig_num}")
        print(f"   Größe: {fig.get_figwidth():.1f} x {fig.get_figheight():.1f} inch")
        print(f"   Axes: {len(ax)}")
        
        # Titel extrahieren (falls vorhanden)
        if ax and hasattr(ax[0], 'get_title'):
            title = ax[0].get_title()
            if title:
                print(f"   Titel: '{title}'")
        
        print()
    
    print(f"{'='*60}\n")

def check_file_sizes(directory=OUTPUT_DIR):
    """Prüft die Größe aller exportierten Dateien."""
    if not os.path.exists(directory):
        print(f"Verzeichnis '{directory}/' existiert nicht!")
        return
    
    files = [f for f in os.listdir(directory) if f.endswith('.png')]
    
    print(f"\n{'='*60}")
    print(f"EXPORTIERTE DATEIEN IN '{directory}/'")
    print(f"{'='*60}")
    
    if not files:
        print("Keine PNG-Dateien gefunden!")
        return
    
    print(f"Anzahl: {len(files)}\n")
    
    total_size = 0
    for filename in sorted(files):
        filepath = os.path.join(directory, filename)
        size_kb = os.path.getsize(filepath) / 1024
        total_size += size_kb
        print(f"  {filename:35s} {size_kb:8.1f} KB")
    
    print(f"\n{'='*60}")
    print(f"Gesamtgröße: {total_size:.1f} KB ({total_size/1024:.2f} MB)")
    print(f"{'='*60}\n")

# ============================================================================
# CONVENIENCE-FUNKTIONEN FÜR JUPYTER
# ============================================================================

def quick_export():
    """Schneller Export mit Standardeinstellungen - ideal für Jupyter."""
    create_output_directory(OUTPUT_DIR)
    count = export_all_plots(PLOT_MAPPING, OUTPUT_DIR, DPI, BBOX, FACECOLOR)
    
    if count == len(PLOT_MAPPING):
        print("\n✅ FERTIG! Alle Plots exportiert.")
        print(f"   Nächster Schritt: Lade die Dateien aus '{OUTPUT_DIR}/' in Overleaf hoch")
    else:
        print(f"\n⚠️  Nur {count}/{len(PLOT_MAPPING)} Plots exportiert - prüfe fehlende!")

# ============================================================================
# VERWENDUNG IN JUPYTER NOTEBOOK
# ============================================================================

"""
EINFACHSTE VERWENDUNG:
----------------------

1. Kopiere diese gesamte Datei als LETZTE ZELLE in MainCode2.ipynb

2. Führe die Zelle aus mit:
   
   quick_export()

3. Fertig! Alle Plots sind in 'figures/' gespeichert


DEBUGGING:
----------

Falls Probleme auftreten:

    # Zeige alle offenen Figures
    list_all_figures()
    
    # Prüfe exportierte Dateien
    check_file_sizes()


EINZELNER PLOT:
---------------

Falls du nur einen bestimmten Plot exportieren willst:

    export_current_figure('mein_custom_plot.png')
"""
