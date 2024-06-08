import configuration 
import data
import requests

def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)


def get_order(track_number):
    get_order_url_api = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_order_url_api)
    return response


def test_order_details():
    response = create_order(data.order_body)
    track_number = response.json()["track"]

    g_response = get_order(track_number)

    assert g_response.status_code == 200, f"Ошибка: {g_response.status_code}"

    order_result = g_response.json()
    print(f"Заказ создан. Номер заказа:\n{track_number}\nДанные заказа:\n{order_result}")
    print(f"Код ответа:\n{g_response.status_code}")


test_order_details()

