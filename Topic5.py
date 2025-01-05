from collections import deque
class JobApplication:
    def __init__(self, ID, title, skills, experience, priority):
        self.ID = ID
        self.title = title
        self.skills = skills
        self.experience = experience
        self.priority = priority

    def __str__(self):
        return (f"ID: {self.ID}, Title: {self.title}, Skills: {', '.join(self.skills)}, "
                f"Experience: {self.experience} years, Priority: {self.priority}")


class DynamicJobTracker:
    def __init__(self):
        self.job_data = deque()

    def add_job_to_front(self, job):
        self.job_data.appendleft(job)
        print(
            f"Job '{job.title}' added to the front of the deque (High priority).")

    def add_job_to_back(self, job):
        self.job_data.append(job)
        print(
            f"Job '{job.title}' added to the back of the deque (Normal priority).")

    def remove_oldest_job(self):
        if self.job_data:
            removed_job = self.job_data.popleft()
            print(f"Oldest job '{removed_job.title}' removed from the deque.")
            return removed_job
        else:
            print("No jobs available to remove.")
            return None

    def remove_latest_job(self):
        if self.job_data:
            removed_job = self.job_data.pop()
            print(f"Latest job '{removed_job.title}' removed from the deque.")
            return removed_job
        else:
            print("No jobs available to remove.")
            return None

    def display_jobs(self):
        if not self.job_data:
            print("No jobs currently being tracked.")
            return

        print("\nCurrent Jobs in the Deque:")
        for idx, job in enumerate(self.job_data, 1):
            print(f"{idx}. {job}")

    def process_job(self):
        if self.job_data:
            job = self.job_data.popleft()
            print(f"\nProcessing Job: {job.title}")
            print(f"ID: {job.ID}")
            print(f"Skills: {', '.join(job.skills)}")
            print(f"Experience: {job.experience} years")
            print(f"Priority: {job.priority}")
            return job
        else:
            print("No jobs to process.")
            return None


def run_dynamic_demo():
    tracker = DynamicJobTracker()
    jobs = [
        JobApplication("J1", "Python Developer", [
                       "Python", "Django"], 3, "High"),
        JobApplication("J2", "Data Scientist", ["Python", "ML"], 2, "Medium"),
        JobApplication("J3", "Web Developer", [
                       "JavaScript", "React"], 2, "Low"),
        JobApplication("J4", "AI Engineer", [
                       "Python", "AI", "TensorFlow"], 5, "High"),
        JobApplication("J5", "DevOps Engineer", [
                       "AWS", "Docker", "Kubernetes"], 4, "Medium"),
    ]

    print("\nAdding Jobs Dynamically:")
    tracker.add_job_to_back(jobs[0])
    tracker.add_job_to_back(jobs[1])
    tracker.add_job_to_front(jobs[2])
    tracker.add_job_to_front(jobs[3])
    tracker.display_jobs()

    print("\nProcessing Jobs Dynamically:")
    tracker.process_job()
    tracker.process_job()
    tracker.display_jobs()

    print("\nRemoving Jobs Dynamically:")
    tracker.remove_oldest_job()
    tracker.remove_latest_job()
    tracker.display_jobs()


run_dynamic_demo()