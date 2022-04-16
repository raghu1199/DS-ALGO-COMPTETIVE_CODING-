
class Job:
    def __init__(self,jobID,profit,deadline):
        self.jobId=jobID
        self.deadline=deadline
        self.profit=profit

def schedule(jobs:list,T):
    slot=[-1]*T  # create slots 1 to T(max deadline) -1 indicate no job plaed there
    jobs.sort(key=lambda j:j.profit,reverse=True)
    profit=0
    for job in jobs:
        for i in range(job.deadline,0,-1):   # time slots start from 1 to T not from 0 to T so last 0 is excluded
            # if job deadline is less than Total time and slot for this deadline is empty then place the job in slot
            if i < T and slot[i]==-1:   
                slot[i]=job.jobId
                profit+=job.profit
                break

    print("Scheduled jobs are:")
    for s in slot:
        if s!=-1:
            print(s,end=" ")
    print("max_profit:",profit)
    print("Scheduled jobs:",list(filter(lambda s:s!=-1,slot)))  # same as above

jobs=[Job(1,85,5),Job(2,25,4),Job(3,16,3),Job(4,40,3),Job(5,55,4),Job(6,19,5),Job(7,92,2),Job(8,80,3),Job(9,15,7)]
T=7

schedule(jobs,T)