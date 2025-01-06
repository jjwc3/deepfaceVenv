pip install deepface tensorflow==2.14.1  
faceRecognition.py 처음 실행하면 알아서 ArcFace 다운로드하고 실행함.  
빌드 명령어: pyinstaller --onefile --hidden-import deepface faceRecognition.py
