#Practice linear algebra
import numpy as np

#Create 3*3 matrix
abc = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print("Original matrix:")
print(abc)

# Add 50 to each element using NumPy
abc_plus_50 = abc + 50
print("\nMatrix after adding 50:")
print(abc_plus_50)

abc_minus_20 = abc - 20
print("\nMatrix after subtracting 20:")
print(abc_minus_20)

abc_times_3 = abc * 3
print("\nMatrix after multiplying by 3:")
print(abc_times_3)

abc_divide_4 = abc / 4
print("\nMatrix after dividing by 4:")
print(abc_divide_4)

array = np.random.randint(1, 10, size=(3, 3))
print("\nRandom matrix:")
print(array)


abc1 = np.random.randint(2, 25, size=(3, 3))
print("\nAnother random matrix:")
print(abc1)

abc2 = np.random.randint(3, 50 , size=(3, 3))
print("\nYet another random matrix:")
print(abc2)

abc_sum = abc1 + abc2
print("\nSum of the two random matrices:")
print(abc_sum)

abc_diff = abc2 - abc1
print("\nDifference of the two random matrices:")
print(abc_diff)

abc_product = abc1 * abc2
print("\nElement-wise product of the two random matrices:")
print(abc_product)

abc_quotient = abc2 / abc1
print("\nElement-wise quotient of the two random matrices:")        
print(abc_quotient)


