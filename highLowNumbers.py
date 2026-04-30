
def high_and_low(numbers):
    nums = list(map(int, numbers.split()))
    
    highest = max(nums)
    lowest = min(nums)
    
    return f"{highest} {lowest}"


print(high_and_low("1 2 -3 4 5"))



