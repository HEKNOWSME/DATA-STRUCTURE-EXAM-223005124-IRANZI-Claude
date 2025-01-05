class Job:
    def __init__(self, ID, title, skills, experience, priority):
        self.ID = ID
        self.title = title
        self.skills = skills
        self.experience = experience
        self.priority = priority

    def __str__(self):
        return f"ID: {self.ID}, Title: {self.title}, Priority: {self.priority}"


def merge_sort(jobs):
    if len(jobs) <= 1:
        return jobs

    mid = len(jobs) // 2
    left = merge_sort(jobs[:mid])
    right = merge_sort(jobs[mid:])

    return merge(left, right)


def merge(left, right):
    sorted_jobs = []
    while left and right:
        if left[0].priority > right[0].priority:
            sorted_jobs.append(left.pop(0))
        else:
            sorted_jobs.append(right.pop(0))
    sorted_jobs.extend(left or right)
    return sorted_jobs


def display_merge():
    jobs = [
        Job(1, "Python Developer", ["Python", "Django"], 3, 0.8),
        Job(2, "Data Scientist", ["Python", "ML"], 2, 0.9),
        Job(3, "Frontend Developer", ["JavaScript", "React"], 4, 0.6),
        Job(4, "Backend Developer", ["Java", "Spring Boot"], 5, 0.85),
        Job(5, "DevOps Engineer", ["Docker", "Kubernetes"], 3, 0.7),
    ]

    print("\nUnsorted Jobs:")
    for job in jobs:
        print(job)

    sorted_jobs = merge_sort(jobs)

    print("\nSorted Jobs (By Priority):")
    for job in sorted_jobs:
        print(job)


display_merge()