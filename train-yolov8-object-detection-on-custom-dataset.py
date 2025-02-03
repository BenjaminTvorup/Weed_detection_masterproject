# https://docs.ultralytics.com/quickstart/#install-ultralytics

# 1. : Anaconda prompt
# git clone https://github.com/ultralytics/ultralytics.git
# pip install ultralytics
# 2.cd ultralytics
# 3. python -m venv yolov8-env
# 4. yolov8-env\Scripts\activate
#
#
#
#
#
#
#
#


from IPython import display
display.clear_output()

import ultralytics
ultralytics.checks()
from ultralytics import YOLO
import torch

   

import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# You can try to change to yolo11n.pt
model = YOLO("yolov8n.pt")  # Load a pretrained model (change to yolov8s.pt, yolov8m.pt, etc.)

device = "cuda" if torch.cuda.is_available() else "cpu"


train_results = model.train(
    data=r"C:\Users\Benjamin Christensen\Desktop\Masterprojekt\Deep_learning\cropandweed-dataset-main\data\Dataset_configuration_file_for_YOLOv8.yaml",  # Path to your dataset YAML file
    epochs=10, #100
    imgsz=640,
    device=device,
)


# Evaluate model performance on the validation set
metrics = model.val()
print(metrics)


# Perform object detection on an image
results = model(r"C:\Users\Benjamin Christensen\Desktop\Masterprojekt\Deep_learning\cropandweed-dataset-main\data\images\ave-0035-0003.jpg")  # Replace with the path to your image
results[0].show()  # Display the results

# Export the model to ONNX format
path = model.export(format="onnx")  # Export the model and get the path to the exported model
print(f"Model exported to: {path}")

