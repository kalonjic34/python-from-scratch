# def count_down_from(number):
#     start = number
#     while start >  0:
#         print(start)
#         start -= 1
        
def count_down_from(number):
    if number <= 0:
        return
    else:
        print(number)
        count_down_from(number -1)

print(count_down_from(5))