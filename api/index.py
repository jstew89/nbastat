from flask import Flask, request, jsonify
from nba_api.stats.endpoints import commonplayerinfo

app = Flask(__name__)

@app.route('/player-info', methods=['GET'])
def get_player_info():
    player_name = request.args.get('name')
    if not player_name:
        return jsonify({'error': 'Player name is required'}), 400

    # Use nba_api to fetch player information
    try:
        player = commonplayerinfo.CommonPlayerInfo(player_name)
        return jsonify(player.get_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
