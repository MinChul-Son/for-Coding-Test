# https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3


# def solution(record):
#     idDict = dict()
#     answer = []
#     logList = []
#     for e in record:
#         dataList = e.split(" ")
#         if dataList[0] == "Leave":
#             logList.append([dataList[1], "님이 나갔습니다."])
#         elif dataList[0] == "Enter":
#             idDict[dataList[1]] = dataList[2]
#             logList.append([dataList[1], "님이 들어왔습니다."])
#         elif dataList[0] == "Change":
#             idDict[dataList[1]] = dataList[2]
#     print(logList)
#     for log in logList:
#         answer.append(idDict[log[0]] + log[1])
#     print(idDict)
#     return answer






