function solution(A) {
    const targetBricks = 10;
    const n = A.length;
    let moves = 0;
    
    for (let i = 0; i < n; i++) {
        const diff = A[i] - targetBricks;
        
        if (diff > 0) {
            // Distribute excess bricks to neighboring boxes
            if (i > 0) {
                A[i - 1] += diff;
                moves += diff;
                A[i] -= diff;
            }
            if (i < n - 1) {
                const remainingMoves = Math.min(diff, A[i + 1]);
                A[i + 1] -= remainingMoves;
                moves += remainingMoves;
                A[i] -= remainingMoves;
            }
        } else if (diff < 0) {
            // Move bricks from neighboring boxes to current box
            if (i > 0) {
                const bricksToMove = Math.min(-diff, A[i - 1]);
                A[i - 1] -= bricksToMove;
                moves += bricksToMove;
                A[i] += bricksToMove;
            }
            if (i < n - 1) {
                const bricksToMove = Math.min(-diff, A[i + 1]);
                A[i + 1] -= bricksToMove;
                moves += bricksToMove;
                A[i] += bricksToMove;
            }
        }
    }
    
    // Check if all boxes have exactly 10 bricks
    for (let i = 0; i < n; i++) {
        if (A[i] !== targetBricks) {
            return -1;
        }
    }
    
    return moves;
}

// Test cases
console.log(solution([7, 15, 10, 8])); // Output: 7
console.log(solution([11, 10, 8, 12, 8, 10, 11])); // Output: 6
console.log(solution([7, 14, 10])); // Output: -1
