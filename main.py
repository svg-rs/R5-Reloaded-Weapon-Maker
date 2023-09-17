T='Settings'
P=open
L=print
K='game_folder.txt'
import sys,webbrowser as U,os
from PyQt5.QtWidgets import QFileDialog as V,QRadioButton,QTreeWidgetItem as W,QApplication as X,QMainWindow as Y,QWidget as Z,QVBoxLayout as a,QTabWidget as b,QLabel as G,QPushButton as c,QListWidget as Q,QLineEdit as M,QToolBar,QMenuBar,QMessageBox as A,QMenu as R,QMessageBox as A,QTableWidget,QTreeWidget as d,QTableWidgetItem,QAbstractItemView as N,QAbstractScrollArea,QAbstractItemView as N
class e(Z):
	def __init__(P):
		L='font: bold;';X='mp_weapon_alternator_smg';Y='mp_weapon_defender';Z='mp_weapon_esaw';A8='mp_weapon_epg';b='mp_weapon_shotgun';e='mp_weapon_vinson';h='mp_weapon_g2';i='mp_weapon_energy_ar';j='mp_weapon_hemlok';k='mp_weapon_sniper';l='mp_weapon_dmr';m='mp_weapon_lstar';A9='mp_weapon_mastiff';n='mp_weapon_shotgun_pistol';o='mp_weapon_semipistol';p='mp_weapon_energy_shotgun';q='mp_weapon_pdw';r='mp_weapon_rspn101';s='mp_weapon_r97';t='mp_weapon_autopistol';AA='mp_weapon_smart_pistol';u='mp_weapon_lmg';v='mp_weapon_doubletake';w='mp_weapon_wingman';x=['alternator','charge_Rifle','devotion','epg','eva','flatline','g7','havoc','hemlok','kraber','longbow','lstar','mastiff','mozambique','p2020','peacekeeper','prowler','r301','r99','re45','smart_pistol','spitfire','triple_take','wingman'];y=[e,i,j,m,r,u,Z];z=[b,p,n];A0=[o,t,w];A1=[X,q,s];A2=[v,l,k,h,Y];AB=R(T);super().__init__();A=a();S=G('Weapon Info: ');S.setStyleSheet(L);A.addWidget(S);global H;H=M();H.setPlaceholderText('Weapon Name');A.addWidget(H);global I;I=M();I.setPlaceholderText('Weapon Description');A.addWidget(I);K=G('Model Selection: ');K.setStyleSheet(L);A.addWidget(K);global B;B=d();B.setHeaderLabels(['Model Type:','Model Name:']);B.setColumnWidth(0,100);B.setStyleSheet('height:125px');B.setAlternatingRowColors(True);B.setSelectionBehavior(N.SelectRows);B.setSelectionMode(N.SingleSelection);A3={'RIFLE':y,'SHOTGUN':z,'SNIPER':A2,'PISTOL':A0,'SMG':A1}
		for(A4,A5)in A3.items():
			for A6 in A5:B.addTopLevelItem(W([A4,A6,x[0]]))
		A.addWidget(B)
		def A7(item):global J,f,g;J=B.currentItem();f=J.text(0);g=J.text(1)
		B.currentItemChanged.connect(A7);K=G('Weapon Type: ');K.setStyleSheet(L);A.addWidget(K);global D;D=Q();D.addItem('Rifle');D.addItem('Shotgun');D.addItem('Sniper');D.addItem('Pistol');A.addWidget(D);global O;O=G('Ammo List: ');O.setStyleSheet(L);A.addWidget(O);global C;C=Q();C.addItem('Heavy Ammo');C.addItem('Light Ammo');C.addItem('Energy Ammo');C.addItem('Shotgun Ammo');A.addWidget(C);U=G('Weapon Damage: ');U.setStyleSheet(L);A.addWidget(U);global E;E=M();E.setPlaceholderText('Weapon Damage Near: ');A.addWidget(E);global F;F=M();F.setPlaceholderText('Weapon Damage Far: ');A.addWidget(F);V=c('Generate Weapon');V.clicked.connect(P.generate_weapon);A.addWidget(V);P.setLayout(A)
	def generate_weapon(B):
		G='Error';D='\n';global C;L(J);K=os.path.join(os.path.dirname(__file__),'weapon_types/mp_weapon_types.txt')
		if H.text()==''or I.text()==''or E.text()==''or F.text()==''or C.count()==0:A.warning(B,G,'Please fill out all fields');return
		elif not E.text().isdigit()or not F.text().isdigit():A.warning(B,G,'Please enter valid numbers');return
		L(K);A.information(B,'Success','Weapon created with info: \n'+'Name: '+H.text()+D+'Desc: '+I.text()+D+'Near Damage: '+E.text()+D+'Far Damage: '+F.text()+'Model: '+J+'\nGenerated at: '+S)
class h(Y):
	def __init__(A):
		super().__init__();A.setWindowTitle('R5 Reloaded | Weapon Maker');A.setGeometry(600,350,650,300);B=R(T,A);A.menuBar().addMenu(B);D=B.addAction('Choose Game Folder');E=B.addAction('Help');F=B.addAction('Exit');F.triggered.connect(A.close);C=b(A);G=e();C.addTab(G,'Weapon Builder');A.setCentralWidget(C)
		def H():U.open('https://github.com/BrickOnAWall/R5-Reloaded-Weapon-Maker')
		def I():
			C=V.getExistingDirectory(A,'Select Game Folder')
			if os.path.exists(K):
				with P(K,'r')as B:B.write(C)
			with P(K,'w')as B:B.write(C)
		E.triggered.connect(H);D.triggered.connect(I)
if __name__=='__main__':
	i=X(sys.argv);j=h()
	if os.path.exists(K):
		with P(K,'r')as k:S=k.read();L(S)
	j.show();sys.exit(i.exec_())
#ni
