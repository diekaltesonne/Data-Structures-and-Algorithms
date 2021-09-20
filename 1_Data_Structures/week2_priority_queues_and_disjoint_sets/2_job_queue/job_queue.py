# python3

from collections import namedtuple
import heapq
AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])



def assign_jobs_fast(n_workers, jobs):
    result = []
    next_free_time= []
    for i in range(0,n_workers,1):
        next_free_time.append([0,i])
    
    heapq.heapify(next_free_time)

    for job in jobs:
        data_of_thread = heapq.heappop(next_free_time)
        result.append(AssignedJob(data_of_thread[1], data_of_thread[0])) #O(1)
        data_of_thread[0] += job
        heapq.heappush(next_free_time,data_of_thread)
    
    return result

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs_fast(n_workers, jobs)


    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
