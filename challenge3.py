import string

def solution(N):
    letters = string.ascii_lowercase
    letter_count = N // 26
    remainder = N % 26
    
    if remainder == 0:
        return letters * letter_count
    else:
        return letters[:remainder] + letters * letter_count

# Test cases
print(solution(3))
print(solution(5))
print(solution(30))
