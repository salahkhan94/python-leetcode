import numpy as np
import matplotlib.pyplot as plt

# Create a 16×16 "dummy" image (just for visualization).
# Here, we'll fill it with values from 0 to 255 in row-major order,
# but you can use any 16×16 data you like.
image = np.arange(256).reshape(16, 16)

# Create a figure and axis for plotting
fig, ax = plt.subplots(figsize=(5, 5))

# Display the image
cax = ax.imshow(image, cmap='gray', origin='upper', interpolation='nearest')

# Draw the grid lines that separate each 4×4 cell
# We'll draw horizontal and vertical lines at multiples of 4
for i in range(0, 17, 4):
    ax.axhline(y=i - 0.5, color='red', linewidth=2)  # horizontal lines
    ax.axvline(x=i - 0.5, color='red', linewidth=2)  # vertical lines

# Label each 4×4 cell with a number
cell_count = 1
for row_block in range(4):        # 4 blocks vertically
    for col_block in range(4):    # 4 blocks horizontally
        # Compute the center of the current 4×4 cell to place the text
        center_x = col_block * 4 + 2
        center_y = row_block * 4 + 2
        
        # Place a label (e.g., "1", "2", ..., "16") in the cell center
        ax.text(center_x, center_y, str(cell_count), 
                color='blue', ha='center', va='center', fontsize=12)
        
        cell_count += 1

# A title for clarity
ax.set_title("16×16 Window Subdivided into 4×4 Cells (Each Cell = 4×4)")

# Remove axis ticks for a cleaner look (optional)
ax.set_xticks([])
ax.set_yticks([])

# Show the plot
plt.show()
