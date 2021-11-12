# https://app.codility.com/c/run/training4PBHNR-545/

def solution(A, B, K):
    # B까지의 K 배수 갯수 - A까지의 K 배수 갯수
    return (B // K) - ((A - 1) // K)