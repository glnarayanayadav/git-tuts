import numpy as np

# Original 1D array
arr = np.arange(12) # Creates an array from 0 to 11
print(f"Original Array:\n{arr}")
print(f"Original Shape: {arr.shape}\n")

# Reshape to a 2x6 matrix
arr_reshaped_2x6 = arr.reshape(2, 6)
print(f"Reshaped to (2, 6):\n{arr_reshaped_2x6}")
print(f"Shape: {arr_reshaped_2x6.shape}\n")

# Reshape to a 3x4 matrix
arr_reshaped_3x4 = arr.reshape(3, 4)
print(f"Reshaped to (3, 4):\n{arr_reshaped_3x4}")
print(f"Shape: {arr_reshaped_3x4.shape}\n")

# Reshape to a 2x2x3 3D array
arr_reshaped_2x2x3 = arr.reshape(2, 2, 3)
print(f"Reshaped to (2, 2, 3):\n{arr_reshaped_2x2x3}")
print(f"Shape: {arr_reshaped_2x2x3.shape}\n")

# Using -1 to infer one dimension
arr_reshaped_auto_rows = arr.reshape(-1, 4) # 4 columns, infer rows
print(f"Reshaped to (-1, 4):\n{arr_reshaped_auto_rows}")
print(f"Shape: {arr_reshaped_auto_rows.shape}\n")

arr_reshaped_auto_cols = arr.reshape(3, -1) # 3 rows, infer columns
print(f"Reshaped to (3, -1):\n{arr_reshaped_auto_cols}")
print(f"Shape: {arr_reshaped_auto_cols.shape}\n")

# Reshaping to a single row or column vector
# To make a 1D array explicitly a 2D row vector (1 row, many columns)
arr_row_vector = arr.reshape(1, -1)
print(f"Reshaped to row vector (1, -1):\n{arr_row_vector}")
print(f"Shape: {arr_row_vector.shape}\n")

# To make a 1D array explicitly a 2D column vector (many rows, 1 column)
arr_col_vector = arr.reshape(-1, 1)
print(f"Reshaped to column vector (-1, 1):\n{arr_col_vector}")
print(f"Shape: {arr_col_vector.shape}\n")