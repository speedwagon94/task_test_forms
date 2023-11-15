import requests


base_url = "http://localhost:5000/get_form"

forms = [
    {"name": "user123", "registration_date": "2023-05-05", "email": "user123@example.com"},
    {"field1": "test", "field2": "2023-01-01", "field3": "+71234567890"},
    {"username": "admin", "registration_date": "2023-06-30", "email": "admin@example.com"},
    {"company": "ABC Inc.", "establishment_date": "2000-12-01", "industry": "Technology"},
    {"product_name": "Gadget", "release_date": "2023-07-15", "manufacturer": "XYZ Corp."},
    {"author": "Author1", "publication_date": "2023-08-05", "content": "Sample content"},
    {"user_name": "John Doe", "order_date": "2023-02-15"},
    {"title": "Event Form", "event_date": "2023-03-20", "location": "City Center"},
    {"customer_name": "Alice", "order_date": "2023-04-10", "product": "Laptop"},
    {"first_name": "Jane", "last_name": "test@test.com", "birth_date": "1990-08-25"},
]


# Проход по каждому набору данных формы в списке forms
for form_data in forms:
    # Выполнение HTTP POST-запроса с использованием библиотеки requests
    response = requests.post(base_url, data=form_data)

    # Вывод информации о запросе
    print(f"Request: {form_data}")

    # Вывод информации об ответе (текст ответа)
    print(f"Response: {response.text}\n")
