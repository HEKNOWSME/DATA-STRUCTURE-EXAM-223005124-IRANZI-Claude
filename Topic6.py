class TreeNode:
    def __init__(self, name, data=None):
        self.name = name
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def display_hierarchy(self, level=0):
        indent = " " * (level * 4)
        print(f"{indent}- {self.name} {'(Data: ' + str(self.data) + ')' if self.data else ''}")
        for child in self.children:
            child.display_hierarchy(level + 1)


def display_tree():
    root = TreeNode("Job Categories")
    it_jobs = TreeNode("IT Jobs")
    engineering_jobs = TreeNode("Engineering Jobs")
    healthcare_jobs = TreeNode("Healthcare Jobs")

    root.add_child(it_jobs)
    root.add_child(engineering_jobs)
    root.add_child(healthcare_jobs)

    python_dev = TreeNode("Python Developer", {
        "skills": ["Python", "Django"],
        "experience": 3,
        "priority": "High"
    })
    data_scientist = TreeNode("Data Scientist", {
        "skills": ["Python", "ML", "Statistics"],
        "experience": 2,
        "priority": "Medium"
    })

    it_jobs.add_child(python_dev)
    it_jobs.add_child(data_scientist)

    civil_engineer = TreeNode("Civil Engineer", {
        "skills": ["Structural Design", "AutoCAD"],
        "experience": 5,
        "priority": "High"
    })
    mechanical_engineer = TreeNode("Mechanical Engineer", {
        "skills": ["SolidWorks", "Manufacturing"],
        "experience": 4,
        "priority": "Medium"
    })

    engineering_jobs.add_child(civil_engineer)
    engineering_jobs.add_child(mechanical_engineer)

    nurse = TreeNode("Registered Nurse", {
        "skills": ["Patient Care", "Medical Terminology"],
        "experience": 2,
        "priority": "High"
    })
    doctor = TreeNode("General Practitioner", {
        "skills": ["Diagnosis", "Treatment Planning"],
        "experience": 6,
        "priority": "High"
    })

    healthcare_jobs.add_child(nurse)
    healthcare_jobs.add_child(doctor)
    print("\nJob Recruitment Portal Hierarchy:")
    root.display_hierarchy()


display_tree()
