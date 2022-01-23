from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, text
eng = create_engine('sqlite:///sneakers.db')
meta = MetaData()
sneakers = Table(
   'sneakers', meta,
   Column('id', Integer, primary_key=True),
   Column('name', String),
   Column('count', Float),
   Column('manufacture', String),
   Column('price', Float),
   Column('size', Float),
)
meta.create_all(eng)

while True:
    print('Ваш запрос?\n'
          'add - добавление\n'
          'show me all - отображение всего\n'
          'delete smth - удалить позицию\n'
          'position stats - статистика по позициям\n')
    commands = input()
    if commands == 'add':
        print('Введите название кроссовок:')
        Name = input()
        print('Введите кол-во кроссовок:')
        Count = int(input())
        print('Введите производителя:')
        Manufacture = input()
        print('Введите цену:')
        Price = float(input())
        print('Введите размер:')
        Size = float(input())

        inser = sneakers.insert()
        inser = sneakers.insert().values(name=Name, count=Count, manufacture=Manufacture, price=Price, size=Size)
        con = eng.connect()
        results = con.execute(inser)

        s = sneakers.select()
        con = eng.connect()
        results = con.execute(s)

        for row in results:
            print(row)

    elif commands == 'show me all':
        s = sneakers.select()
        con = eng.connect()
        results = con.execute(s)

        for row in results:
            print(row)

    elif commands == 'delete smth ':
        print('Задайте id для удаления:')
        position = input()

        con = eng.connect()
        stmt = sneakers.delete().where(sneakers.c.id == position)
        con.execute(stmt)

    elif commands == 'position stats':
        con = eng.connect()
        t = text("SELECT COUNT(id) FROM SNEAKERS")
        results = con.execute(t)
        for row in results:
            print(row[0])
