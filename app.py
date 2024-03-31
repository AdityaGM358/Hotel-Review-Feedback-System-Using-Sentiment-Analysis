from flask import Flask, request, jsonify, render_template,  redirect, url_for, send_file
from test_string import predict,predict_file,predict_file_stats # replace with the name of your sentiment analysis script

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/result/<string:result1>')
def result(result1):
    return render_template('result.html', result=result1)


'''@app.route('/download')
def download():
    path = 'C:\\Users\\Rohan bn\\Desktop\\project\\templates\\result.csv'
    return send_file(path, as_attachment=True)

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    f.save(f.filename)
    #res=predict_file(f.filename)
    predict_file(f.filename)
    return render_template("download.html")
    #print("sent upload result", res)
    #return redirect(url_for("fileresult",result1=res))'''

@app.route('/download/<string:result1>')
def download(result1):
    #path = 'C:\\Users\\Rohan bn\\Desktop\\project\\templates\\result.csv'
    #return send_file(path, as_attachment=True)
    return render_template('newdownload.html', result=result1)

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    f.save(f.filename)
    res = predict_file_stats(f.filename)
    #return render_template("download.html")
    print("sent upload result", res)
    return redirect(url_for("download",result1=res))

@app.route('/analyze', methods=['POST'])
def analyze():
    print("analysing")
    sentence = request.form['sentence']
    print("got sentence")
    res = predict(sentence)
    print("sent analyse result", res)
    return redirect(url_for("result",result1=res))



if __name__ == '__main__':
    app.run(debug=True)