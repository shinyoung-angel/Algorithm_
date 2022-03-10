import heapq
jobs = [[0, 3], [1, 9], [2, 6]]
heap = []

def solution(jobs):
    jobs.sort()
    time = jobs[0][0] + jobs[0][1]
    result = [jobs[0][1]]
    jobs.pop(0)

    if jobs:
        for start, take in jobs:
            heapq.heappush(heap,[take, start])


    while heap:
        take, start = heapq.heappop(heap)

        if start <= time:
            result.append(time-start+take)
            time += take
        else:
            result.append(take)
            time += start-time+take


    return sum(result)//(len(jobs)+1)

print(solution(jobs))