import string

all_letters = string.ascii_letters
all_num = string.digits


class Task:
    id = 0
    @classmethod
    def new_id(cls):
        Task.id += 1
        return Task.id


    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.id = Task.new_id()
        self.is_finished_status = False

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

    def mark_finished(self, id_of_task: int):
        for task in self.list_of_tasks:
            if task.id == id_of_task:
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

        return finishedSum, unfinishedSum, fin_workload, unfin_workload


class OrderBookApplication:
    def __init__(self):
        pass
        self.orderbook = OrderBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def add_order(self):
        description = input("description ")
        programmer_workload = input("programmer and workload estimate: ")
        try:
            programmer = programmer_workload.split(" ")[0]
            work_load = int(programmer_workload.split(" ")[1])
            self.orderbook.add_order(description, programmer, work_load)
            print("added!")
        except:
            print("erroneous input")

    def list_finished_tasks(self):
        if len(self.orderbook.finished_orders()) == 0:
            print("no finished tasks")
        else:
            [print(order) for order in self.orderbook.finished_orders()]

    def list_unfinished_tasks(self):
        if len(self.orderbook.unfinished_orders()) == 0:
            print("no unfinished tasks")
        else:
            [print(order) for order in self.orderbook.unfinished_orders()]

    def mark_task_ask_finished(self):
        try:
            id_of_task = int(input("id: "))
            self.orderbook.mark_finished(id_of_task)
            print("marked as finished")
        except ValueError:
            print("erroneous input")

    def programmers(self):
        [print(programmer) for programmer in self.orderbook.programmers()]

    def state_of_programmer(self):
        programmer_name = input("enter name of programmer ")

        for programmer in self.orderbook.programmers():
            if programmer != programmer_name:
                print("erroneous input")
                return

        result = [task for task in self.orderbook.status_of_programmer(programmer_name)]
        print(f"tasks: finished {result[0]} not finished {result[1]}, hours: done {result[2]} scheduled {result[3]}")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            if command == "1":
                self.add_order()
            if command == "2":
                self.list_finished_tasks()
            if command == "3":
                self.list_unfinished_tasks()
            if command == "4":
                self.mark_task_ask_finished()
            if command == "5":
                self.programmers()
            if command == "6":
                self.state_of_programmer()


orderbook = OrderBookApplication()
orderbook.execute()
