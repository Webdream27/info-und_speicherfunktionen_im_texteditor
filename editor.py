""" ************************************************
Ein Editor
Aufgabe 1 und Aufgabe 2
************************************************""" 
# die Module importieren
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtCore import QDir

# das Formular importieren
from formular import Ui_MeinFormular

# eine Klasse für das Hauptfenster
class Hauptfenster(QMainWindow, Ui_MeinFormular):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Aufgabe 2: Variable zur Speicherung des aktuellen Dateipfades
        self.aktueller_dateipfad = None
        
        # die Aktionen verbinden
        self.action_Beenden.triggered.connect(self.action_close)
        self.action_Neu.triggered.connect(self.action_neu)
        self.action_ffnen.triggered.connect(self.action_open)
        self.action_Speichern.triggered.connect(self.action_save)
        
        # Aufgabe 1: Die "Info"-Aktion verbinden.
        self.action_Info.triggered.connect(self.zeige_info_dialog)
        
        # Aufgabe 2: Die "Speichern unter"-Aktion verbinden
        self.actionSpeichern_unter.triggered.connect(self.aktion_speichern_unter)
        
        # das Widget anzeigen
        self.show()

    def action_close(self):
        self.close()
        
    def action_neu(self):
        meine_abfrage = QMessageBox.question(self, 
                               "Abfrage",
                               "Wollen Sie wirklich eine neue Datei anlegen?")
        if meine_abfrage == QMessageBox.Yes:
            self.textEdit.clear()
            # Aufgabe 2: Dateipfad für neue Datei zurücksetzen
            self.aktueller_dateipfad = None
            
    # Aufgabe 2: Intelligente Speicherfunktion
    def action_save(self):
        if self.aktueller_dateipfad is None:
            self.aktion_speichern_unter()
        else:
            with open(self.aktueller_dateipfad, "w") as datei:
                datei.writelines(self.textEdit.toPlainText())
            self.statusbar.showMessage("Datei gespeichert.", 5000)

    # Aufgabe 2: Funktion für "Speichern unter"
    def aktion_speichern_unter(self):
        dateiname = QFileDialog.getSaveFileName(self,
                                                "Datei speichern unter", 
                                                QDir.currentPath(),
                                                "Textdateien (*.txt)")
        if dateiname[0] != "":
            self.aktueller_dateipfad = dateiname[0]
            self.action_save()
            
    def action_open(self):
        dateiname = QFileDialog.getOpenFileName(self,
                                                "Datei laden", 
                                                QDir.currentPath(),
                                                "Textdateien (*.txt)")
       
        if dateiname[0] != "":
            with open(dateiname[0], "r") as datei:
                text = ""
                for zeile in datei:
                    text = text + zeile
                self.textEdit.setPlainText(text)
            
            # Aufgabe 2: Pfad der geöffneten Datei merken
            self.aktueller_dateipfad = dateiname[0]
            
            self.statusbar.showMessage("Die Datei wurde geladen.", 5000)
    
    # Aufgabe 1: Funktion für den Info-Dialog
    def zeige_info_dialog(self):
        QMessageBox.information(self, 
                                   "Information", 
                                   "Mini-Editor\nProgrammiert von Andrea Sigl 2025")
           
# Anwendung starten
app = QApplication([])
fenster = Hauptfenster()
app.exec()