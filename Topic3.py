from collections import deque


class JobApplication:
    def __init__(self, ID, title, skills, experience, priority):
        self.ID = ID
        self.title = title
        self.skills = skills
        self.experience = experience
        self.priority = priority


class JobQueue:
    def __init__(self):
        self.job_queue = deque()
        self.processed = 0

    def add_job(self, job):
        self.job_queue.append(job)
        print(f"\nNew Job Added:")
        print(f"ID: {job.ID}")
        print(f"Title: {job.title}")
        print(f"Skills: {', '.join(job.skills)}")
        print(f"Experience: {job.experience} years")
        print(f"Priority: {job.priority}")

    def process_job(self):
        if not self.job_queue:
            print("\nNo jobs to process")
            return None

        self.job_queue = deque(
            sorted(self.job_queue, key=lambda x: x.priority, reverse=True))
        job = self.job_queue.popleft()
        self.processed += 1

        print(f"\nProcessing Job:")
        print(f"ID: {job.ID}")
        print(f"Title: {job.title}")
        print(f"Skills: {', '.join(job.skills)}")
        print(f"Experience: {job.experience} years")
        print(f"Priority: {job.priority}")
        return job

    def show_queue_status(self):
        print(f"\nQueue Status:")
        print(f"Jobs in Queue: {len(self.job_queue)}")
        print(f"Jobs Processed: {self.processed}")


def displayOutput():
    job_queue = JobQueue()
    jobs = [
        JobApplication("J1", "Python Developer", [
                       "Python", "Django"], 3, "High"),
        JobApplication("J2", "Data Scientist", ["Python", "ML"], 2, "Medium")
    ]

    print("Queue for job recruitment portal with AI-based matching")

    for job in jobs:
        job_queue.add_job(job)
        job_queue.show_queue_status()

    print("\nProcessing Jobs...")

    while job_queue.job_queue:
        job_queue.process_job()
        job_queue.show_queue_status()


displayOutput()