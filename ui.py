from PyQt5 import QtCore, QtGui, QtWidgets
from deepface import DeepFace, models
import os
import cv2
import time



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):


        self.ref_file = ""
        self.target_files = []
        self.output_folder = ""
        self.is_extracting = False
        self.extracting_index = -1


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Background = QtWidgets.QLabel(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.Background.setStyleSheet("background-color: white;")
        self.Background.setText("")
        self.Background.setObjectName("Background")

        self.LeftTop = QtWidgets.QLabel(self.centralwidget)
        self.LeftTop.setGeometry(QtCore.QRect(0, 0, 300, 300))
        self.LeftTop.setStyleSheet("border: 3px solid rgb(186, 186, 186);")
        self.LeftTop.setText("")
        self.LeftTop.setObjectName("LeftTop")

        self.Right = QtWidgets.QLabel(self.centralwidget)
        self.Right.setGeometry(QtCore.QRect(600, 0, 200, 600))
        self.Right.setStyleSheet("border: 3px solid rgb(186, 186, 186);\n""")
        self.Right.setFrameShape(QtWidgets.QFrame.Box)
        self.Right.setLineWidth(5)
        self.Right.setText("")
        self.Right.setObjectName("Right")

        self.Button1Ref = QtWidgets.QPushButton(self.centralwidget)
        self.Button1Ref.setGeometry(QtCore.QRect(608, 15, 180, 50))
        self.Button1Ref.setStyleSheet("QPushButton {\n""background: rgb(245,245,245);\n""border: 1px solid rgb(230,230,230);\n""color: black;\n""border-radius: 10px;\n""}\n""\n""QPushButton:hover {\n""background: rgb(250,250,250);\n""}\n""\n""QPushButton:pressed {\n""background: rgb(230, 230, 230);\n""}")
        self.Button1Ref.setObjectName("Button1Ref")
        self.Button1Ref.clicked.connect(self.loadRef)

        self.Button2Tar = QtWidgets.QPushButton(self.centralwidget)
        self.Button2Tar.setGeometry(QtCore.QRect(608, 75, 180, 50))
        self.Button2Tar.setStyleSheet("QPushButton {\n""background: rgb(245,245,245);\n""border: 1px solid rgb(230,230,230);\n""color: black;\n""border-radius: 10px;\n""}\n""\n""QPushButton:hover {\n""background: rgb(250,250,250);\n""}\n""\n""QPushButton:pressed {\n""background: rgb(230, 230, 230);\n""}")
        self.Button2Tar.setObjectName("Button2Tar")
        self.Button2Tar.clicked.connect(self.loadTars)

        self.Button3Fol = QtWidgets.QPushButton(self.centralwidget)
        self.Button3Fol.setGeometry(QtCore.QRect(608, 135, 180, 50))
        self.Button3Fol.setStyleSheet("QPushButton {\n""background: rgb(245,245,245);\n""border: 1px solid rgb(230,230,230);\n""color: black;\n""border-radius: 10px;\n""}\n""\n""QPushButton:hover {\n""background: rgb(250,250,250);\n""}\n""\n""QPushButton:pressed {\n""background: rgb(230, 230, 230);\n""}")
        self.Button3Fol.setObjectName("Button3Fol")
        self.Button3Fol.clicked.connect(self.selectFolder)

        self.Button4Ext = QtWidgets.QPushButton(self.centralwidget)
        self.Button4Ext.setGeometry(QtCore.QRect(608, 195, 180, 50))
        self.Button4Ext.setStyleSheet("QPushButton {\n""background: rgb(245,245,245);\n""border: 1px solid rgb(230,230,230);\n""color: black;\n""border-radius: 10px;\n""}\n""\n""QPushButton:hover {\n""background: rgb(250,250,250);\n""}\n""\n""QPushButton:pressed {\n""background: rgb(230, 230, 230);\n""}")
        self.Button4Ext.setObjectName("Button3Ext")
        self.Button4Ext.clicked.connect(self.startExtract)

        self.SelFolderLabel = QtWidgets.QLabel(self.centralwidget)
        self.SelFolderLabel.setGeometry(QtCore.QRect(608, 260, 180, 100))
        self.SelFolderLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.SelFolderLabel.setText(f"선택된 폴더:<br>{self.output_folder}")
        self.SelFolderLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.SelFolderLabel.setStyleSheet("color: black;\n""border: none\n")
        self.SelFolderLabel.setWordWrap(True)
        self.SelFolderLabel.setObjectName("SelFolderLabel")

        self.MidTop = QtWidgets.QLabel(self.centralwidget)
        self.MidTop.setGeometry(QtCore.QRect(300, 0, 300, 300))
        self.MidTop.setStyleSheet("border: 3px solid rgb(186, 186, 186);\n")
        self.MidTop.setText("")
        self.MidTop.setObjectName("MidTop")

        self.MidTopText = QtWidgets.QListWidget(self.centralwidget)
        self.MidTopText.setGeometry(QtCore.QRect(305, 10, 290, 285))
        self.MidTopText.setStyleSheet("color: black;\n""background-color: white;\n""border: none;\n")

        self.LeftBottom = QtWidgets.QLabel(self.centralwidget)
        self.LeftBottom.setGeometry(QtCore.QRect(0, 300, 300, 300))
        self.LeftBottom.setStyleSheet("border: 3px solid rgb(186, 186, 186);")
        self.LeftBottom.setText("")
        self.LeftBottom.setObjectName("LeftBottom")

        self.MidBottom = QtWidgets.QLabel(self.centralwidget)
        self.MidBottom.setGeometry(QtCore.QRect(300, 300, 300, 300))
        self.MidBottom.setStyleSheet("border: 3px solid rgb(186, 186, 186);\n")
        self.MidBottom.setText("")
        self.MidBottom.setObjectName("MidBottom")

        self.BackgroundNoRad = QtWidgets.QLabel(self.centralwidget)
        self.BackgroundNoRad.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.BackgroundNoRad.setStyleSheet("background-color: none;\n""border: 4px solid rgb(186,186,186);")
        self.BackgroundNoRad.setText("")
        self.BackgroundNoRad.setObjectName("BackgroundNoRad")

        self.BackgroundRad = QtWidgets.QLabel(self.centralwidget)
        self.BackgroundRad.setGeometry(QtCore.QRect(1, 1, 798, 598))
        self.BackgroundRad.setStyleSheet("background-color: none;\n""border: 5px solid rgb(186,186,186);\n""border-radius: 10px;")
        self.BackgroundRad.setText("")
        self.BackgroundRad.setObjectName("BackgroundRad")

        self.LeftTopImage = QtWidgets.QLabel(self.centralwidget)
        self.LeftTopImage.setGeometry(QtCore.QRect(6, 5, 291, 290))
        self.LeftTopImage.setText("")
        self.LeftTopImage.setObjectName("LeftTopImage")

        self.LeftBottomImage = QtWidgets.QLabel(self.centralwidget)
        self.LeftBottomImage.setGeometry(QtCore.QRect(6, 305, 291, 290))
        self.LeftBottomImage.setText("")
        self.LeftBottomImage.setObjectName("LeftBottomImage")

        self.MidBottomImage = QtWidgets.QLabel(self.centralwidget)
        self.MidBottomImage.setGeometry(QtCore.QRect(306, 305, 291, 290))
        self.MidBottomImage.setText("")
        self.MidBottomImage.setObjectName("MidBottomImage")

        self.Background.raise_()
        self.BackgroundRad.raise_()
        self.BackgroundNoRad.raise_()
        self.LeftTop.raise_()
        self.Right.raise_()
        self.Button1Ref.raise_()
        self.Button2Tar.raise_()
        self.Button3Fol.raise_()
        self.Button4Ext.raise_()
        self.SelFolderLabel.raise_()
        self.MidTop.raise_()
        self.MidTopText.raise_()
        self.LeftBottom.raise_()
        self.MidBottom.raise_()
        self.LeftTopImage.raise_()
        self.LeftBottomImage.raise_()
        self.MidBottomImage.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button1Ref.setText(_translate("MainWindow", "비교 파일 불러오기"))
        self.Button2Tar.setText(_translate("MainWindow", "대상 파일 불러오기"))
        self.Button3Fol.setText(_translate("MainWindow", "추출 폴더 선택하기"))
        self.Button4Ext.setText(_translate("MainWindow", "추출 시작"))



    def loadRef(self):
        options = QtWidgets.QFileDialog.Options()
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(None, "이미지 파일 선택", "", "Images (*.png *.xpm *.jpg)", options=options)
        if file_name:
            self.ref_file = file_name
            pixmap = QtGui.QPixmap(file_name)
            self.LeftTopImage.setPixmap(pixmap.scaled(self.LeftTopImage.size(), QtCore.Qt.KeepAspectRatio))  # 이미지 크기에 맞게 조정
            self.LeftTopImage.setAlignment(QtCore.Qt.AlignCenter)  # 이미지 중앙 정렬
        else:
            QtWidgets.QMessageBox.warning(None, "Warning", "파일을 선택하지 않았습니다.")


    def loadTars(self):
        options = QtWidgets.QFileDialog.Options()
        file_names, _ = QtWidgets.QFileDialog.getOpenFileNames(None, "이미지 파일 선택", "", "Images (*.png *.xpm *.jpg)", options=options)
        if file_names:
            self.target_files = file_names
            self.MidTopText.clear()  # 리스트 초기화
            for file_name in file_names:
                print(file_name)
                item = QtWidgets.QListWidgetItem(file_name)
                self.MidTopText.addItem(item)
        else:
            QtWidgets.QMessageBox.warning(None, "Warning", "파일을 선택하지 않았습니다.")


    def selectFolder(self):
        options = QtWidgets.QFileDialog.Options()
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(None, "폴더 선택", "", options=options)
        if folder_path:
            self.output_folder = folder_path
            self.SelFolderLabel.setText(f"선택된 폴더: {self.output_folder}")
            print(f"선택된 폴더: {folder_path}")
        else:
            QtWidgets.QMessageBox.warning(None, "Warning", "폴더를 선택하지 않았습니다.")


    def startExtract(self):
        if self.ref_file == "" or self.target_files == []:
            QtWidgets.QMessageBox.warning(None, "Warning", "파일을 모두 선택하지 않았습니다.")
            return 0
        if self.output_folder == "":
            QtWidgets.QMessageBox.warning(None, "Warning", "폴더를 선택하지 않았습니다.")
            return 0


        self.extract_thread = ExtractThread(self.ref_file, self.target_files, self.output_folder)
        self.extract_thread.update_target_image.connect(self.updateLeftBottomImage)
        self.extract_thread.update_output_image.connect(self.updateMidBottomImage)
        self.extract_thread.log_message.connect(self.logMessage)

        self.extract_thread.start()


    def updateLeftBottomImage(self, pixmap):
        self.LeftBottomImage.setPixmap(pixmap.scaled(self.LeftBottomImage.size(), QtCore.Qt.KeepAspectRatio))
        self.LeftBottomImage.setAlignment(QtCore.Qt.AlignCenter)

    def updateMidBottomImage(self, pixmap):
        self.MidBottomImage.setPixmap(pixmap.scaled(self.MidBottomImage.size(), QtCore.Qt.KeepAspectRatio))
        self.MidBottomImage.setAlignment(QtCore.Qt.AlignCenter)

    def logMessage(self, message):
        print(message)

        # self.extracting_index = 0
        #
        # while self.extracting_index < len(self.target_files):
        #     target_file = self.target_files[self.extracting_index]
        #
        #     pixmap = QtGui.QPixmap(target_file)
        #     self.LeftBottomImage.setPixmap(pixmap.scaled(self.LeftBottomImage.size(), QtCore.Qt.KeepAspectRatio))  # 이미지 크기에 맞게 조정
        #     self.LeftBottomImage.setAlignment(QtCore.Qt.AlignCenter)
        #
        #     target_img = cv2.imread(target_file)
        #
        #     result = DeepFace.verify(img1_path=self.ref_file,
        #                              img2_path=target_file,
        #                              detector_backend='retinaface',
        #                              model_name='ArcFace'
        #                              )
        #     if result['verified']:
        #         print(f"얼굴 일치")
        #         try:
        #             faces = DeepFace.extract_faces(img_path=target_file, detector_backend='retinaface')
        #             if faces:
        #                 for face_info in faces:
        #                     facial_area = face_info['facial_area']
        #                     x, y, w, h = facial_area['x'], facial_area['y'], facial_area['w'], facial_area['h']
        #
        #                     padding_x = int(w * 2.5)
        #                     padding_y = int(h * 3)
        #
        #                     center_x = x + w // 2
        #                     center_y = y + h // 2
        #
        #                     new_x = max(0, center_x - padding_x // 2)
        #                     new_y = max(0, center_y - padding_y // 2)
        #                     new_w = min(target_img.shape[1] - new_x, padding_x)
        #                     new_h = min(target_img.shape[0] - new_y, padding_y)
        #
        #                     cropped_img = target_img[new_y:new_y + new_h, new_x:new_x + new_w]
        #                     if 'windows' in platform.system().lower():
        #                         output_path = self.output_folder + "\\resized_" + os.path.basename(target_file)
        #                     else:
        #                         output_path = self.output_folder + "/resized_" + os.path.basename(target_file)
        #
        #                     cv2.imwrite(output_path, cropped_img)
        #                     pixmap = QtGui.QPixmap(output_path)
        #                     self.MidBottomImage.setPixmap(pixmap.scaled(self.MidBottomImage.size(), QtCore.Qt.KeepAspectRatio))  # 이미지 크기에 맞게 조정
        #                     self.MidBottomImage.setAlignment(QtCore.Qt.AlignCenter)
        #                     print(f"  - Resized image saved to {output_path}")
        #                     break
        #         except Exception as e:
        #             print(f"  - Face extraction failed for {target_file}: {e}")
        #     else:
        #         print(f"[NO MATCH] {target_file}: Face Did Not Match.")
        #     self.extracting_index += 1

class ExtractThread(QtCore.QThread):
    update_target_image = QtCore.pyqtSignal(QtGui.QPixmap)
    update_output_image = QtCore.pyqtSignal(QtGui.QPixmap)
    log_message = QtCore.pyqtSignal(str)

    def __init__(self, ref_file, target_files, output_folder):
        super().__init__()
        self.ref_file = ref_file
        self.target_files = target_files
        self.output_folder = output_folder

    def run(self):
        for target_file in self.target_files:
            pixmap = QtGui.QPixmap(target_file)
            self.update_target_image.emit(pixmap)

            try:
                target_img = cv2.imread(target_file)
                result = DeepFace.verify(
                    img1_path=self.ref_file,
                    img2_path=target_file,
                    detector_backend='retinaface',
                    model_name='ArcFace'
                )

                if result['verified']:
                    faces = DeepFace.extract_faces(img_path=target_file, detector_backend='retinaface')
                    if faces:
                        for face_info in faces:
                            facial_area = face_info['facial_area']
                            x, y, w, h = facial_area['x'], facial_area['y'], facial_area['w'], facial_area['h']

                            padding_x = int(w * 2.5)
                            padding_y = int(h * 3)

                            center_x = x + w // 2
                            center_y = y + h // 2

                            new_x = max(0, center_x - padding_x // 2)
                            new_y = max(0, center_y - padding_y // 2)
                            new_w = min(target_img.shape[1] - new_x, padding_x)
                            new_h = min(target_img.shape[0] - new_y, padding_y)

                            cropped_img = target_img[new_y:new_y + new_h, new_x:new_x + new_w]
                            output_path = os.path.join(self.output_folder, f"resized_{os.path.basename(target_file)}")
                            cv2.imwrite(output_path, cropped_img)

                            output_pixmap = QtGui.QPixmap(output_path)
                            self.update_output_image.emit(output_pixmap)
                            self.log_message.emit(f"Resized image saved to {output_path}")
                            time.sleep(1)
                            break
                else:
                    self.log_message.emit(f"[NO MATCH] {target_file}: Face Did Not Match.")
            except Exception as e:
                self.log_message.emit(f"Face extraction failed for {target_file}: {e}")


        QtCore.QMetaObject.invokeMethod(
            self,
            "exec_warning_message",
            QtCore.Qt.QueuedConnection,
        )

    @QtCore.pyqtSlot()
    def exec_warning_message(self):
        QtWidgets.QMessageBox.warning(None, "Completed", "작업이 완료되었습니다.")




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
