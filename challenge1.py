def solution(A):
    N = len(A)
    target_bricks = 10
    moves = 0
    
    for i in range(N):
        if A[i] == target_bricks:
            continue
        elif A[i] < target_bricks:
            diff = target_bricks - A[i]
            if i < N - 1:
                A[i+1] -= diff
                moves += diff
            else:
                return -1
        else:
            diff = A[i] - target_bricks
            if i < N - 1:
                A[i+1] += diff
                moves += diff
            else:
                return -1
                
    return moves

# Test cases
print(solution([7, 15, 10, 8])) # Output should be 7
print(solution([11, 10, 8, 12, 8, 10, 11])) # Output should be 6
print(solution([7, 14, 10])) # Output should be -1
