import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

class Browser(QWebEngineView):
    def contextMenuEvent(self, event):
        self.menus = QMenu()
        self.menus.setStyleSheet("border-image:url(img/webbg2.png); QMenu::item::hover { text-color: rgb(30,30,30); }")
        action1 = QAction("View source code", self)
        self.menus.addAction(action1)
        self.menus.popup(event.globalPos())

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
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
        self.home_btn.triggered.connect(lambda: self.tabs.currentWidget().setUrl(QUrl('https://ishanleung.netlify.app')))
        self.navbar.addAction(self.home_btn)

        self.new_tab_btn = QAction("New Tab", self)
        self.new_tab_btn.triggered.connect(self.add_new_tab)
        self.navbar.addAction(self.new_tab_btn)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate)
        self.navbar.addWidget(self.urlbar)

        self.searchbar = QLineEdit()
        self.searchbar.returnPressed.connect(self.search)
        self.navbar.addWidget(self.searchbar)

        self.add_new_tab()

    def add_new_tab(self):
        qurl = QUrl('https://www.google.com')
        browser = QWebEngineView()
        browser.setUrl(qurl)
        browser.urlChanged.connect(self.update_urlbar)
        i = self.tabs.addTab(browser, "New Tab")
        self.tabs.setCurrentIndex(i)

    def close_tab(self, i):
        self.tabs.removeTab(i)

    def navigate(self):
        qurl = QUrl(self.urlbar.text())
        if qurl.scheme() == "":
            qurl.setScheme("http")
        self.tabs.currentWidget().setUrl(qurl)
        self.urlbar.setText(qurl.toString())

    def search(self):
        search_term = self.searchbar.text()
        url = f"https://www.google.com/search?q={search_term}"
        self.tabs.currentWidget().setUrl(QUrl(url))
        self.urlbar.setText(url)

    def update_urlbar(self, q):
        self.urlbar.setText(q.toString())

app = QApplication(sys.argv)
app.setApplicationName("Tabbed Browser")
window = MainWindow()
window.show()
app.exec_()
