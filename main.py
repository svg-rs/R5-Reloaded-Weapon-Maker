#Importing PyQt5, and system
import sys, webbrowser, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget, QLabel, QPushButton, QListWidget, QLineEdit, QToolBar, QMenuBar, QAction, QMessageBox, QMenu, QMessageBox



#Create new instance of Tab
class Tab1(QWidget):
    def __init__(self):


        settings_menu = QMenu("Settings")
        
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
        ammo_types.addItem("Heavy Ammo")
        ammo_types.addItem("Light Ammo")
        ammo_types.addItem("Energy Ammo")
        ammo_types.addItem("Shotgun Ammo")
        layout.addWidget(ammo_types)

        #Create label for weapon damage
        weapon_damage = QLabel("Weapon Damage: ")
        weapon_damage.setStyleSheet("font: bold;")
        layout.addWidget(weapon_damage)

        #Create weapon damage near input
        global weapon_near
        weapon_near = QLineEdit()
        weapon_near.setPlaceholderText("Weapon Damage Near: ")
        layout.addWidget(weapon_near)

        #Create weapon damage far input
        global weapon_far
        weapon_far = QLineEdit()
        weapon_far.setPlaceholderText("Weapon Damage Far: ")
        layout.addWidget(weapon_far)

        #Create Weapon List Button
        list_weapon = QPushButton("Generate Weapon")
        list_weapon.clicked.connect(self.generate_weapon)
        layout.addWidget(list_weapon)

        #Add Widgets to layout
        self.setLayout(layout)

        

    #Generate the weapon using user input
    def generate_weapon(self):
        global ammo_types

        #Check if user input is valid
        if weapon_name.text() == "" or weapon_description.text() == "" or weapon_near.text() == "" or weapon_far.text() == "" or ammo_types.count() == 0:
            QMessageBox.warning(self, "Error", "Please fill out all fields")
            return
        #elif user input is not an integer
        elif not weapon_near.text().isdigit() or not weapon_far.text().isdigit():
            QMessageBox.warning(self, "Error", "Please enter valid numbers")
            return
        
        #Copy file within weapon_types to output
        os.system("copy weapon_types/weapon_types.txt output/weapon_types.txt")


        

        #Give user success popup
        QMessageBox.information(self, "Success", "Weapon Generated")
            


    
    

#Create new window
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modern UI with Tabs")
        self.setGeometry(300, 300, 450, 30)
        
        #Create settings menu
        settings_menu = QMenu("Settings", self)
        self.menuBar().addMenu(settings_menu)
        

        
        #If help action is pressed, open the help window
        help_action = settings_menu.addAction("Help")
        

        #If exit action is pressed, close the window
        exit_action = settings_menu.addAction("Exit")
        exit_action.triggered.connect(self.close)

        tab_widget = QTabWidget(self)
        tab1 = Tab1()
        tab_widget.addTab(tab1, "Weapon Builder")
        self.setCentralWidget(tab_widget)

        #Create a function to open a link when help action is pressed
        def openLink():
            webbrowser.open("https://github.com/BrickOnAWall/R5-Reloaded-Weapon-Maker")

        help_action.triggered.connect(openLink)
        

#Start window
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
