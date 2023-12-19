use std::error::Error;
use sqlx::postgres::PgPoolOptions;
use sqlx::{FromRow,Row};
use chrono::NaiveDate;
// use: Внутри области видимости использование ключевого слова use
// создаёт псевдонимы для элементов, чтобы уменьшить повторение
// длинных путей.

// #[типаж()]
// C помощью типажа fmt::Debug все типы могут выводить
// (автоматически создавать, derive) реализацию fmt::Debug.
#[derive(Debug, FromRow)]   // derive - "встроенные реализации"
struct Flight {             // структура Flight
    id: i32,
    name: String,
    country: String,
    flight_date: NaiveDate, // дата
    spaceship: String,
}

// async/.await - это специальный синтаксис Rust, который позволяет
//      не блокировать поток, а передавать управление другому коду,
//      пока ожидается завершение операции.
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> { // либо результ, либо еррор
    // Подключение к базе данных PostgreSQL
    // переменная пул, адрес//имя:пароль
    let pool = PgPoolOptions::new()
        .connect("postgres://postgres:222@localhost:5432/testdb")
        .await?;

    // Создание таблицы в базе данных
    // Приводим в соответствие типы переменных Rust и Postgres:
    //      i32 Rust соответствует INT, SERIAL Postgres;
    //      String - VARCHAR, CHAR(n), TEXT, CITEXT, NAME, UNKNOWN;
    //      chrono::NaiveDate - DATE;
    //      i64 - BIGINT (для вывода COUNT Postgres.В последнем запросе, ниже.)
    sqlx::query(
        "CREATE TABLE IF NOT EXISTS flights (
            id SERIAL NOT NULL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            country VARCHAR(50) NOT NULL,
            flight_date DATE NOT NULL,
            spaceship VARCHAR(50) NOT NULL
        )",
    )
    .execute(&pool)
    .await?;

    // Парсинг CSV файла
    let mut row_count = 0; // mut - это *изменяемое* связанное имя
    //      переменной. Когда связанное имя изменяемо, это означает, что
    //      мы можем поменять связанное с ним значение.
    let file_path = "./space_travellers.csv"; // путь файла ля парсинга
    let file = std::fs::File::open(file_path)?;
    let mut reader = csv::Reader::from_reader(file);
    // Чтение содержимого файла.

    // Чтение данных из CSV и запись в базу данных
    // core::option::Option Some(value) - кортежная структура, обёртка для значения типа T,
    //      для перехвата ошибок вместо вызова паники с помощью макроса panic!
    while let Some(result) = reader.records().next() {
        let record = result?;
        let flight = Flight {
        // unwrap() - если возвращенный объект Result представляет константу Ok, то метод unwrap()
        // возвращает объект, который содержится в константе Ok. Но если объект Result
        // представляет константу Err, то метод unwrap() вызывает макрос panic!.
            id: record[0].parse().unwrap(),
            name: record[1].to_string(),
            country: record[2].to_string(),
        //  парсинг строки из заданного пользователем формата в значение NaiveDate.
            flight_date: NaiveDate::parse_from_str(&record[3], "%Y-%m-%d").unwrap(),
            spaceship: record[4].to_string(),
        };

        // Вставка данных в базу данных
        sqlx::query(
            "INSERT INTO flights (
                id, name, country, flight_date, spaceship
            ) VALUES ($1, $2, $3, $4, $5)",
        )
        .bind(flight.id)
        .bind(&flight.name)
        .bind(&flight.country)
        .bind(flight.flight_date)
        .bind(&flight.spaceship)
        .execute(&pool)
        .await?;
        row_count += 1;
    }

    println!("В таблице: {} записей", row_count);
    println!("*******");

    // Пример запроса 1 к базе данных для вывода в консоль
    println!("Список космонавтов Советского Союза, взлетавших в 1960-х г.г.");
    let mut index_number= 0;
    let time_interval = sqlx::query(
        "SELECT name, country,flight_date, spaceship FROM flights
        WHERE flight_date >= '1961-01-01' AND flight_date < '1969-12-31' AND country LIKE 'Со%'
        ")
        .fetch_all(&pool)
        .await?;
    // Итератор. Из time_interval: Vec<PgRow> присваиваем переменным значения строки. Вывод.
    for interval in time_interval {
        let name: String = interval.get("name");
        let country: String = interval.get("country");
        let flight_date: NaiveDate = interval.get("flight_date");
        let spaceship: String = interval.get("spaceship");
        index_number += 1;
        println!( // чтобы не скакали надписи 1,2,3, ..., были вровень с 10, т.д.
            "{index_number:>2}. {}, {}, {}, {}",
            name, country, flight_date, spaceship
        );
    }
    println!("*******");

    // Пример запроса 2 к базе данных для вывода в консоль
    println!("Список стран, космонавты которых побывали в космосе 10 и более раз (по убыванию)");
    index_number = 0;
	let select_query = sqlx::query
        ("SELECT country, COUNT(country) FROM flights
        GROUP BY country HAVING COUNT (country) > 10 ORDER BY COUNT(country) desc;
        ")
        .fetch_all(&pool)
        .await?;
    for el in select_query {
        let country: String = el.get("country");
        let cnt: i64 = el.get("count");
        index_number += 1;
        println!(
            "{index_number}. {} ({})",
            country, cnt
        );
    }
    println!("*******");

    Ok(())
}