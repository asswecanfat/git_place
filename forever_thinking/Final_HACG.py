from HCAG_UI import *

class Myapp(Ui_Form):
    def __init__(self, Form):
        super(Myapp, self).setupUi(Form)

    def get_data(self):
        self.progressBar.setValue(100)
        # print(self.)

if __name__=="__main__":
    import sys

    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    # ui=Ui_Form()
    # ui.setupUi(widget)
    Myapp(widget)
    widget.show()
    sys.exit(app.exec_())
