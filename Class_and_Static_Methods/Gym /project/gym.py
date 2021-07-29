from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        for el in self.customers:
            if el.id == customer.id:
                return
        self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        for el in self.trainers:
            if el.id == trainer.id:
                return
        self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        for el in self.equipment:
            if el.id == equipment.id:
                return
        self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        for el in self.plans:
            if el . id == plan.id:
                return
        self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        for el in self.subscriptions:
            if el.id == subscription.id:
                return
        self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        nl = "\n"
        result = '\n'.join(str(i) for i in self.subscriptions if i.id == subscription_id)
        result += nl
        result += '\n'.join(str(i) for i in self.customers if i.id == subscription_id)
        result += nl
        result += '\n'.join(str(i) for i in self.trainers if i.id == subscription_id)
        result += nl
        result += '\n'.join(str(i) for i in self.equipment if i.id == subscription_id)
        result += nl
        result += '\n'.join(str(i) for i in self.plans if i.id == subscription_id)
        return result

