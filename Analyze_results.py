# Assuming train_results is an object that contains the following attributes
losses = train_results.losses  # Extract losses
metrics = train_results.metrics  # Extract metrics (if available)

# Print loss values
print("Training Losses:", losses)

# Extract and print specific metrics
if 'mAP' in metrics:
    print("Mean Average Precision (mAP):", metrics['mAP'])

if 'precision' in metrics:
    print("Precision:", metrics['precision'])

if 'recall' in metrics:
    print("Recall:", metrics['recall'])

# Print training time if available
if hasattr(train_results, 'training_time'):
    print("Total Training Time:", train_results.training_time)
    
    
import matplotlib.pyplot as plt

# Plotting training losses
plt.figure(figsize=(10, 5))
plt.plot(losses, label='Training Loss')
plt.title('Training Loss Over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.grid()
plt.show()

# If you have precision and recall values over epochs
precision_values = metrics.get('precision_values', [])
recall_values = metrics.get('recall_values', [])

plt.figure(figsize=(10, 5))
plt.plot(precision_values, label='Precision')
plt.plot(recall_values, label='Recall')
plt.title('Precision and Recall Over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Value')
plt.legend()
plt.grid()
plt.show()
