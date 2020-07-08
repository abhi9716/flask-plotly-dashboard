from flask import Flask, render_template, request, jsonify, make_response
from plot import *
feats=feature()

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def index():

	my_list=feats
	print(my_list)
	my_list=[x.replace(" ", "_") for x in (my_list)]
	feat=request.args.get("gender")
	bar = create_plot()
	word_freqs_js,max_freq = word_cloud(feats[0])

	return render_template('main.html', my_list=my_list, plot=bar,plot1=bar, word_freqs=word_freqs_js, max_freq=max_freq)



@app.route('/bar', methods=['GET', 'POST'])
def bar():

    if request.method == 'POST':
	    req = request.get_json()
	    a=" ".join(req["name"].split("_"))
	    res=make_response(jsonify({"message":"massage"}),200)
	    word_freqs_js,max_freq = word_cloud(a)

	    return jsonify({"word_freqs":word_freqs_js,"max_freq":max_freq})

    
if __name__ == '__main__':
	app.run(debug=True,port=5001)