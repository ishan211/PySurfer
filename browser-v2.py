from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.navbar = QToolBar("Navigation")
        self.addToolBar(self.navbar)

        self.back_btn = QAction("Back", self)
        self.back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
        self.navbar.addAction(self.back_btn)

        self.forward_btn = QAction("Forward", self)
        self.forward_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
        self.navbar.addAction(self.forward_btn)

        self.reload_btn = QAction("Reload", self)
        self.reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
        self.navbar.addAction(self.reload_btn)

        self.home_btn = QAction("Home", self)
        self.home_btn.triggered.connect(lambda: self.tabs.currentWidget().setUrl(QUrl('https://www.google.com')))
        self.navbar.addAction(self.home_btn)

        self.new_tab_btn = QAction("New Tab", self)
        self.new_tab_btn.triggered.connect(self.add_new_tab)
        self.navbar.addAction(self.new_tab_btn)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate)
        self.navbar.addWidget(self.urlbar)

        self.add_new_tab()

    def add_new_tab(self, qurl=None):
        if qurl is None:
            qurl = QUrl('https://www.google.com')

        browser = QWebEngineView()
        browser.setUrl(qurl)

        i = self.tabs.addTab(browser, "New Tab")
        self.tabs.setCurrentIndex(i)

    def navigate(self):
        qurl = QUrl(self.urlbar.text())
        if qurl.scheme() == "":
            qurl.setScheme("http")
        self.tabs.currentWidget().setUrl(qurl)

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
