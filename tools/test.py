from ultralytics import YOLO

if __name__ == '__main__':
    # Load a model

    model = YOLO(r'/path/to/your/QHNet_1.0/ultralytics/cfg/models/QHNet_N.yaml')  
   
    model.info()

