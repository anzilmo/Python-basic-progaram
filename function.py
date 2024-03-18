def calculate_mean(numbers):
  
    
   
    if not numbers:
        return None
    
   
    total = 0
    for num in numbers:
        total += num
    
   
    mean = total / len(numbers)
    
    return mean


numbers_list = [1, 2, 3, 4, 5]
result = calculate_mean(numbers_list)
print("Mean of the numbers:", result)
