class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            self.items = self.items[:-1]
        else:
            return 'error'

    def get_max(self):
        mx = 'None'
        if len(self.items) > 0:
            mx = max(self.items)
        return mx