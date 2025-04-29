# Merge Intervals

def merge(intervals=[[1,3], [2,6], [8,10], [15,18]]):
    intervals.sort()
    merged=[]
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    print("Merged Intervals: ", merged)

merge()