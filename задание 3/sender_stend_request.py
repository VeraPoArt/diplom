import configuration
import data
import requests



# Выполнить запрос на создание заказа
def post_new_order(create_order):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                    json=create_order,
                    headers=data.headers)
response = post_new_order(data.create_order)

# Сохранить номер трека заказа
track_order = response.json()["track"]


# Выполнить запрос на получения заказа по треку заказа
def get_order_track(track_order):
    return requests.get(configuration.URL_SERVICE + configuration.GET_TRACK_ORDER,
                        params={"t": track_order})