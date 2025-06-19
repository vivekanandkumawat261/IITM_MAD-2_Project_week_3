from flask import Flask, request, jsonify
from flask_cors import CORS 
import sqlite3
from tasks import process_reply 

app = Flask(__name__)
CORS(app)

DB = 'database.db'

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''
            CREATE TABLE IF NOT EXISTS replies (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              message TEXT NOT NULL
              )
              ''')
    
    conn.commit()
    conn.close()


@app.route('/replies', methods=['GET'])
def get_replies():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT id, message FROM replies")
    rows = c.fetchall()
    conn.close()
    return jsonify([{"id": r[0],"message": r[1]} for r in rows])


@app.route('/replies', methods=['POST'])
def add_reply():
    data = request.json
    message = data['message']
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('INSERT INTO replies (message) VALUES (?) ', (message,))
    conn.commit()
    conn.close()

    process_reply.delay(message)
    return jsonify({"status": "ok"})


@app.route('/replies/<int:id>',methods=['DELETE'])
def delete_reply(id):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('DELET FROM replies WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({"status": "deleted"})

if __name__=='__main__':
    init_db()
    app.run(debug=True)
