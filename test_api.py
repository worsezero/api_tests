import requests
import allure

BASE_URL = "https://jsonplaceholder.typicode.com"

@allure.title("Проверка статус-кода GET /posts/1")
@allure.description("Запрос одного поста должен вернуть 200")
def test_get_post_status_code():
    with allure.step("Отправляем GET запрос"):
        response = requests.get(f"{BASE_URL}/posts/1")
    with allure.step("Проверяем статус-код 200"):
        assert response.status_code == 200


@allure.title("Проверка верного id GET /posts/1")
@allure.description("Запрос первого поста должен вернуть 1")
def test_get_post_has_correct_id():
    with allure.step("Отправляем GET запрос"):
         response = requests.get(f"{BASE_URL}/posts/1")
         data = response.json()
    with allure.step("Проверям статус-id 1"):
         assert data["id"] == 1

@allure.title("Проверка title GET /posts/1")
@allure.description("Запрос первого поста должен вернуть str")
def test_get_post_title_is_string():
    with allure.step("Отправляем GET запрос"):
         response = requests.get(f"{BASE_URL}/posts/1")
         data = response.json()
    with allure.step("Проверяем title str"):
         assert isinstance(data["title"], str)


@allure.title("Проверка создания поста POST /posts")
@allure.description("Запрос первого поста должен вернуть статус-код 201,статус id 101")
def test_create_post():
    with allure.step("Создаем тело запроса"):
         new_post = {
             "title": "My test post",
             "body": "This is a test",
             "userId": 1
         }

    with allure.step("Отправляем POST запрос"):
         response = requests.post(f"{BASE_URL}/posts", json=new_post)
         data = response.json()
    with allure.step("Смотрим ответы статус-код 201, id 101"):

        assert response.status_code == 201
        assert data["title"] == "My test post"
        assert data["id"] == 101


@allure.title("Проверка удаления поста DELETE /posts/1")
@allure.description("Запрос удаление первого поста должен вернуть пустой джейсон")
def test_delete_post():
    with allure.step ("Отправляем Delete запрос"):
         response = requests.delete(f"{BASE_URL}/posts/1")


    with allure.step ("Проверяем статус-код 200,ответ пустой json"):
          assert response.status_code == 200
          assert response.json() == {}



@allure.title("Проверяем комментарий GEt /comments?postId=1")
@allure.description("Запрос первого комментария, статус-код 200,данные в list")
def test_get_comments_by_post():
    with allure.step("Отправляем GET запрос"):
          response = requests.get(f"{BASE_URL}/comments?postId=1")
          data = response.json()

    with allure.step("Смотрим ответ статус-код 200,ответ в list"):
         assert response.status_code == 200
         assert isinstance(data, list)


@allure.title("Проверка полного обновления поста PUT")
@allure.description("Запрос статус-код 200,ответ в title")
def test_update_post():
    with allure.step("Отправляем запрос PUT"):
         update_post = {
        "id": 1,
        "title": "My test post",
        "body": "Updated body",
        "userId": 1
         }

         response = requests.put(f"{BASE_URL}/posts/1", json=update_post)
         data = response.json()

    with allure.step("Смотрим ответ статус-код 200,ответ title- My test post"):
          assert response.status_code == 200
          assert data["title"] == "My test post"



