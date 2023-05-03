class Task:
    number = 0

    def __init__(self, description: str, programmer: str, workload: int):
        if Task.number == 0:
            self.id = 1
            Task.number = 1
        else:
            if Task.number > 0:
                Task.number += 1
                self.id = Task.number
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.is_finished_status = False
        id(1)

    def is_finished(self):
        if not self.is_finished_status:
            return False
        else:
            return True

    def mark_finished(self):
        self.is_finished_status = True

    def status(self):
        if not self.is_finished_status:
            return "NOT FINISHED"
        else:
            return "FINISHED"

    def __str__(self):
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.status()}"


class OrderBook:
    def __init__(self):
        # self.task = Task()
        self.list_of_tasks = []

    def add_order(self, description: str, programmer: str, workload: int):
        self.list_of_tasks.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.list_of_tasks

    def programmers(self):
        return list(set(task.programmer for task in self.list_of_tasks))

    def mark_finished(self, id: int):
        for task in self.list_of_tasks:
            if task.id == id:
                task.mark_finished()
                return
        raise ValueError("id not found")

    def finished_orders(self):
        return [task for task in self.list_of_tasks if task.is_finished_status is True]

    def unfinished_orders(self):
        return [task for task in self.list_of_tasks if task.is_finished_status is False]


    def status_of_programmer(self, programmer: str):
        # sum of finished tasks, sum of unfinished, sum of workload for finished, sum for unfinished
        finishedSum = 0
        unfinishedSum = 0
        fin_workload = 0
        unfin_workload = 0

        if programmer not in self.programmers():
            raise ValueError

        for task in self.list_of_tasks:
            if programmer == task.programmer and task.is_finished_status is True:
                    finishedSum += 1
                    fin_workload += task.workload
            if programmer == task.programmer and task.is_finished_status is False:
                unfinishedSum += 1
                unfin_workload += task.workload

        return (finishedSum, unfinishedSum, fin_workload, unfin_workload)

if __name__ == "__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)