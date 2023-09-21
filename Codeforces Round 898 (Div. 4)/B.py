def max_product(n, digits):
    min_digit = min(digits)
    min_digit_index = digits.index(min_digit)
    digits[min_digit_index] += 1
    
    product = 1
    for digit in digits:
        product *= digit
    
    return product

t = int(input())

for _ in range(t):
    n = int(input())  
    digits = list(map(int, input().split()))  
    
    result = max_product(n, digits)
    print(result)
