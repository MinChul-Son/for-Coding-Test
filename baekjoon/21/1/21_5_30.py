# https://www.acmicpc.net/problem/1700
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
elec_items = list(map(int, input().split()))
answer = 0
multi_tap = []
for i in range(len(elec_items)):
    if len(multi_tap) < n and elec_items[i] not in multi_tap:
        multi_tap.append(elec_items[i])
    else:
        if elec_items[i] in multi_tap:
            continue
        for j in multi_tap:
            if j in elec_items[i+1:]:
                pass
            else: # 해당 전자제품이 뒤에서 다시 사용되지 않는 case
                answer += 1
                multi_tap.remove(j)
                multi_tap.append(elec_items[i])
                break
        else: # 모든 전자제품이 뒤에서 다시 사용되는 case
            next_schedule_idx = []
            for socket in multi_tap:
                next_schedule_idx.append((elec_items[i+1:].index(socket), socket))
            multi_tap.remove(max(next_schedule_idx)[1])
            multi_tap.append(elec_items[i])
            answer += 1
print(answer)