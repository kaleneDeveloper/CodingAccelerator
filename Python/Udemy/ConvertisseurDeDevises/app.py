from PySide2 import QtWidgets
import currency_converter

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.c = currency_converter.CurrencyConverter()
        self.setWindowTitle("Currency converter")
        self.setup_UI()
        self.set_default_values()
        self.setup_connection()
        self.setup_css()
    
    def setup_UI(self):
        self.layout = QtWidgets.QHBoxLayout(self)
        self.cbb_currencyFrom = QtWidgets.QComboBox()
        self.spn_amount = QtWidgets.QSpinBox()
        self.cbb_currencyTo = QtWidgets.QComboBox()
        self.spn_converterAmount = QtWidgets.QSpinBox()
        self.btn_invert = QtWidgets.QPushButton("Invert currency")
        
        self.layout.addWidget(self.cbb_currencyFrom)
        self.layout.addWidget(self.spn_amount)
        self.layout.addWidget(self.cbb_currencyTo)
        self.layout.addWidget(self.spn_converterAmount)
        self.layout.addWidget(self.btn_invert)
        
        self.layout2 = QtWidgets.QVBoxLayout(self)
        self.cbb_currencyFrom2 = QtWidgets.QComboBox()
        self.spn_amount2 = QtWidgets.QSpinBox()
        self.cbb_currencyTo2 = QtWidgets.QComboBox()
        self.spn_converterAmount2 = QtWidgets.QSpinBox()
        self.btn_invert2 = QtWidgets.QPushButton("Invert currency2")
        
        self.layout2.addWidget(self.cbb_currencyFrom2)
        self.layout2.addWidget(self.spn_amount2)
        self.layout2.addWidget(self.cbb_currencyTo2)
        self.layout2.addWidget(self.spn_converterAmount2)
        self.layout2.addWidget(self.btn_invert2)

    def set_default_values(self):
        self.cbb_currencyFrom.addItems(sorted(list(self.c.currencies)))
        self.cbb_currencyTo.addItems(sorted(list(self.c.currencies)))
        self.cbb_currencyFrom.setCurrentText("EUR")
        self.cbb_currencyTo.setCurrentText("EUR")
        
        self.spn_amount.setRange(1, 1000000)
        self.spn_converterAmount.setRange(1, 1000000)
        self.spn_amount.setValue(100)
        self.spn_converterAmount.setValue(100)
   
    def setup_connection(self):
        self.cbb_currencyFrom.activated.connect(self.compute)
        self.cbb_currencyTo.activated.connect(self.compute)
        
        self.spn_amount.valueChanged.connect(self.compute)
        self.spn_converterAmount.valueChanged.connect(self.compute)
        
        self.btn_invert.clicked.connect(self.invert_currency)
    
    def compute(self):
        amount = self.spn_amount.value() # Take value insert
        # converterAmount = self.spn_converterAmount.value()
        currency_from = self.cbb_currencyFrom.currentText() # Take currency
        currency_to = self.cbb_currencyTo.currentText() # Take currency
        try:
            result_from_to = self.c.convert(amount, currency_from, currency_to)
        except currency_converter.currency_converter.RateNotFoundError:
            print("Conversion did not work.")
        else:
            self.spn_converterAmount.setValue(result_from_to)
            # self.spn_amount.setValue(result_to_from)
    
    def invert_currency(self):
        currency_from = self.cbb_currencyFrom.currentText()
        currency_to = self.cbb_currencyTo.currentText()
        
        self.cbb_currencyFrom.setCurrentText(currency_to)
        self.cbb_currencyTo.setCurrentText(currency_from)
        self.compute()

    def setup_css(self):
        self.setStyleSheet("""
        background-color: rgb(50, 50 ,50); 
        color: rgb(240, 240, 240);             
        """)
        self.btn_invert.setStyleSheet("background-color:(60, 60 ,60);")
            
app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()
 