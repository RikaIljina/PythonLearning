import sys
from qtpy import QtWidgets, QtGui
from pathlib import Path
from BatchRenamer import BatchRenamer
from renamer_ui.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)


# TODO: implement sequential rename
# TODO: implement add suffix
# TODO: implement the rename logic
# TODO: implement "delete file name" and "delete part of file name" logic


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(770, 630)

        self.files_object = BatchRenamer()

        self.file_paths = []

        self.ui.pushButton_browse.clicked.connect(self.browse)
        self.ui.pushButton_update.clicked.connect(self.update_result)
        self.ui.pushButton_up.clicked.connect(self.move_entry_up)
        self.ui.pushButton_down.clicked.connect(self.move_entry_down)
        self.ui.pushButton_del.clicked.connect(self.delete_entry)
        self.ui.pushButton_sort.clicked.connect(self.sort)

    def list_selected_files(self):

        for path in self.file_paths:
            # convert each path to Windows path
            path = Path(path)
            # files_object is a BatchRenamer instance. It is used for all logic concerning the renaming.
            # a list in files_object will hold all paths
            self.files_object.add_path(path)
            # we only want to show the names of the files in the widget
            path_name = path.name
            # adding each path name to the listWidget
            self.ui.listWidget_selected.addItem(path_name)

        # selecting first item in the widget
        self.ui.listWidget_selected.setCurrentRow(0)

    def browse(self):
        # open a Browse dialog where user can select files
        # these files are converted to a list, we need only the first element (second element contains the extension)
        self.file_paths = list(QtWidgets.QFileDialog.getOpenFileNames(self, 'Choose files to rename', '.', '*.*',))[0]
        # the file paths overwrite previously added file_paths

        # if user has selected files, call function to show them in listWidget
        if len(self.file_paths) != 0:
            self.list_selected_files()

    def move_entry_up(self):
        row = self.ui.listWidget_selected.currentRow()

        if row >= 1:
            item = self.ui.listWidget_selected.takeItem(row)
            self.ui.listWidget_selected.insertItem(row-1, item)
            self.ui.listWidget_selected.setCurrentItem(item)
            self.files_object.move_up(row)
        self.debugprint()

    def debugprint(self):
        print(self.file_paths)
        print(self.files_object.get_paths())

    def move_entry_down(self):
        row = self.ui.listWidget_selected.currentRow()
        self.debugprint()

        if row < self.ui.listWidget_selected.count() - 1:
            item = self.ui.listWidget_selected.takeItem(row)
            self.ui.listWidget_selected.insertItem(row+1, item)
            self.ui.listWidget_selected.setCurrentItem(item)
            self.files_object.move_down(row)
        self.debugprint()

    def delete_entry(self):
        row = self.ui.listWidget_selected.currentRow()
        item = self.ui.listWidget_selected.takeItem(row)
        self.files_object.del_path(row)
        del item
        self.debugprint()

    def sort(self):
        self.ui.listWidget_selected.sortItems()
        self.files_object.sort_paths()
        self.debugprint()

    def update_result(self):
        self.ui.listWidget_results.clear()

        prefix = self.ui.lineEdit_user_prefix.text()
        prefix = self.files_object.check_prefix(prefix)
        self.ui.lineEdit_user_prefix.setText(prefix)

        for path in self.files_object.user_paths:

            path_name = prefix + path.name
            self.ui.listWidget_results.addItem(path_name)

        self.debugprint()


window = MainWindow()
window.show()


sys.exit(app.exec_())
