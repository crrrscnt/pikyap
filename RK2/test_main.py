from main import otm_function, mtm_function, set_a

#TDD-фреймворк
def test_otm_function():
    expected = [('Алексеев', 4.0, '9 мат'), ('Борисов', 4.8, '10 мат'), ('Иванов', 5.0, '11 мат'),
                ('Петров', 4.4, '11 мат'), ('Сидоров', 3.9, '11 мат'), ('Антонов', 4.0, '11 мат')]
    actual = []
    assert otm_function(actual) == expected


def test_mtm_function():
    expected = [('Алексеев', 4.0, '9 мат'), ('Борисов', 4.8, '10 мат'), ('Иванов', 5.0, '11 мат'),
                ('Петров', 4.4, '11 мат'), ('Сидоров', 3.9, '11 мат'), ('Антонов', 4.0, '11 мат'),
                ('Алексеев', 4.0, '9 гум'), ('Борисов', 4.8, '10 гум'), ('Иванов', 5.0, '11 гум'),
                ('Петров', 4.4, '11 гум'), ('Сидоров', 3.9, '11 гум'), ('Антонов', 4.0, '11 гум')]
    actual = []
    assert mtm_function(actual) == expected


def test_set_a():
    expected = {'Алексеев': ['9 мат', '9 гум'], 'Антонов': ['11 мат', '11 гум']}
    m_to_m = []
    res = {}
    actual = set_a(mtm_function(m_to_m), res)
    assert expected == actual