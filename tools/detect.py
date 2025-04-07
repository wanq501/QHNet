import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('path/to/your/model.pt')  # select your model.pt path
    model.predict(source='path/to/your/input/image.png',
                  imgsz=640,
                  project='path/to/your/project_directory',
                  name='',
                  save=True,
                  classes=0
                 )