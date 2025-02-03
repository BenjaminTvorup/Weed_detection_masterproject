import os
import pandas as pd

def convert_csv_to_yolo(csv_file, image_name, output_dir, image_width, image_height):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Create the corresponding label file
    label_file = os.path.join(output_dir, f"{os.path.splitext(image_name)[0]}.txt")
    
    with open(label_file, 'w') as f:
        for _, row in df.iterrows():
            # Extract bounding box data and label ID
            left, top, right, bottom, label_id, stem_x, stem_y = row
            
            # Check if label_id is valid (0 for crop, 1 for weed)
            if label_id not in [0, 1]:
                continue  # Skip if label_id is not 0 or 1

            # Convert to YOLO format
            x_center = (left + right) / 2
            y_center = (top + bottom) / 2
            width = right - left
            height = bottom - top
            
            # Normalize values
            x_center /= image_width
            y_center /= image_height
            width /= image_width
            height /= image_height
            
            # Write to label file
            f.write(f"{label_id} {x_center} {y_center} {width} {height}\n")

# Example usage
def process_csv_files(images_directory, bboxes_directory, output_directory, image_width, image_height):
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Get a list of all CSV files
    csv_files = [f for f in os.listdir(bboxes_directory) if f.endswith('.csv')]

    for csv_file in csv_files:
        # Construct the corresponding image name
        image_name = f"{os.path.splitext(csv_file)[0]}.jpg"  # Adjust based on your image format
        csv_path = os.path.join(bboxes_directory, csv_file)

        # Convert CSV to YOLO format
        convert_csv_to_yolo(csv_path, image_name, output_directory, image_width, image_height)


# Example parameters
image_width = 1920  
image_height = 1088 

directory = directory= r"C:\Users\Benjamin Christensen\Desktop\Masterprojekt\Deep_learning\cropandweed-dataset-main\data"

images_directory = os.path.join(directory, 'images')
bboxes_directory = os.path.join(directory, 'bboxes\CropOrWeed2')
output_directory = os.path.join(directory, 'Yolo_data')

# Call the function to process CSV files
process_csv_files(images_directory, bboxes_directory, output_directory, image_width, image_height)
