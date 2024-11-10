import sqlite3
from database import Database
from typing import List, Dict, Optional

class SQLiteDatabase(Database):
    def __init__(self, db_name: str):
        self.db_name = db_name
        self._create_table()
    
    def _create_table(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
    
    def get_all(self) -> List[Dict]:
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM items')
        rows = cursor.fetchall()
        conn.close()
        return [
            {"id": row[0], "name": row[1], "description": row[2], "price": row[3]}
            for row in rows
        ]
    
    def get(self, id: int) -> Optional[Dict]:
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM items WHERE id = ?', (id,))
        row = cursor.fetchone()
        conn.close()
        if row is None:
            return None
        return {"id": row[0], "name": row[1], "description": row[2], "price": row[3]}
    
    def create(self, item: Dict) -> Dict:
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO items (name, description, price) VALUES (?, ?, ?)',
            (item['name'], item['description'], item['price'])
        )
        item_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return {**item, "id": item_id}
    
    def update(self, id: int, item: Dict) -> Optional[Dict]:
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE items SET name = ?, description = ?, price = ? WHERE id = ?',
            (item['name'], item['description'], item['price'], id)
        )
        conn.commit()
        if cursor.rowcount == 0:
            conn.close()
            return None
        conn.close()
        return {**item, "id": id}
    
    def delete(self, id: int) -> bool:
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM items WHERE id = ?', (id,))
        conn.commit()
        success = cursor.rowcount > 0
        conn.close()
        return success