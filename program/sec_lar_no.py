def second_large(numbers):
    numbers=set(numbers)
    numbers=( sorted(numbers) )
    print(numbers)
    return numbers[-2]
nums = [10, 20, 4, 10, 45, 99] 
print(second_large(nums))