from DB import DB

class Update(DB):
    cxnx = DB()
    (cxnx.connect("UPDATE actor SET first_name = 'AVIVA' WHERE first_name = 'PENELOPE'",'update'))

    (cxnx.connect("UPDATE actor SET first_name = 'AVI' WHERE first_name = 'NICK'", 'update'))

    (cxnx.connect("UPDATE actor SET first_name = 'ISRAEL' WHERE first_name = 'ED'",'update'))

    (cxnx.connect("UPDATE actor SET first_name = 'BETTY' WHERE first_name = 'JENNIFER'",'update'))

    (cxnx.connect("UPDATE actor SET first_name = 'ASAF' WHERE first_name = 'JOHNNY'",'update'))
    print(cxnx.connect("SELECT first_name FROM actor",'select'))

