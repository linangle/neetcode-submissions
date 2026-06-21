class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
    # max heap sol
    # idea : always want to run the task that still has the most remaining occurrences
        # keep max heap with task with most frequent on top
        # after running a task, it goes into a cooldown q
        # when the cooldown finishes, push it back into the heap

        # Counter() maps task to its frequency
        count = Counter(tasks)
        # negative because we're doing a maxheap
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # pairs of [-cnt, idleTime]
        # while heap and cooldown q are not empty
        while maxHeap or q:
            time += 1

            # if heap is empty and cooldown q not empty
                # set time = next_time (fast-forward)
            if not maxHeap:
                time = q[0][1] # q[0][1] is the idleTime of the front task (earliest moment any task can be scheduled)
            else:
                # pop the task with the largest remaining count
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt: 
                    q.append([cnt, time + n])
            # while the task at the front has next_available_time == time
                # remove from q and push back into max-heap
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time