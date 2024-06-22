from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shamba')
def shamba():
    return render_template('shamba.html')

@app.route('/tai-mashambani')
def tai_mashambani():
    return render_template('tai-mashambani.html')

# Add routes for other sections (tai-experiences, duka, kahawa-mashambani, tai-community-center) similarly

if __name__ == '__main__':
    app.run(debug=True)
