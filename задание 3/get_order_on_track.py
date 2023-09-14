import sender_stend_request
# Вера Попова, 8-ая когорта, финальный проект. Инженер по тестированию плюс

# Функция для позитивной проверки
def positive_assert(track_order):
    # В переменную order_respons сохраняется запрос на получения заказа по треку заказа
    order_response = sender_stend_request.get_order_track(track_order)
    # Проверить, что код ответа равен 200
    assert order_response.status_code == 200


# Тест 01.
def test_get_order_track_success_response():
    positive_assert(sender_stend_request.track_order)