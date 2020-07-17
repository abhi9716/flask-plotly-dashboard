from flask import Flask, render_template, request, jsonify, make_response
from plot import *

feats, prod = feature()

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
	feat_list=feats
	prod_list=prod
	feat_list=[x.replace(" ", "_") for x in (feat_list)]
	word_freqs_js,max_freq = word_cloud(feats[0],prod_list[0])
	bar = create_plot(word_freqs_js)
	return render_template('main.html', my_list=feat_list, prod_list=prod_list, plot=bar,plot1=bar, word_freqs=word_freqs_js, max_freq=max_freq)

@app.route('/bar', methods=['GET', 'POST'])
def bar():
    if request.method == 'POST':
	    req = request.get_json()
	    a=" ".join(req["feat"].split("_"))
	    b=int(req["prod"])
	    res=make_response(jsonify({"message":"massage"}),200)
	    word_freqs_js,max_freq = word_cloud(a,b)
	    plot=create_plot(word_freqs_js)
	    return jsonify({"word_freqs":word_freqs_js,"max_freq":max_freq, "plot":plot})

if __name__ == '__main__':
	app.run(debug=True)