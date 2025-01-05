class Job:
    def __init__(self, id, title, skills, experience, salary, priority):
        self.id = id
        self.title = title
        self.skills = skills
        self.experience = experience
        self.salary = salary
        self.priority = priority


class Node:
    def __init__(self, job):
        self.job = job
        self.next = None


class JobRecruitmentArray:
    def __init__(self, capacity=10):
        self.jobs = []
        self.capacity = capacity

    def add_job(self, job):
        if len(self.jobs) < self.capacity:
            self.jobs.append(job)
            self.jobs.sort(key=lambda x: x.priority,
                           reverse=True)  
            print(f"\nJob Added to Array:")
            print(f"ID: {job.id}")
            print(f"Title: {job.title}")
            print(f"Priority: {job.priority}")
            print(f"Skills: {', '.join(job.skills)}")
            return True
        return False

    def remove_job(self, job_id):
        for i, job in enumerate(self.jobs):
            if job.id == job_id:
                removed = self.jobs.pop(i)
                print(f"\nRemoved job: {removed.title}")
                return True
        return False

    def find_matches(self, candidate_skills, exp):
        matches = []
        for job in self.jobs:
            for skill in candidate_skills:
                if skill in job.skills and job.experience <= exp:
                    matches.append(job)
        return matches

    def display_jobs(self):
        print("\nCurrent Jobs in Array:")
      
        for job in self.jobs:
            print(
                f"ID: {job.id}, Title: {job.title}, Priority: {
                    job.priority}, Salary: {job.salary} Rwf"
            )


class JobRecruitmentLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_job(self, job):
        new_node = Node(job)
        if not self.head or job.priority > self.head.job.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.job.priority >= job.priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1
        print(f"\nJob Added to Linked List:")
        print(f"ID: {job.id}")
        print(f"Title: {job.title}")
        print(f"Priority: {job.priority}")
        print(f"Skills: {', '.join(job.skills)}")

    def remove_job(self, job_id):
        if not self.head:
            return False

        if self.head.job.id == job_id:
            self.head = self.head.next
            self.size -= 1
            return True

        current = self.head
        while current.next:
            if current.next.job.id == job_id:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        return False

    def display_jobs(self):
        print("\nCurrent Jobs in Linked List:")
        
        current = self.head
        while current:
            print(
                f"Title: {current.job.title}, Priority: {current.job.priority} ", end="-> "
            )
            current = current.next
        print(None)


def display_output():
    array_system = JobRecruitmentArray(capacity=5)
    list_system = JobRecruitmentLinkedList()

    jobs = [
        Job("J1", "Python Developer", ["Python", "Django"], 3, 75000, 3),
        Job("J2", "Data Scientist", ["Python", "ML"], 2, 80000, 5),
    ]

    print("The job recruitment portal with AI-based matching")

    for job in jobs:
        array_system.add_job(job)
        list_system.add_job(job)

    array_system.display_jobs()
    list_system.display_jobs()

    candidate_skills = ["Python", "React"]
    candidate_exp = 2

    print("\nMatches from Array:")
    jobs_matched = array_system.find_matches(candidate_skills, candidate_exp)
    for job in jobs_matched:
        print(f"{job.title}  {job.salary} Rwf")


display_output()
