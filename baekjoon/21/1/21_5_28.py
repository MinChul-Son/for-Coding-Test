# https://www.acmicpc.net/problem/1062
## 실패
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
words = []
answer = 0
for _ in range(N):
    input_word = input().strip()
    words.append(set(input_word[4:-4]))
learned = ["a", "n", "t", "i", "c"]

if K < 5:
    print(0)
else:
    words = sorted(words, key=lambda x:len(x))
    K -= 5
    for word in words:
        if word == "":
            answer += 1
            continue
        for alpha in word:
            if alpha in learned:
                pass
            else:
                if K == 0:
                    break
                K -= 1
                learned.append(alpha)
        else:
            answer += 1
    print(answer)
        

#--------------------------------------------------------------------------
# https://www.acmicpc.net/problem/14719
import sys
input = sys.stdin.readline
h, w = map(int, input().split())
height = list(map(int, input().split()))
raindrop = 0
for i in range(len(height)):     
    max_left = max(height[:i+1])
    max_right = max(height[i:])
    which_low = min(max_left, max_right)
    raindrop = raindrop + abs(height[i] - which_low)
print(raindrop)

