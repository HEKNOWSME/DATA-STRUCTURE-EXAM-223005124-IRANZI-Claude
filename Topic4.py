class JobOrder:
    def __init__(self, ID, title, experience, priority):
        self.ID = ID
        self.title = title
        self.experience = experience
        self.priority = priority


class TreeNode:
    def __init__(self, order):
        self.order = order
        self.left = None
        self.right = None
        self.height = 1


class JobMatchingAVL:
    def __init__(self, max_size):
        self.root = None
        self.max_size = max_size
        self.current_size = 0

    def get_height(self, node):
        return 0 if not node else node.height

    def get_balance(self, node):
        return 0 if not node else self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, root, order):
        if not root:
            self.current_size += 1
            return TreeNode(order)

        if order.priority < root.order.priority:
            root.left = self.insert(root.left, order)
        else:
            root.right = self.insert(root.right, order)

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and order.priority < root.left.order.priority:
            return self.right_rotate(root)

        if balance < -1 and order.priority > root.right.order.priority:
            return self.left_rotate(root)

        if balance > 1 and order.priority > root.left.order.priority:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and order.priority < root.right.order.priority:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def remove_min(self, root):
        if not root.left:
            return root.right, root
        root.left, removed_node = self.remove_min(root.left)
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))
        return root, removed_node

    def add_job(self, job):

        if self.current_size >= self.max_size:
            print(f"Tree is full. Removing lowest-priority job.")
            self.root, _ = self.remove_min(self.root)
            self.current_size -= 1

        self.root = self.insert(self.root, job)

    def in_order_traversal(self, root):
        if not root:
            return []
        return self.in_order_traversal(root.left) + [root.order] + self.in_order_traversal(root.right)


def display_output():
    max_jobs = 4
    tree = JobMatchingAVL(max_jobs)

    jobs = [
        JobOrder(1, "Python Developer", ["Python", "Django", "SQL"], 0.9),
        JobOrder(2, "Data Scientist", ["Python", "ML", "Statistics"], 0.8),
        JobOrder(3, "Frontend Developer", [
                 "JavaScript", "React", "HTML"], 0.7),
        JobOrder(4, "Senior Architect", ["Python", "System Design"], 0.95),
    ]

    print("Adding jobs to AVL Tree:")
    for job in jobs:
        tree.add_job(job)
        print(f"Added: {job.title} (Priority: {job.priority})")
        print("Current jobs in tree (in-order traversal):")
        for job_in_tree in tree.in_order_traversal(tree.root):
            print(f"Job: {job_in_tree.title}, Priority: {job_in_tree.priority}")
        print("-" * 30)

display_output()
