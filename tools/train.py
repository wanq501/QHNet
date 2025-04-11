import sys
sys.path.append("/root/ultralytics")
from ultralytics import YOLO

if __name__ == '__main__':
    # Load model：Training without pretrained weights
    model = YOLO(r'/root/QHNet/ultralytics/cfg/models/QHNet_N.yaml')  
  
    # Training parameters ----------------------------------------------------------------------------------------------
    model.train(
        data=r'/root/QHNet/dateset/DUT_Anti-UAV_YOLO.yaml',
        resume=False,  # Resume training from last checkpoint
        epochs=200,  # Number of epochs for training
        patience=50,  # Number of epochs with no improvement after which training stops early
        batch=100,  # Number of images per batch (-1 for automatic batch size)
        imgsz=640,  # Input image size, integer or w,h
        save=True,  # Save training checkpoints and prediction results
        save_period=-1,  # Save checkpoint every x epochs (disabled if < 1)
        cache=False,  # True/ram, disk, or False. Use cache for data loading
        device='',  # Device to run, e.g., cuda device=0, device=0,1,2,3 or device=cpu
        workers=8,  # Number of worker threads for data loading (per DDP process)
        project='/root/QHNet/run',  # Project directory name
        name='train',  # Experiment name; results saved in 'project/name' directory
        exist_ok=False,  # Overwrite existing experiment
        pretrained=True,  # Use pretrained model weights (bool) or specify model to load weights from (str)
        optimizer='SGD',  # Optimizer to use [SGD, Adam, Adamax, AdamW, NAdam, RAdam, RMSProp, auto]
        verbose=True,  # Print detailed output
        seed=0,  # Random seed for reproducibility
        deterministic=True,  # Enable deterministic mode
        single_cls=False,  # Train multi-class data as single-class
        rect=False,  # Rectangular training if mode='train' or rectangular validation if mode='val'
        cos_lr=False,  # Use cosine learning rate scheduler
        close_mosaic=0,  # Disable mosaic augmentation for the last epochs
        amp=True,  # Automatic Mixed Precision (AMP) training
        fraction=1.0,  # Fraction of dataset used for training (1.0 means all images)
        profile=False,  # Enable ONNX and TensorRT profiling during training
        freeze=None,  # Freeze the first n layers during training or provide list of layer indices
        # Segmentation parameters
        overlap_mask=True,  # Whether masks should overlap during training (segmentation training only)
        mask_ratio=4,  # Mask downsampling ratio (segmentation training only)
        # Classification parameters
        dropout=0.0,  # Dropout regularization (classification training only)
        # Hyperparameters ----------------------------------------------------------------------------------------------
        lr0=0.01,  # Initial learning rate (e.g., SGD=1E-2, Adam=1E-3)
        lrf=0.01,  # Final learning rate (lr0 * lrf)
        momentum=0.937,  # SGD momentum/Adam beta1
        weight_decay=0.0005,  # Optimizer weight decay
        warmup_epochs=3.0,  # Warmup epochs (fractional allowed)
        warmup_momentum=0.8,  # Warmup initial momentum
        warmup_bias_lr=0.1,  # Warmup initial bias learning rate
        box=7.5,  # Box loss gain
        cls=0.5,  # Class loss gain
        dfl=1.5,  # DFL loss gain
        pose=12.0,  # Pose loss gain
        kobj=1.0,  # Keypoint object loss gain
        label_smoothing=0.0,  # Label smoothing
        nbs=64,  # Nominal batch size
        hsv_h=0.015,  # Image HSV-Hue augmentation (fraction)
        hsv_s=0.7,  # Image HSV-Saturation augmentation (fraction)
        hsv_v=0.4,  # Image HSV-Value augmentation (fraction)
        degrees=0.0,  # Image rotation (+/- degrees)
        translate=0.1,  # Image translation (+/- fraction)
        scale=0.5,  # Image scaling (+/- gain)
        shear=0.0,  # Image shearing (+/- degrees)
        perspective=0.0,  # Image perspective (+/- fraction), range 0-0.001
        flipud=0.0,  # Vertical flip probability
        fliplr=0.5,  # Horizontal flip probability
        mosaic=1.0,  # Mosaic augmentation probability
        mixup=0.0,  # Mixup augmentation probability
        copy_paste=0.0,  # Segmentation copy-paste probability
    )
