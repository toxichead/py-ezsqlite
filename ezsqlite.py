import sqlite3

class EzSQLite3():
    def __init__(self, db: str = "sqlite.db"):
        self.connection = sqlite3.connect(db)
        #self.cursor = sqlite_connection.cursor()
    def query(self, query: str = ""):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            try:
                record = cursor.fetchall()
                cursor.close()
                return {"status": True, "details": record} 
            except:
                try: cursor.close()
                except: pass
                finally: return {"status": True, "details": None} 
        except Exception as e: return {"status": False, "details": str(e)} 
    def close(self):
        self.connection.close()
