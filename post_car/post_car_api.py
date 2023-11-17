from fastapi import APIRouter
from post_car import PostCarModel
from database.postcarservice import post_your_car, change_car, add_car_photo, get_all_cars, get_exact_car

car_router = APIRouter(prefix='/car', tags=['Работа с тазами'])


@car_router.post('/post-car')
async def post(data: PostCarModel):
    result = post_your_car(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message': 'ERROR'}


@car_router.get('/get-car')
async def get_car(car_id: int = 0):
    if car_id == 0:
        result = get_all_cars()
        return {'message': result}
    else:
        result = get_exact_car(car_id)
        return {'message': result}

'''нада добавить возможность для добавления фотографий, посмотрим чё Ботир скажет'''
