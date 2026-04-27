num = list(range(1, 51))

# 2. Define the squaring function
def square_num(n):
    return n ** 2

def get_square(num_list):
    
    all_num = filter(lambda x: True, num_list)
    
    # Use map to square each element returned by the filter
    squared_list = map(square_num, all_num)
    
    return list(squared_list)

# Execute and print results
result = get_square(num)
print(f"Squared list: {result}")