# Daily temperatures: Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to wait after the 
# ith day to get a warmer temperature. If there is no future day for which this is possible, 
# keep answer[i] == 0 instead.

def dailyTemperatures(temperatures):
    answer = [0]*(len(temperatures))
    stack = []
    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev = stack.pop()
            answer[prev] = i - prev
        stack.append(i)
    print("Answers array is: ", answer)

dailyTemperatures(temperatures=[73,74,75,71,69,72,76,73])
