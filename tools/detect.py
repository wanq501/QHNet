import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('path/to/your/model.pt')  # select your model.pt path
    model.predict(source='path/to/your/input/image.png',
                  imgsz=640,
                  project='/root/QHNet/run',
                  name='detect',
                  save=True,
                  classes=0
                 )