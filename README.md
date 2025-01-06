파이썬 버전: 3.0~3.11(Tensorflow 2.14.1때문에)  
pip install deepface tensorflow==2.14.1  
faceRecognition.py 처음 실행하면 알아서 ArcFace 다운로드하고 실행함.  
빌드 명령어: pyinstaller --onefile --hidden-import deepface faceRecognition.py
