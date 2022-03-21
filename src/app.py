from PyQt6.QtWidgets import QApplication, QWidget


def main():
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle('Sorting Visualization')
    window.setGeometry(100, 100, 280, 80)
    window.move(60, 15)
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
