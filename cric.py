from flask import Flask, request, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'cricket_db'

# Initialize MySQL
mysql = MySQL(app)

# Helper functions
def get_cursor():
    return mysql.get_db().cursor()

def commit_changes():
    mysql.get_db().commit()

# Routes
@app.route('/', methods=['GET'])
def greet():
    return "Hello, welcome to the Cricket API!"

@app.route('/api/admin/signup', methods=['POST'])
def register_admin():
    data = request.json
    username = data['username']
    password = data['password']
    email = data['email']

    cur = get_cursor()
    cur.execute(
        "INSERT INTO users (username, password, email, role) VALUES (%s, %s, %s, %s)",
        (username, password, email, 'admin')
    )
    commit_changes()
    cur.close()

    return jsonify({
        "message": "Admin account successfully created",
        "status_code": 200,
        "user_id": cur.lastrowid
    })

@app.route('/api/admin/login', methods=['POST'])
def login_user():
    data = request.json
    username = data['username']
    password = data['password']

    cur = get_cursor()
    cur.execute(
        "SELECT * FROM users WHERE username = %s AND password = %s",
        (username, password)
    )
    user = cur.fetchone()

    if user:
        return jsonify({
            "status": "Login successful",
            "status_code": 200,
            "user_id": user[0],
            "access_token": "dummy_token"
        })

    return jsonify({
        "status": "Incorrect username/password provided. Please retry",
        "status_code": 401
    })

@app.route('/api/matches', methods=['POST'])
def create_match():
    data = request.json
    team_1 = data['team_1']
    team_2 = data['team_2']
    date = data['date']
    venue = data['venue']

    cur = get_cursor()
    cur.execute(
        "INSERT INTO matches (team_1, team_2, date, venue) VALUES (%s, %s, %s, %s)",
        (team_1, team_2, date, venue)
    )
    commit_changes()
    cur.close()

    return jsonify({
        "message": "Match created successfully",
        "match_id": cur.lastrowid
    })

@app.route('/api/matches', methods=['GET'])
def get_match_schedules():
    cur = get_cursor()
    cur.execute("SELECT * FROM matches")
    matches = cur.fetchall()

    return jsonify({"matches": matches})

@app.route('/api/matches/<match_id>', methods=['GET'])
def get_match_details(match_id):
    cur = get_cursor()
    cur.execute("SELECT * FROM matches WHERE match_id = %s", (match_id,))
    match = cur.fetchone()

    if match:
        squads = {
            "team_1": [
                {"player_id": "1001", "name": "Virat Kohli"},
                {"player_id": "1002", "name": "Rohit Sharma"}
            ],
            "team_2": [
                {"player_id": "1003", "name": "Jasprit Bumrah"},
                {"player_id": "1004", "name": "Hardik Pandya"}
            ]
        }

        match_details = {
            "match_id": match[0],
            "team_1": match[1],
            "team_2": match[2],
            "date": match[3].strftime('%Y-%m-%d'),
            "venue": match[4],
            "status": "upcoming",
            "squads": squads
        }

        return jsonify(match_details)

    return jsonify({"message": "Match not found", "status_code": 404})

@app.route('/api/players/<player_id>/stats', methods=['GET'])
def get_player_stats(player_id):
    # Retrieve player statistics from the database based on player_id
    player_stats = {
        "player_id": player_id,
        "name": "Virat Kohli",
        "matches_played": 200,
        "runs": 12000,
        "average": 59.8,
        "strike_rate": 92.5
    }

    return jsonify(player_stats)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
