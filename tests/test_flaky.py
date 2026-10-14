import random


def test_unstable_response_time():
    # имитация нестабильного теста: падает примерно в одном запуске из трёх
    assert random.random() > 0.33
