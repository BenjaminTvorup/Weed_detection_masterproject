import os
import random
import shutil

# Configuration
dataset_dir = r"C:\Users\Benjamin Christensen\Desktop\Masterprojekt\Deep_learning\cropandweed-dataset-main\data"  # Base directory
images_dir = os.path.join(dataset_dir, 'images')  # Directory containing images
labels_dir = os.path.join(dataset_dir, 'Yolo_data')  # Directory containing YOLO labels
train_dir = os.path.join(dataset_dir, 'train')  # Directory for training images and labels
valid_dir = os.path.join(dataset_dir, 'valid')  # Directory for validation images and labels
train_file = os.path.join(dataset_dir, 'train.txt')  # File listing training images
valid_file = os.path.join(dataset_dir, 'valid.txt')  # File listing validation images
names_file = os.path.join(dataset_dir, 'classes.names')  # File for class names
data_file = os.path.join(dataset_dir, 'data.data')  # Data configuration file

# Create directories for training and validation sets
os.makedirs(train_dir, exist_ok=True)
os.makedirs(valid_dir, exist_ok=True)

# Get list of all images and labels
image_files = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]
label_files = [f for f in os.listdir(labels_dir) if f.endswith('.txt')]

# Create a set of label file names without extensions for easy checking
label_file_names = {os.path.splitext(label)[0] for label in label_files}

# Filter image files to only include those with corresponding label files
valid_image_files = [img for img in image_files if os.path.splitext(img)[0] in label_file_names]

# Shuffle and split the dataset into training and validation sets (80% train, 20% valid)
random.shuffle(valid_image_files)
split_index = int(len(valid_image_files) * 0.8)
train_images = valid_image_files[:split_index]
valid_images = valid_image_files[split_index:]

# Move images and labels to the respective directories
for img in train_images:
    # Copy image
    shutil.copy(os.path.join(images_dir, img), train_dir)
    
    # Prepare label file name
    label_file = img.replace('.jpg', '.txt').replace('.png', '.txt').replace('.jpeg', '.txt')
    label_path = os.path.join(labels_dir, label_file)

    # Copy label file
    shutil.copy(label_path, train_dir)

for img in valid_images:
    # Copy image
    shutil.copy(os.path.join(images_dir, img), valid_dir)
    
    # Prepare label file name
    label_file = img.replace('.jpg', '.txt').replace('.png', '.txt').replace('.jpeg', '.txt')
    label_path = os.path.join(labels_dir, label_file)

    # Copy label file
    shutil.copy(label_path, valid_dir)

# Create train.txt and valid.txt files
with open(train_file, 'w') as f:
    for img in train_images:
        f.write(f"{os.path.join(train_dir, img)}\n")

with open(valid_file, 'w') as f:
    for img in valid_images:
        f.write(f"{os.path.join(valid_dir, img)}\n")

# Create classes.names file
with open(names_file, 'w') as f:
    f.write("crop\n")
    f.write("weed\n")

# Create data.data file
with open(data_file, 'w') as f:
    f.write(f"classes = 2\n")
    f.write(f"train = {train_file}\n")
    f.write(f"valid = {valid_file}\n")
    f.write(f"names = {names_file}\n")
    f.write(f"backup = {os.path.join(dataset_dir, 'backup/')}\n")  # Adjust backup path as needed

print("Dataset preparation complete!")