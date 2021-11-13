def solution(A):
    max_even = 0
    max_odd = 0

    for i in A:
        if i % 2 == 0:
            max_even = max(i, max_even)
        else:
            max_odd = max(i, max_odd)
    
    return max_even + max_odd


# ------------------------------------------
def solution(S):
    blocks = []
    block = S[0]
    answer = 0
    
    for i in range(1, len(S)):
        if block[-1] == S[i]:
            block += S[i]
        else:
            blocks.append(block)
            block = S[i]
    
    if block:
        blocks.append(block)
    
    blocks = sorted(blocks, key=lambda x: -(len(x)))
    
    max_block_length = len(blocks[0])

    for i in blocks:
        answer += (max_block_length - len(i))
    
    return answer


# -----------------------------------------------------
from collections import Counter

def solution(A):
    num_counter = Counter(A)
    answer = 0

    for i in num_counter.items():
        answer += min(i[1], abs(i[0]-i[1]))
    
    return answer