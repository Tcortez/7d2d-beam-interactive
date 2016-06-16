from PyQt4 import QtGui, QtCore, QtSql  # Import the PyQt4 module we'll need
import sys  # We need sys so that we can pass argv to QApplication
import wssocket
import design  # This file holds our MainWindow and all design related things+


class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):
	def __init__(self):
		# Explaining super is out of the scope of this article
		# So please google it if you're not familar with it
		# Simple reason why we use it here is that it allows us to
		# access variables, methods etc in the design.py file
		super(self.__class__, self).__init__()
		self.setupUi(self)  # This is defined in design.py file automatically
		# It sets up layout and widgets that are defined
		self.setWindowTitle("7DTD Interactive")
		self.setWindowIcon(QtGui.QIcon('icon.jpg'))

		db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
		db.setDatabaseName('tester.sqlite')

		if not db.open():
			QtGui.QMessageBox.critical(None, QtGui.QMessageBox.tr(QtGui.QMessageBox.QObject, "OOPS"),
				QtGui.QMessageBox.tr(QtGui.QMessageBox.QObject, "Unable to establish a database connection.\n"
					"This example needs SQLite support. Please read "
					"the Qt SQL driver documentation for information "
					"how to build it.\n\n" "Click Cancel to exit."),
				QtGui.QMessageBox.Cancel)

		query = QtSql.QSqlQuery()

		query.exec_('''CREATE TABLE IF NOT EXISTS beam
		(ID INTEGER PRIMARY KEY   AUTOINCREMENT,
		username TEXT NOT NULL,
		password TEXT NOT NULL);''')

		# print("Table created successfully")

		query = QtSql.QSqlQuery()

		query.exec_('''CREATE TABLE IF NOT EXISTS server
		(ID INTEGER PRIMARY KEY   AUTOINCREMENT,
		username TEXT NOT NULL,
		host TEXT NOT NULL,
		port INTEGER NOT NULL,
		password TEXT NOT NULL);''')

		query = QtSql.QSqlQuery()

		beam = query.exec_("SELECT * FROM beam")
		while query.next():
			beam = query.value(0)

		print("Beam =", beam)

		query = QtSql.QSqlQuery()
		server = query.exec_("SELECT * FROM server")
		while query.next():
			server = query.value(0)

		print("Server =", server)

		server = dict(host='', port='', password='', username='')
		server["host"] = self.telnethostLineEdit
		server['port'] = self.telnetportLineEdit
		server['password'] = self.telnetpwLineEdit
		server['username'] = self.steamidLineEdit

		streamer = dict(username='', password='')
		streamer["username"] = self.beamunLineEdit
		streamer['password'] = self.beampwLineEdit

		if beam is True or server is True:
			self.startBtn.clicked.connect(lambda: self.startbtn_db(self))  # When the button is pressed
			self.stopbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)

		else:
			query = QtSql.QSqlQuery()

			query.exec_("SELECT * FROM beam")
			while query.next():
				beamplayerunvalue = query.value(1)
				beamplayerpwvalue = query.value(2)

				streamer['username'] = beamplayerunvalue
				streamer['password'] = beamplayerpwvalue

				self.beamplayerunvalue = self.beamunLineEdit.setText(beamplayerunvalue)
				self.beamplayerpwvalue = self.beampwLineEdit.setText(beamplayerpwvalue)

			query = QtSql.QSqlQuery()

			query.exec_("SELECT * FROM server")
			while query.next():
				serverunvalue = query.value(1)
				serverhtvalue = query.value(2)
				serverptvalue = query.value(3)
				serverpwvalue = query.value(4)

				self.serverhtvalue = self.telnethostLineEdit.setText(serverhtvalue)
				self.serverptvalue = self.telnetportLineEdit.setText(str(serverptvalue))
				self.serverpwvalue = self.telnetpwLineEdit.setText(serverpwvalue)
				self.serverunvalue = self.steamidLineEdit.setText(serverunvalue)

			self.startBtn.clicked.connect(lambda: self.startbtn(self))  # When the button is pressed
			self.stopbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)

	@staticmethod
	def startbtn(self):
		print("Update DB")

		#########################################################

		server = dict(host='', port='', username='', password='')
		server["host"] = self.telnethostLineEdit.text()
		server['port'] = self.telnetportLineEdit.text()
		server['password'] = self.telnetpwLineEdit.text()
		server['username'] = self.steamidLineEdit.text()

		query = QtSql.QSqlTableModel()
		query.setTable("server")
		query.setFilter("id = 1")
		query.select()

		record = query.record(0)
		record.setValue("host", server['host'])
		record.setValue("port", server['port'])
		record.setValue("username", server['username'])
		record.setValue("password", server['password'])
		query.setRecord(0, record)
		query.submitAll()

		#####################################################

		streamer = dict(username='', password='')
		streamer['username'] = self.beamunLineEdit.text()
		streamer['password'] = self.beampwLineEdit.text()

		query = QtSql.QSqlTableModel()
		query.setTable("beam")
		query.setFilter("id = 1")
		query.select()

		record = query.record(0)
		record.setValue("username", streamer['username'])
		record.setValue("password", streamer['password'])
		query.setRecord(0, record)
		query.submitAll()

		####################################################

		wssocket.test(streamer, server)

	@staticmethod
	def startbtn_db(self):
		print("Insert into DB")

		server = dict(host='', port='', username='', password='')
		server["host"] = self.telnethostLineEdit.text()
		server['port'] = self.telnetportLineEdit.text()
		server['password'] = self.telnetpwLineEdit.text()
		server['username'] = self.steamidLineEdit.text()

		streamer = dict(username='', password='')
		streamer['username'] = self.beamunLineEdit.text()
		streamer['password'] = self.beampwLineEdit.text()

		query = QtSql.QSqlTableModel()
		query.setTable("server")
		row = 0
		query.insertRows(row, 1)
		query.setData(query.index(row, 0), 1)
		query.setData(query.index(row, 1), server['username'])
		query.setData(query.index(row, 2), server['host'])
		query.setData(query.index(row, 3), server['port'])
		query.setData(query.index(row, 4), server['password'])
		query.submitAll()

		query = QtSql.QSqlTableModel()
		query.setTable("beam")
		row = 0
		query.insertRows(row, 1)
		query.setData(query.index(row, 0), 1)
		query.setData(query.index(row, 1), streamer['username'])
		query.setData(query.index(row, 2), streamer['password'])
		query.submitAll()
		wssocket.test(streamer, server)


if __name__ == '__main__':  # if we're running file directly and not importing it
	app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
	# if not createConnection():
	# 	sys.exit(1)
	form = ExampleApp()  # We set the form to be our ExampleApp (design)
	form.show()  # Show the form
	app.exec_()  # and execute the app
