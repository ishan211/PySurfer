from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QVBoxLayout, QWidget, QLineEdit, QPushButton, QHBoxLayout, QAction, QMenu, QMenuBar, QToolBar
from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtGui import QIcon, QColor, QGradient, QLinearGradient, QPalette
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ISHAN-Ternet Explorer")
        self.setGeometry(100, 100, 1200, 800)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        
        # Central Widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction("Forward", self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction("Home", self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

        # Menu
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        new_tab_action = QAction("New Tab", self)
        new_tab_action.triggered.connect(self.add_new_tab)
        file_menu.addAction(new_tab_action)

        bookmarks_menu = QMenu("Bookmarks", self)
        file_menu.addMenu(bookmarks_menu)

        history_menu = QMenu("History", self)
        file_menu.addMenu(history_menu)

        save_passwords_action = QAction("Save Passwords", self)
        file_menu.addAction(save_passwords_action)

        # Customizable Theme
        self.apply_custom_theme()

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://www.google.com"))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, url):
        self.url_bar.setText(url.toString())

    def add_new_tab(self):
        new_tab = QWebEngineView()
        new_tab.setUrl(QUrl("https://www.google.com"))
        self.tabs.addTab(new_tab, "New Tab")

    def apply_custom_theme(self):
        palette = QPalette()
        gradient = QLinearGradient(0, 0, 1, 1)
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QColor(255, 0, 0))
        gradient.setColorAt(1.0, QColor(0, 0, 255))
        palette.setBrush(QPalette.Window, gradient)
        self.setPalette(palette)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Browser()
    window.show()
    sys.exit(app.exec_())
