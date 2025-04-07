from ultralytics import YOLO

if __name__ == '__main__':
    # Load model
    model = YOLO(r'path/to/your/model_weights.pt')
    # Validate model
    metrics = model.val(
        val=True,  # (bool) Perform validation/testing during training
        data=r'path/to/your/dataset_config.yaml',
        split='val',  # (str) Dataset split for validation ('val', 'test', or 'train')
        batch=1,  # (int) Number of images per batch (-1 for automatic batching)
        imgsz=640,  # (int or tuple) Input image size (e.g., 640 or (width, height))
        device='0',  # Device to run on, e.g., cuda device=0 or device=cpu
        workers=8,  # Number of worker threads for data loading (per DDP process)
        save_json=False,  # Save results to a JSON file
        save_hybrid=False,  # Save hybrid version of labels (labels + additional predictions)
        conf=0.001,  # Confidence threshold for object detection (default 0.25 for prediction, 0.001 for validation)
        iou=0.6,  # Intersection over Union (IoU) threshold for Non-Maximum Suppression (NMS)
        project='path/to/your/project_directory',  # Project directory name (optional)
        name='your_experiment_name',  # Experiment name; results saved in 'project/name' directory (optional)
        max_det=300,  # Maximum number of detections per image
        half=False,  # Use half-precision (FP16)
        dnn=False,  # Use OpenCV DNN for ONNX inference
        plots=True,  # Save images during training/validation
    )

    print(f"mAP50-95: {metrics.box.map}")  # Mean Average Precision from 0.50 to 0.95 IoU
    print(f"mAP50: {metrics.box.map50}")   # Mean Average Precision at IoU=0.50
    print(f"mAP75: {metrics.box.map75}")   # Mean Average Precision at IoU=0.75
    speed_metrics = metrics.speed
    total_time = sum(speed_metrics.values())
    fps = 1000 / total_time
    print(f"FPS: {fps}")  # Frames Per Second
