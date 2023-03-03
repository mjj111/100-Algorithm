def solution(jobs):
    wait = 0
    curr = 0
    jobs.sort(key=lambda x:x[1])
    visited = set()
    while len(visited) < len(jobs):
        chk = True
        for i in range(len(jobs)):
            if i in visited:
                continue
            if jobs[i][0] <= curr:
                curr += jobs[i][1]
                wait += curr - jobs[i][0]
                visited.add(i)
                chk = False
                break
        if chk:
            curr += 1
    return wait // len(jobs)