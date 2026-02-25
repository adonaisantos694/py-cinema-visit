from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers, hall_number, cleaner, movie):
    hall = CinemaHall(number=hall_number)
    cleaner_obj = Cleaner(name=cleaner)

    customer_objects = [
        Customer(name=c["name"], food=c["food"])
        for c in customers
    ]

    for customer in customer_objects:
        CinemaBar.sell_product(customer.food, customer)

    hall.start_movie(movie)

    for customer in customer_objects:
        customer.watch_movie(movie)

    hall.end_movie(movie)

    cleaner_obj.clean_hall(hall_number)