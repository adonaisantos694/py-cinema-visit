from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(food: str, customer: Customer) -> None:
        print(f'Cinema bar sold {food} to {customer.name}.')
