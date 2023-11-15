from flask import Flask, request, jsonify

from validation import find_matching_template
from logging_config import configure_logging


configure_logging()

app = Flask(__name__)


@app.route('/get_form', methods=['POST'])
def get_form():
    """
    Обработчик POST-запроса для получения формы.

    Пытается извлечь данные из запроса, затем находит соответствующий шаблон,
    основываясь на этих данных. Если валидация не проходит, возвращается ошибка 400.
    Если найден подходящий шаблон, возвращается успешный результат. В случае неожиданной ошибки,
    возвращается ошибка 500, сопровождаемая соответствующим сообщением.

    Returns:
        Response: JSON-ответ с результатом или ошибкой.
    """
    try:
        # Извлечение данных из запроса
        data = request.form.to_dict()

        # Поиск подходящего шаблона на основе данных
        result = find_matching_template(data)

        if isinstance(result, dict):
            # Логгирование ошибки валидации
            app.logger.error("Validation failed: %s", result)
            return jsonify(result), 400  # Ошибка валидации
        else:
            # Логгирование успешного результата
            app.logger.info("Matching template found: %s", result)
            return result
    except Exception as e:
        # Логгирование неожиданной ошибки
        app.logger.exception("An unexpected error occurred: %s", str(e))
        return jsonify({'error': 'Internal Server Error'}), 500


if __name__ == '__main__':
    app.run(debug=True)
