#Importing PyQt5, and system
import sys, webbrowser
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget, QLabel, QPushButton, QListWidget, QLineEdit, QToolBar, QMenuBar, QAction, QMessageBox, QMenu, QMessageBox



#Create new instance of Tab
class Tab1(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        #Create a title
        title = QLabel("Weapon Creator")
        title.setStyleSheet("font: bold;")
        layout.addWidget(title)

        #Create weapon name input
        global weapon_name
        weapon_name = QLineEdit()
        weapon_name.setPlaceholderText("Weapon Name")
        layout.addWidget(weapon_name)

        #Create weapon description input
        global weapon_description
        weapon_description = QLineEdit()
        weapon_description.setPlaceholderText("Weapon Description")
        layout.addWidget(weapon_description)

        #Create label for weapon list
        global weapon_list
        weapon_list = QLabel("Weapon List: ")
        weapon_list.setStyleSheet("font: bold;")
        layout.addWidget(weapon_list)


        #Create new list of weapons
        global weapons
        weapons = QListWidget()
        weapons.addItem("Rifle")
        weapons.addItem("Shotgun")
        weapons.addItem("Sniper")
        weapons.addItem("Pistol")
        layout.addWidget(weapons)

        #Create label for ammo list
        global ammo_list
        ammo_list = QLabel("Ammo List: ")
        ammo_list.setStyleSheet("font: bold;")
        layout.addWidget(ammo_list)

        #Create new list of ammo types
        global ammo_types
        ammo_types = QListWidget()
        ammo_types.addItem("Heavy")
        ammo_types.addItem("Light")
        ammo_types.addItem("Energy")
        layout.addWidget(ammo_types)

        #Create weapon damage near input
        global weapon_damage_near
        weapon_damage_near = QLineEdit()
        weapon_damage_near.setPlaceholderText("Weapon Damage Near")

        #Create weapon damage far input
        global weapon_damage_far
        weapon_damage_far = QLineEdit()
        weapon_damage_far.setPlaceholderText("Weapon Damage Far")

        #Create Weapon List Button
        list_weapon = QPushButton("Generate Weapon")
        list_weapon.clicked.connect(self.generate_weapon)
        layout.addWidget(list_weapon)

        #Add Widgets to layout
        self.setLayout(layout)

    #Generate the weapon using user input
    def generate_weapon(self):
        global ammo_types
        #Output weapon info to generate_weapons.txt and replace certain strings with user input
        with open("generate_weapons.txt", "w") as f:
            f.write(weapon_name.text() + "\n")
            f.write(weapon_description.text() + "\n")
            f.write(weapons.currentItem().text() + "\n")
            f.write(ammo_types.currentItem().text() + "\n")
            f.write(weapon_damage_near.text() + "\n")
            f.write(weapon_damage_far.text() + "\n")

        #Open generate_weapons.txt and add new line with weapon name
        with open("generated_weapons.txt", "a") as f:
            f.write("\n" + weapon_name.text())

        #Give user success popup
        QMessageBox.information(self, "Success", "Weapon Generated")
            

    #Go to url if user clicked
    def open_url(self):
        webbrowser.open_new_tab("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        

#Create new window
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modern UI with Tabs")
        self.setGeometry(300, 300, 450, 30)
        
        #Create settings menu
        settings_menu = QMenu("Settings", self)
        settings_menu.addAction("Help")
        settings_menu.addAction("Exit")
        self.menuBar().addMenu(settings_menu)

        tab_widget = QTabWidget(self)
        tab1 = Tab1()
        tab_widget.addTab(tab1, "Weapon Builder")
        self.setCentralWidget(tab_widget)

        

#Start window
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())