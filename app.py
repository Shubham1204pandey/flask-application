from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', count=None)

@app.route('/count', methods=['POST'])
def count():
    strings = request.form.get('strings')
    tobefound = request.form.get('tobefound')
    tobefound = tobefound.lower()
    c = 0
    strings_lower = strings.lower()
    l = strings_lower.split(" ")
    for i in l:
        if tobefound.lower() in i.lower():
            c += i.count(tobefound)
        # return render_template('index.html', count=c, strings=strings)
    return render_template('index.html', count=c, tobefound=tobefound, strings=strings)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)