from flask import Flask, render_template, url_for, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    video_url = url_for('static', filename='videos/opening_video.mp4')
    title = "Halaman Utama Game"
    welcome_message = "Selamat datang di Nusan Quiz saya!"
    return render_template('index.html', title=title, message=welcome_message, video_url=video_url)

@app.route('/start-game')
def startGame():
    return render_template('games/index.html')

# route new for access renspy assets in static/games folder
@app.route('/<path:filename>')
def serve_renpy_game_assets_puclic(filename):
    return send_from_directory('static/games/', filename)


@app.route('/riwayat')
def about():
    return render_template('riwayat.html')

@app.route('/profile')
def show_user_profile():
    bg_1 = url_for('static', filename='images/bg-1.jpeg')
    return render_template('profile.html', bg_1=bg_1)

if __name__ == '__main__':
    app.run(debug=True) # debug=True akan otomatis me-reload server saat ada perubahan kode