from flask import Flask, request, render_template
import numpy as np
#import scipy
from scipy import stats
#from scipy.stats import norm

app = Flask(__name__)

def get_pvalue(mean_control, std_control, nobs_control, mean_test, std_test, nobs_test):
    return round(stats.ttest_ind_from_stats(mean_control, std_control, nobs_control, mean_test, std_test, nobs_test, equal_var = True)[1],3)

@app.route("/")
def home():
    return render_template('page.html') 

@app.route("/detector", methods = ['POST'])
def emotion_detector():
    message = [item for item in request.form.values()]
    mean_control = int(message[0])
    std_control = int(message[1])
    nobs_control = int(message[2])

    mean_test = int(message[3])
    std_test = int(message[4])
    nobs_test = int(message[5])

    pvalue = get_pvalue(mean_control, std_control, nobs_control, mean_test, std_test, nobs_test)

    return render_template('page.html', prediction_text = 'P-value is: {}'.format(str(pvalue)))

if __name__  == '__main__': 
    app.run(debug=True)