values = [3,6,9,12,15,18,21,24]
other_values = [5,10,15,20,25,30]

def odd_sum(numbers):
    total_sum = 0
    for number in numbers:
        if number % 2 == 1:
            total_sum += number
    return total_sum
            
print(odd_sum(values))
print(odd_sum(other_values))

def greatest_number(numbers):
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest
            
    
print(greatest_number([1,2,3]))
print(greatest_number([3,2,1]))
print(greatest_number([4,5,5]))
print(greatest_number([-3,-2,-1]))