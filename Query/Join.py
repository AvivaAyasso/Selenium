from DB import DB

class Join(DB):
    cxnx = DB()
    a = (cxnx.connect("SELECT a.phone,c.city FROM address as a join city as c on a.city_id = c.city_id",'select'))
    print(a)
    b = (cxnx.connect("SELECT a.phone,c.city FROM address as a join city as c on a.city_id = c.city_id WHERE city like 'Ahmadnagar'",'select'))
    print(b)
    c = (cxnx.connect("SELECT a.phone,c.city FROM address as a join city as c on a.city_id = c.city_id WHERE city like 'as%'",'select'))
    print(c)
    d = (cxnx.connect("SELECT a.phone,c.city FROM address as a join city as c on a.city_id = c.city_id WHERE city like '%s%'",'select'))
    print(d)
    e = (cxnx.connect("SELECT a.phone,c.city FROM address as a join city as c on a.city_id = c.city_id WHERE phone like '%99%'",'select'))
    print(e)