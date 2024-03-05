def digit_sum(num):
    return sum(map(int, str(num)))

def solution(A):
    max_sum = -1
    sum_dict = {}

    for num in A:
        digit_sum_value = digit_sum(num)
        if digit_sum_value in sum_dict:
            max_sum = max(max_sum, sum_dict[digit_sum_value] + num)
            sum_dict[digit_sum_value] = max(sum_dict[digit_sum_value], num)
        else:
            sum_dict[digit_sum_value] = num
    
    return max_sum

# Test cases
print(solution([51, 71, 17, 42])) # Output should be 93
print(solution([42, 33, 60])) # Output should be 102
print(solution([51, 32, 43])) # Output should be -1
