import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert list to 3x3 numpy array
    matrix = np.array(lst).reshape(3, 3)
    
    # Calculate statistics along axes and for flattened array
    mean_axis0 = np.mean(matrix, axis=0).tolist()
    mean_axis1 = np.mean(matrix, axis=1).tolist()
    mean_flat = np.mean(matrix).item()
    
    var_axis0 = np.var(matrix, axis=0).tolist()
    var_axis1 = np.var(matrix, axis=1).tolist()
    var_flat = np.var(matrix).item()
    
    std_axis0 = np.std(matrix, axis=0).tolist()
    std_axis1 = np.std(matrix, axis=1).tolist()
    std_flat = np.std(matrix).item()
    
    max_axis0 = np.max(matrix, axis=0).tolist()
    max_axis1 = np.max(matrix, axis=1).tolist()
    max_flat = np.max(matrix).item()
    
    min_axis0 = np.min(matrix, axis=0).tolist()
    min_axis1 = np.min(matrix, axis=1).tolist()
    min_flat = np.min(matrix).item()
    
    sum_axis0 = np.sum(matrix, axis=0).tolist()
    sum_axis1 = np.sum(matrix, axis=1).tolist()
    sum_flat = np.sum(matrix).item()
    
    # Prepare the dictionary
    result = {
        'mean': [mean_axis0, mean_axis1, mean_flat],
        'variance': [var_axis0, var_axis1, var_flat],
        'standard deviation': [std_axis0, std_axis1, std_flat],
        'max': [max_axis0, max_axis1, max_flat],
        'min': [min_axis0, min_axis1, min_flat],
        'sum': [sum_axis0, sum_axis1, sum_flat]
    }
    
    return result


#from mean_var_std import calculate

result = calculate([0,1,2,3,4,5,6,7,8])
print(result)

{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}