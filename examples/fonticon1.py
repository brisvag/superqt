try:
    from fonticon_fa5 import FA5S
except ImportError as e:
    raise type(e)(
        "This example requires the fontawesome fontpack:\n\n"
        "pip install git+https://github.com/tlambert03/fonticon-fontawesome5.git"
    )

from superqt.fonticon import icon, pulse
from superqt.qtcompat.QtCore import QSize
from superqt.qtcompat.QtWidgets import QApplication, QPushButton

app = QApplication([])

btn2 = QPushButton()
btn2.setIcon(icon(FA5S.spinner, animation=pulse(btn2)))
btn2.setIconSize(QSize(225, 225))
btn2.show()

app.exec()
