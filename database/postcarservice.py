from database.models import Car
from database import get_database
from datetime import datetime


def post_your_car(brand, model, wearness, trader_number, cost, type):
    db = next(get_database())

    new_car = Car(
        brand=brand,
        model=model,
        wearness=wearness,
        trader_number=trader_number,
        cost=cost,
        type=type,
        reg_date=datetime.now()
    )
    db.add(new_car)
    db.commit()

    return 'Машина успешно добавлена'


def change_car(brand, model, wearness, trader_number, cost, type):
    db = next(get_database())

    new_car = Car(
        brand=brand,
        model=model,
        wearness=wearness,
        trader_number=trader_number,
        cost=cost,
        type=type
    )
    db.add(new_car)
    db.commit()

    return ('Машина успешно изменена')
# ДА ДА ДА просто записывается машина новая, другая уже, я знаю


def add_car_photo(car_id, photo_of_car):
    db = next(get_database())

    check = db.query(Car).filter_by(id=car_id).first()

    if check:
        check.photo_of_car = photo_of_car
        db.commit()
        return 'Фото машины успешно добавлено'
    else:
        return False


def get_all_cars():
    db = next(get_database())

    all_cars = db.query(Car).all()

    return all_cars


def get_exact_car(car_id):
    db = next(get_database())

    car_info = db.query(Car).filter_by(id=car_id).first()

    return car_info





