from ultralytics import YOLO

if __name__ == '__main__':
    # Load a model

    model = YOLO(r'/path/to/your/QHNet/main/cfg/models/QHNet_N.yaml')  
   
    model.info()

