class TaskManager:

    def __init__(self):
        self.task = dict()

    def new_task(self, task, priority):
        if priority not in self.task:
            self.task[priority] = Steck()
        self.task[priority].push(task)

    def __str__(self):
        display = list()
        if self.task:
            for i_priority in sorted(self.task.keys()):
                display.append(f'{i_priority} {self.task[i_priority]}\n')
        return ''.join(display)



class Steck:
    def __init__(self):
        self.__st = list()

    def __str__(self):
        return '; '.join(self.__st)

    def push(self, element):
        self.__st.append(element)

    def pop(self):
        if len(self.__st) == 0:
            return None
        else:
            return self.__st.pop()



manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)