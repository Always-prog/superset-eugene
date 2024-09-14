from sqlalchemy import create_engine, select, MetaData, Table, update

# Подключение к внешней базе данных с описаниями метрик
DESC_DATABASE_URI = (
    f"postgresql://"
    f"superset:superset@"
    f"localhost:5432/external_verboses"
)
# Название таблицы с метриками
METRICS_TABLE_NAME = 'metrics'

# Подключение к базе данных Суперсет. 
# Нужны права на изменение таблицы sql_metrics!
DATABASE_URI = (
    f"postgresql://"
    f"superset:superset@"
    f"localhost:5432/superset"
)

# Создание движков для подключения к базам данных
desc_engine = create_engine(DESC_DATABASE_URI)
engine = create_engine(DATABASE_URI)

# Загрузка метаданных и таблиц
metadata = MetaData()
sql_metrics = Table('sql_metrics', metadata, autoload_with=engine)
metrics = Table(METRICS_TABLE_NAME, metadata, autoload_with=desc_engine)

# Выполнение запроса к таблице metrics для получения названий метрик и описаний
with desc_engine.connect() as desc_conn, engine.connect() as conn:
    # Получение данных из таблицы metrics
    metric_data = desc_conn.execute(select(metrics.c.name, metrics.c.description)).fetchall()

    # Проход по результатам и обновление соответствующих записей в sql_metrics
    for metric_name, description in metric_data:
        # Обновление поля description в sql_metrics, если метрика найдена
        update_stmt = (
            update(sql_metrics)
            .where(sql_metrics.c.metric_name == metric_name)
            .values(description=description)
        )
        result = conn.execute(update_stmt)
        if result.rowcount > 0:
            print(f"Updated metric '{metric_name}' with new description.")
        else:
            print(f"Metric '{metric_name}' not found in sql_metrics.")

print("Done updating descriptions.")

