from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    title = "Halaman Utama Game"
    welcome_message = "Selamat datang di Nusan Quiz saya!"
    return render_template('index.html', title=title, message=welcome_message)

@app.route('/riwayat')
def about():
    return render_template('riwayat.html')

@app.route('/profile')
def show_user_profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True) # debug=True akan otomatis me-reload server saat ada perubahan kode