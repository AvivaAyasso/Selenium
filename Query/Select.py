from DB import DB

class Select(DB):
    cxnx = DB()
    print(cxnx.connect("select first_name from  actor",'select'))
    print(cxnx.connect("select * from  film",'select'))
    print(cxnx.connect("select * from  city",'select'))
    print(cxnx.connect("select * from  address",'select'))
