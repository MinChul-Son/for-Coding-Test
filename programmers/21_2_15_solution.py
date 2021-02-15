# https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3
# def solution(new_id):
#     answer = ''
#     new_id = list(new_id.lower())
#     temp = ''
#     for i,p in enumerate(new_id):
#         if not p.isalpha():
#             if p == '-' or p == '_' or p== '.':
#                 temp += p
#             elif p.isdecimal():
#                 temp += p
#             else:
#                 pass
#         else:
#             temp += p
#     new_id = temp
#     while True:
#         if ".." in new_id:
#             new_id = new_id.replace("..", ".")
#         else:
#             break
#     if new_id[0] == '.':
#         new_id = new_id[1:]
#     elif new_id[-1] == '.':
#         new_id = new_id[:-1]
#     if not new_id:
#         new_id += 'a'
#     if len(new_id) >= 16:
#         new_id = new_id[:15]
#     while True:
#         if new_id[-1] == '.':
#             new_id = new_id[:-1]
#         else:
#             break
#     if len(new_id) <= 2:
#         while len(new_id) < 3:
#             new_id += new_id[-1]
#     return new_id

# solution("abcdefghijklmn.p")
