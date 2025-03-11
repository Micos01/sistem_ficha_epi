# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ficha_epioPkbAv.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QTableView,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(879, 577)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"QCheckBox {\n"
"    padding: 2px;\n"
"}\n"
"QCheckBox:hover {\n"
"    border: 1px solid rgb(255,150,60);\n"
"    border-radius: 4px;\n"
"    padding: 1px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(190, 90, 50, 50), stop:1 rgba(250, 130, 40, 50));\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    border: 1px solid rgb(246, 134, 86);\n"
"    border-radius: 4px;\n"
"    background-color: rgb(246, 134, 86);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    border-width: 1px solid rgb(246, 134, 86);\n"
"    border-radius: 4px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QColorDialog {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"QComboBox {\n"
"    color: rgb(81,72,65);\n"
"    background: #ffffff;\n"
"}\n"
"QComboBox:editable {\n"
"    selection-color: rgb(81,72,65);\n"
"    selection-background-color: #ffffff;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    selection-color: #ffffff;\n"
"    sel"
                        "ection-background-color: rgb(246, 134, 86);\n"
"}\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    color: #1e1d23;\n"
"}\n"
"QDateTimeEdit, QDateEdit, QDoubleSpinBox, QFontComboBox {\n"
"    color: rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}\n"
"QDialog {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"QLabel,QLineEdit {\n"
"    color: rgb(17,17,17);\n"
"}\n"
"QLineEdit {\n"
"    background-color: rgb(255,255,255);\n"
"    selection-background-color: rgb(236,116,64);\n"
"}\n"
"QMenuBar {\n"
"    color: rgb(223,219,210);\n"
"    background-color: rgb(65,64,59);\n"
"}\n"
"QMenuBar::item {\n"
"    padding-top: 4px;\n"
"    padding-left: 4px;\n"
"    padding-right: 4px;\n"
"    color: rgb(223,219,210);\n"
"    background-color: rgb(65,64,59);\n"
"}\n"
"QMenuBar::item:selected {\n"
"    color: rgb(255,255,255);\n"
"    padding-top: 2px;\n"
"    padding-left: 2px;\n"
"    padding-right: 2px;\n"
"    border-top-width: 2px;\n"
"    border-left-width: 2px;\n"
"    border-right-width: 2px;"
                        "\n"
"    border-top-right-radius: 4px;\n"
"    border-top-left-radius: 4px;\n"
"    border-style: solid;\n"
"    background-color: rgb(65,64,59);\n"
"    border-top-color: rgb(47,47,44);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(90, 87, 78, 255), stop:1 rgba(47,47,44, 255));\n"
"    border-left-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(90, 87, 78, 255), stop:1 rgba(47,47,44, 255));\n"
"}\n"
"QMenu {\n"
"    color: rgb(223,219,210);\n"
"    background-color: rgb(65,64,59);\n"
"}\n"
"QMenu::item {\n"
"    color: rgb(223,219,210);\n"
"    padding: 4px 10px 4px 20px;\n"
"}\n"
"QMenu::item:selected {\n"
"    color: rgb(255,255,255);\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(225, 108, 54, 255), stop:1 rgba(246, 134, 86, 255));\n"
"    border-style: solid;\n"
"    border-width: 3px;\n"
"    padding: 4px 7px 4px 17px;\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x"
                        "2:0.5, y2:0, stop:0 rgba(175,85,48,255), stop:1 rgba(236,114,67, 255));\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"    border-left-color: qlineargradient(spread:pad, x1:1, y1:0.5, x2:0, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"}\n"
"QPlainTextEdit {\n"
"    border: 1px solid transparent;\n"
"    color: rgb(17,17,17);\n"
"    selection-background-color: rgb(236,116,64);\n"
"    background-color: #FFFFFF;\n"
"}\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(0, 0, 0);\n"
"    border: 1px inset rgb(150,150,150);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(221,221,219);\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(225,"
                        " 108, 54, 255), stop:1 rgba(246, 134, 86, 255));\n"
"    border: 1px solid;\n"
"    border-radius: 8px;\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(175,85,48,255), stop:1 rgba(236,114,67, 255));\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"    border-left-color: qlineargradient(spread:pad, x1:1, y1:0.5, x2:0, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"}\n"
"QPushButton {\n"
"    color: rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-bottom-color: rgb(150,150,150);\n"
"    border-right-color: rgb(165,165,165);\n"
"    border-left-color: rgb(165,165,165);\n"
"    border-top-color: rgb(180,180,180);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"  "
                        "  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	text-align:left;\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-top-color: rgb(255,150,60);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"    border-left-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"    border-bottom-color: rgb(200,70,20);\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:default {\n"
"    color: rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-top-color: rgb(255,150,60);\n"
"    border"
                        "-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"    border-left-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"    border-bottom-color: rgb(200,70,20);\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:pressed {\n"
"    color: rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-top-color: rgba(255,150,60,200);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 200));\n"
"    border-left-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 200));\n"
"    border-bottom-color: rgba(200,70,20,200);\n"
"    borde"
                        "r-style: solid;\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:disabled {\n"
"    color: rgb(174,167,159);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(200, 200, 200, 255), stop:1 rgba(230, 230, 230, 255));\n"
"}\n"
"QRadioButton {\n"
"    padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 1px;\n"
"    border-color: rgba(246, 134, 86, 255);\n"
"    color: #a9b7c6;\n"
"    background-color: rgba(246, 134, 86, 255);\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 1px;\n"
"    border-color: rgb(246, 134, 86);\n"
"    color: "
                        "#a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QScrollArea {\n"
"    color: white;\n"
"    background-color: #f0f0f0;\n"
"}\n"
"QSlider::groove {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background: rgb(246, 134, 86);\n"
"}\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    background: rgb(246, 134, 86);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    width: 12px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    height: 12px;\n"
"    margin: 0 -5px;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal, QSlider::add-page:vertical {\n"
"    backgroun"
                        "d: white;\n"
"}\n"
"QSlider::sub-page:horizontal, QSlider::sub-page:vertical {\n"
"    background: rgb(246, 134, 86);\n"
"}\n"
"QStatusBar, QSpinBox {\n"
"    color: rgb(81,72,65);\n"
"}\n"
"QSpinBox {\n"
"    background-color: #ffffff;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    max-height: 20px;\n"
"    border: 1px transparent;\n"
"    margin: 0px 20px 0px 20px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(253,253,253);\n"
"    border: 1px solid rgb(207,207,207);\n"
"    border-radius: 7px;\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: rgb(253,253,253);\n"
"    border: 1px solid rgb(255,150,60);\n"
"    border-radius: 7px;\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: 1px solid rgb(207,207,207);\n"
"    border-top-right-radius: 7px;\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    background: rgb(255, 255, 255);\n"
"    width: 20px;\n"
"    subcontrol-position: right;\n"
""
                        "    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {\n"
"    border: 1px solid rgb(255,150,60);\n"
"    border-top-right-radius: 7px;\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    background: rgb(255, 255, 255);\n"
"    width: 20px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"    border: 1px solid grey;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    background: rgb(231,231,231);\n"
"    width: 20px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: 1px solid rgb(207,207,207);\n"
"    border-top-right-radius: 7px;\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    background: rgb(255, 255, 255);\n"
"    width: 20px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origi"
                        "n: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"    border: 1px solid rgb(255,150,60);\n"
"    border-top-right-radius: 7px;\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    background: rgb(255, 255, 255);\n"
"    width: 20px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"    border: 1px solid grey;\n"
"    border-top-right-radius: 7px;\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    background: rgb(231,231,231);\n"
"    width: 20px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::left-arrow:horizontal {\n"
"    border: 1px transparent grey;\n"
"    border-top-left-radius: 3px;\n"
"    border-bottom-left-radius: 3px;\n"
"    width: 6px;\n"
"    height: 6px;\n"
"    background: rgb(230,230,230);\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"    border: 1px transparent grey;\n"
"    border-top-rig"
                        "ht-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    width: 6px;\n"
"    height: 6px;\n"
"    background: rgb(230,230,230);\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar:vertical {\n"
"    max-width: 20px;\n"
"    border: 1px transparent grey;\n"
"    margin: 20px 0px 20px 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border: 1px solid;\n"
"    border-color: rgb(207,207,207);\n"
"    border-bottom-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-top-left-radius: 7px;\n"
"    background: rgb(255, 255, 255);\n"
"    height: 20px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {\n"
"    border: 1px solid;\n"
"    border-color: rgb(255,150,60);\n"
"    border-bottom-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-top-left-radius: 7px;\n"
"    background: rgb(255, 255, 255);\n"
"    height: 20px;\n"
""
                        "    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {\n"
"    border: 1px solid grey;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    border-top-left-radius: 7px;\n"
"    background: rgb(231,231,231);\n"
"    height: 20px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    border: 1px solid rgb(207,207,207);\n"
"    border-top-right-radius: 7px;\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    background: rgb(255, 255, 255);\n"
"    height: 20px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {\n"
"    border: 1px solid rgb(255,150,60);\n"
"    border-top-right-radius: 7px;\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    background: rgb(255, 255, 255);\n"
"    height: 20px;\n"
"    subcontrol-positi"
                        "on: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"    border: 1px solid grey;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    background: rgb(231,231,231);\n"
"    height: 20px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(253,253,253);\n"
"    border: 1px solid rgb(207,207,207);\n"
"    border-radius: 7px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgb(253,253,253);\n"
"    border: 1px solid rgb(255,150,60);\n"
"    border-radius: 7px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::up-arrow:vertical {\n"
"    border: 1px transparent grey;\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    width: 6px;\n"
"    height: 6px;\n"
"    background: rgb(230,230,230);\n"
"}\n"
"QScrollBar::down-arrow:vertical {\n"
"    border: 1px transparent grey;\n"
"    border-bottom-"
                        "left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    width: 6px;\n"
"    height: 6px;\n"
"    background: rgb(230,230,230);\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"QTabWidget {\n"
"    color: rgb(0,0,0);\n"
"    background-color: rgb(247,246,246);\n"
"}\n"
"QTabWidget::pane {\n"
"    border-color: rgb(180,180,180);\n"
"    background-color: rgb(247,246,246);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"}\n"
"QTabBar::tab {\n"
"    padding-left: 4px;\n"
"    padding-right: 4px;\n"
"    padding-bottom: 2px;\n"
"    padding-top: 2px;\n"
"    color: rgb(81,72,65);\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(221,218,217,255), stop:1 rgba(240,239,238,255));\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-top-right-radius: 4px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-color: rgb(180,180,180);\n"
"    border"
                        "-left-color: rgb(180,180,180);\n"
"    border-right-color: rgb(180,180,180);\n"
"    border-bottom-color: transparent;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"    background-color: rgb(247,246,246);\n"
"    margin-left: 0px;\n"
"    margin-right: 1px;\n"
"}\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 1px;\n"
"    margin-right: 1px;\n"
"}\n"
"QTextEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: transparent;\n"
"    color: rgb(17,17,17);\n"
"    selection-background-color: rgb(236,116,64);\n"
"}\n"
"QTimeEdit, QToolBox, QToolBox::tab, QToolBox::tab:selected {\n"
"    color: rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.label)

        self.pages = QStackedWidget(self.frame_2)
        self.pages.setObjectName(u"pages")
        self.tabelas_page = QWidget()
        self.tabelas_page.setObjectName(u"tabelas_page")
        self.horizontalLayout_3 = QHBoxLayout(self.tabelas_page)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tabWidget = QTabWidget(self.tabelas_page)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.horizontalLayout_11 = QHBoxLayout(self.tab_5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_10 = QLabel(self.tab_5)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_10.addWidget(self.label_10)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.line_pesquisa_ficha = QLineEdit(self.tab_5)
        self.line_pesquisa_ficha.setObjectName(u"line_pesquisa_ficha")

        self.horizontalLayout_7.addWidget(self.line_pesquisa_ficha)

        self.cb_revazer_ficha = QComboBox(self.tab_5)
        self.cb_revazer_ficha.setObjectName(u"cb_revazer_ficha")

        self.horizontalLayout_7.addWidget(self.cb_revazer_ficha)

        self.btn_pesquisar_colaborador = QPushButton(self.tab_5)
        self.btn_pesquisar_colaborador.setObjectName(u"btn_pesquisar_colaborador")

        self.horizontalLayout_7.addWidget(self.btn_pesquisar_colaborador)

        self.btn_refazer_ficha = QPushButton(self.tab_5)
        self.btn_refazer_ficha.setObjectName(u"btn_refazer_ficha")

        self.horizontalLayout_7.addWidget(self.btn_refazer_ficha)

        self.btn_remover = QPushButton(self.tab_5)
        self.btn_remover.setObjectName(u"btn_remover")

        self.horizontalLayout_7.addWidget(self.btn_remover)

        self.btn_abrir_banco = QPushButton(self.tab_5)
        self.btn_abrir_banco.setObjectName(u"btn_abrir_banco")

        self.horizontalLayout_7.addWidget(self.btn_abrir_banco)

        self.btn_fechar_banco = QPushButton(self.tab_5)
        self.btn_fechar_banco.setObjectName(u"btn_fechar_banco")

        self.horizontalLayout_7.addWidget(self.btn_fechar_banco)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.tw_historico_fichas = QTableView(self.tab_5)
        self.tw_historico_fichas.setObjectName(u"tw_historico_fichas")
        self.tw_historico_fichas.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.EditKeyPressed)
        self.tw_historico_fichas.horizontalHeader().setCascadingSectionResizes(False)
        self.tw_historico_fichas.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout_10.addWidget(self.tw_historico_fichas)


        self.horizontalLayout_11.addLayout(self.verticalLayout_10)

        self.frame_4 = QFrame(self.tab_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_9.addWidget(self.label_5)

        self.cb_funcao = QComboBox(self.frame_4)
        self.cb_funcao.setObjectName(u"cb_funcao")

        self.verticalLayout_9.addWidget(self.cb_funcao)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_9.addWidget(self.label_6)

        self.cb_setor = QComboBox(self.frame_4)
        self.cb_setor.setObjectName(u"cb_setor")

        self.verticalLayout_9.addWidget(self.cb_setor)

        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_9.addWidget(self.label_7)

        self.le_admissao = QLineEdit(self.frame_4)
        self.le_admissao.setObjectName(u"le_admissao")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_admissao.sizePolicy().hasHeightForWidth())
        self.le_admissao.setSizePolicy(sizePolicy1)

        self.verticalLayout_9.addWidget(self.le_admissao)

        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_9.addWidget(self.label_8)

        self.le_integracao = QLineEdit(self.frame_4)
        self.le_integracao.setObjectName(u"le_integracao")
        sizePolicy1.setHeightForWidth(self.le_integracao.sizePolicy().hasHeightForWidth())
        self.le_integracao.setSizePolicy(sizePolicy1)

        self.verticalLayout_9.addWidget(self.le_integracao)

        self.label_12 = QLabel(self.frame_4)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_9.addWidget(self.label_12)

        self.line_nome = QLineEdit(self.frame_4)
        self.line_nome.setObjectName(u"line_nome")
        sizePolicy1.setHeightForWidth(self.line_nome.sizePolicy().hasHeightForWidth())
        self.line_nome.setSizePolicy(sizePolicy1)

        self.verticalLayout_9.addWidget(self.line_nome)

        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_9.addWidget(self.label_13)

        self.line_cpf = QLineEdit(self.frame_4)
        self.line_cpf.setObjectName(u"line_cpf")
        sizePolicy1.setHeightForWidth(self.line_cpf.sizePolicy().hasHeightForWidth())
        self.line_cpf.setSizePolicy(sizePolicy1)

        self.verticalLayout_9.addWidget(self.line_cpf)

        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_9.addWidget(self.label_11)

        self.line_tam_uniforme = QLineEdit(self.frame_4)
        self.line_tam_uniforme.setObjectName(u"line_tam_uniforme")
        sizePolicy1.setHeightForWidth(self.line_tam_uniforme.sizePolicy().hasHeightForWidth())
        self.line_tam_uniforme.setSizePolicy(sizePolicy1)

        self.verticalLayout_9.addWidget(self.line_tam_uniforme)

        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_9.addWidget(self.label_9)

        self.line_tam_sapato = QLineEdit(self.frame_4)
        self.line_tam_sapato.setObjectName(u"line_tam_sapato")
        sizePolicy1.setHeightForWidth(self.line_tam_sapato.sizePolicy().hasHeightForWidth())
        self.line_tam_sapato.setSizePolicy(sizePolicy1)

        self.verticalLayout_9.addWidget(self.line_tam_sapato)

        self.btn_gerar_ficha_epi = QPushButton(self.frame_4)
        self.btn_gerar_ficha_epi.setObjectName(u"btn_gerar_ficha_epi")

        self.verticalLayout_9.addWidget(self.btn_gerar_ficha_epi)


        self.horizontalLayout_11.addWidget(self.frame_4)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_7 = QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.scrollArea = QScrollArea(self.tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -1139, 789, 1588))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.le_pesquisa_config = QLineEdit(self.scrollAreaWidgetContents)
        self.le_pesquisa_config.setObjectName(u"le_pesquisa_config")

        self.horizontalLayout_4.addWidget(self.le_pesquisa_config)

        self.btn_pesquisa_config = QPushButton(self.scrollAreaWidgetContents)
        self.btn_pesquisa_config.setObjectName(u"btn_pesquisa_config")

        self.horizontalLayout_4.addWidget(self.btn_pesquisa_config)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.tv_funcao = QTableView(self.scrollAreaWidgetContents)
        self.tv_funcao.setObjectName(u"tv_funcao")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tv_funcao.sizePolicy().hasHeightForWidth())
        self.tv_funcao.setSizePolicy(sizePolicy2)
        self.tv_funcao.setMinimumSize(QSize(0, 350))
        self.tv_funcao.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.EditKeyPressed|QAbstractItemView.EditTrigger.SelectedClicked)

        self.verticalLayout_3.addWidget(self.tv_funcao)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMaximumSize(QSize(250, 16777215))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.cb_select_func_config = QComboBox(self.frame_3)
        self.cb_select_func_config.setObjectName(u"cb_select_func_config")
        self.cb_select_func_config.setMaximumSize(QSize(132, 16777215))

        self.verticalLayout.addWidget(self.cb_select_func_config)

        self.label_14 = QLabel(self.frame_3)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout.addWidget(self.label_14)

        self.le_add_func_config = QLineEdit(self.frame_3)
        self.le_add_func_config.setObjectName(u"le_add_func_config")
        sizePolicy1.setHeightForWidth(self.le_add_func_config.sizePolicy().hasHeightForWidth())
        self.le_add_func_config.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.le_add_func_config)

        self.label_15 = QLabel(self.frame_3)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout.addWidget(self.label_15)

        self.le_add_uniforme_config = QLineEdit(self.frame_3)
        self.le_add_uniforme_config.setObjectName(u"le_add_uniforme_config")
        sizePolicy1.setHeightForWidth(self.le_add_uniforme_config.sizePolicy().hasHeightForWidth())
        self.le_add_uniforme_config.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.le_add_uniforme_config)

        self.btn_add_item_config = QPushButton(self.frame_3)
        self.btn_add_item_config.setObjectName(u"btn_add_item_config")

        self.verticalLayout.addWidget(self.btn_add_item_config)

        self.btn_remover_config = QPushButton(self.frame_3)
        self.btn_remover_config.setObjectName(u"btn_remover_config")

        self.verticalLayout.addWidget(self.btn_remover_config)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.le_pesquisa_config_2 = QLineEdit(self.scrollAreaWidgetContents)
        self.le_pesquisa_config_2.setObjectName(u"le_pesquisa_config_2")

        self.horizontalLayout_6.addWidget(self.le_pesquisa_config_2)

        self.btn_pesquisa_config_2 = QPushButton(self.scrollAreaWidgetContents)
        self.btn_pesquisa_config_2.setObjectName(u"btn_pesquisa_config_2")

        self.horizontalLayout_6.addWidget(self.btn_pesquisa_config_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.tv_funcao_2 = QTableView(self.scrollAreaWidgetContents)
        self.tv_funcao_2.setObjectName(u"tv_funcao_2")
        self.tv_funcao_2.setMinimumSize(QSize(0, 350))

        self.verticalLayout_6.addWidget(self.tv_funcao_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_6)

        self.frame_5 = QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMaximumSize(QSize(250, 16777215))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.label_16 = QLabel(self.frame_5)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_5.addWidget(self.label_16)

        self.le_funcao_original_config = QLineEdit(self.frame_5)
        self.le_funcao_original_config.setObjectName(u"le_funcao_original_config")
        sizePolicy1.setHeightForWidth(self.le_funcao_original_config.sizePolicy().hasHeightForWidth())
        self.le_funcao_original_config.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.le_funcao_original_config)

        self.label_17 = QLabel(self.frame_5)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_5.addWidget(self.label_17)

        self.le_funcao_ficha_config = QLineEdit(self.frame_5)
        self.le_funcao_ficha_config.setObjectName(u"le_funcao_ficha_config")
        sizePolicy1.setHeightForWidth(self.le_funcao_ficha_config.sizePolicy().hasHeightForWidth())
        self.le_funcao_ficha_config.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.le_funcao_ficha_config)

        self.btn_add_func_config_2 = QPushButton(self.frame_5)
        self.btn_add_func_config_2.setObjectName(u"btn_add_func_config_2")

        self.verticalLayout_5.addWidget(self.btn_add_func_config_2)

        self.btn_remover_config_2 = QPushButton(self.frame_5)
        self.btn_remover_config_2.setObjectName(u"btn_remover_config_2")

        self.verticalLayout_5.addWidget(self.btn_remover_config_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)


        self.horizontalLayout_5.addWidget(self.frame_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.le_pesquisa_setor_config = QLineEdit(self.scrollAreaWidgetContents)
        self.le_pesquisa_setor_config.setObjectName(u"le_pesquisa_setor_config")

        self.horizontalLayout_9.addWidget(self.le_pesquisa_setor_config)

        self.btn_pesquisa_setor_config = QPushButton(self.scrollAreaWidgetContents)
        self.btn_pesquisa_setor_config.setObjectName(u"btn_pesquisa_setor_config")

        self.horizontalLayout_9.addWidget(self.btn_pesquisa_setor_config)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.tv_setor = QTableView(self.scrollAreaWidgetContents)
        self.tv_setor.setObjectName(u"tv_setor")
        self.tv_setor.setMinimumSize(QSize(0, 350))
        self.tv_setor.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.EditKeyPressed|QAbstractItemView.EditTrigger.SelectedClicked)

        self.verticalLayout_8.addWidget(self.tv_setor)


        self.horizontalLayout_8.addLayout(self.verticalLayout_8)

        self.frame_6 = QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(250, 16777215))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_11.addWidget(self.label_4)

        self.label_18 = QLabel(self.frame_6)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_11.addWidget(self.label_18)

        self.le_add_Setor_config = QLineEdit(self.frame_6)
        self.le_add_Setor_config.setObjectName(u"le_add_Setor_config")
        sizePolicy1.setHeightForWidth(self.le_add_Setor_config.sizePolicy().hasHeightForWidth())
        self.le_add_Setor_config.setSizePolicy(sizePolicy1)

        self.verticalLayout_11.addWidget(self.le_add_Setor_config)

        self.btn_add_setor_config = QPushButton(self.frame_6)
        self.btn_add_setor_config.setObjectName(u"btn_add_setor_config")

        self.verticalLayout_11.addWidget(self.btn_add_setor_config)

        self.btn_remover_setor_config = QPushButton(self.frame_6)
        self.btn_remover_setor_config.setObjectName(u"btn_remover_setor_config")

        self.verticalLayout_11.addWidget(self.btn_remover_setor_config)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_2)


        self.horizontalLayout_8.addWidget(self.frame_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.le_pesquisa_local_config = QLineEdit(self.scrollAreaWidgetContents)
        self.le_pesquisa_local_config.setObjectName(u"le_pesquisa_local_config")

        self.horizontalLayout_12.addWidget(self.le_pesquisa_local_config)

        self.btn_pesquisa_local_config = QPushButton(self.scrollAreaWidgetContents)
        self.btn_pesquisa_local_config.setObjectName(u"btn_pesquisa_local_config")

        self.horizontalLayout_12.addWidget(self.btn_pesquisa_local_config)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)

        self.tv_local = QTableView(self.scrollAreaWidgetContents)
        self.tv_local.setObjectName(u"tv_local")
        self.tv_local.setMinimumSize(QSize(0, 350))
        self.tv_local.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.EditKeyPressed|QAbstractItemView.EditTrigger.SelectedClicked)

        self.verticalLayout_12.addWidget(self.tv_local)


        self.horizontalLayout_10.addLayout(self.verticalLayout_12)

        self.frame_7 = QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(250, 16777215))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_7)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_19 = QLabel(self.frame_7)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_13.addWidget(self.label_19)

        self.label_20 = QLabel(self.frame_7)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_13.addWidget(self.label_20)

        self.le_add_Setor_config_2 = QLineEdit(self.frame_7)
        self.le_add_Setor_config_2.setObjectName(u"le_add_Setor_config_2")
        sizePolicy1.setHeightForWidth(self.le_add_Setor_config_2.sizePolicy().hasHeightForWidth())
        self.le_add_Setor_config_2.setSizePolicy(sizePolicy1)

        self.verticalLayout_13.addWidget(self.le_add_Setor_config_2)

        self.btn_add_local = QPushButton(self.frame_7)
        self.btn_add_local.setObjectName(u"btn_add_local")

        self.verticalLayout_13.addWidget(self.btn_add_local)

        self.btn_remover_local = QPushButton(self.frame_7)
        self.btn_remover_local.setObjectName(u"btn_remover_local")

        self.verticalLayout_13.addWidget(self.btn_remover_local)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_4)


        self.horizontalLayout_10.addWidget(self.frame_7)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_7.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.tab, "")

        self.horizontalLayout_3.addWidget(self.tabWidget)

        self.pages.addWidget(self.tabelas_page)

        self.verticalLayout_2.addWidget(self.pages)


        self.horizontalLayout_2.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Ficha de EPI</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Hist\u00f3rico de Fichas", None))
        self.btn_pesquisar_colaborador.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.btn_refazer_ficha.setText(QCoreApplication.translate("MainWindow", u"Refazer", None))
        self.btn_remover.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        self.btn_abrir_banco.setText(QCoreApplication.translate("MainWindow", u"Abrir banco", None))
        self.btn_fechar_banco.setText(QCoreApplication.translate("MainWindow", u"Fechar banco", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Selecione o cargo:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Selecione o setor:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Data de Admiss\u00e3o:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Data de Integra\u00e7\u00e3o:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Nome do colaborador:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"CPF:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Tamanho Uniforme", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Tamanho Sapato:", None))
        self.btn_gerar_ficha_epi.setText(QCoreApplication.translate("MainWindow", u"Gerar Ficha de EPI", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Ficha de EPI", None))
        self.btn_pesquisa_config.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Uniformes</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Criar Fun\u00e7\u00e3o:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Uniforme:", None))
        self.btn_add_item_config.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.btn_remover_config.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        self.btn_pesquisa_config_2.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Fun\u00e7\u00f5es</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Fun\u00e7\u00e3o original:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Fun\u00e7\u00e3o na ficha:", None))
        self.btn_add_func_config_2.setText(QCoreApplication.translate("MainWindow", u"Adicionar ", None))
        self.btn_remover_config_2.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        self.btn_pesquisa_setor_config.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Setores</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Setor:", None))
        self.btn_add_setor_config.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.btn_remover_setor_config.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        self.btn_pesquisa_local_config.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Locais da Planilha:</p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Local:", None))
        self.btn_add_local.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.btn_remover_local.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es Ficha", None))
    # retranslateUi

