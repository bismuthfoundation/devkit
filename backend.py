import sys
sys.path.append("d:/bismuth")
import essentials
import sqlite3

class DbHandler():
    def __init__(self):
        self.database = sqlite3.connect("D:/Bismuth/static/ledger.db")
        self.database.text_factory = str
        self.cursor = self.database.cursor()
        self.limiter = None
        self.limit = -1

dbhandler = DbHandler()

def getbyop(operation):
    print(dbhandler.limiter)

    if dbhandler.limiter:
        dbhandler.cursor.execute("SELECT * FROM transactions WHERE ? in (address|recipient) AND operation = ? ORDER BY block_height DESC LIMIT ?", (dbhandler.limiter, operation,dbhandler.limit,))
        result = dbhandler.cursor.fetchall()

    else:
        dbhandler.cursor.execute("SELECT * FROM transactions WHERE operation = ? ORDER BY block_height DESC LIMIT ?", (operation,dbhandler.limit,))
        result = dbhandler.cursor.fetchall()


    if result:
        return_value = []
        for entry in result:
            return_value.append(essentials.format_raw_tx(entry))
        return return_value


def getbydata(data):
    print(dbhandler.limiter)
    if dbhandler.limiter:
        dbhandler.cursor.execute("SELECT * FROM transactions WHERE ? in (address|recipient) AND openfield = ?  ORDER BY block_height DESC LIMIT ?", (dbhandler.limiter, data ,dbhandler.limit,))
        result = dbhandler.cursor.fetchall()

    else:
        dbhandler.cursor.execute("SELECT * FROM transactions WHERE openfield = ? ORDER BY block_height DESC LIMIT ?", (data,dbhandler.limit,))
        result = dbhandler.cursor.fetchall()

    if result:
        return_value = []
        for entry in result:
            return_value.append(essentials.format_raw_tx(entry))
        return return_value