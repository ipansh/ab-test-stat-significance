from flask import Flask, request, render_template
import formulas

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('two_sample_proportion.html')

@app.route("/two_sample_proportion")
def two_sample_proportion_page():
    return render_template('two_sample_proportion.html')

@app.route("/student_ttest")
def student_ttest_page():
    return render_template('student_ttest.html')

@app.route("/pvaluestudent", methods = ['POST'])
def pvalue_student_page():
    message = [item for item in request.form.values()]
    
    mean_control = int(message[0])
    std_control = int(message[1])
    nobs_control = int(message[2])

    mean_test = int(message[3])
    std_test = int(message[4])
    nobs_test = int(message[5])

    pvalue = formulas.get_pvalue_student(mean_control, std_control, nobs_control, mean_test, std_test, nobs_test)

    pvalue = float(pvalue)
    pvalue = round(pvalue,4)

    if pvalue < 0.05:
      pvalue_explanation = 'is statistically significant and you can reject the null hypothesis. You can be 95% confident that the results are not due to chance.'
    else:
      pvalue_explanation = 'is not statistically significant and you can accept the null hypothesis.'


    return render_template('student_ttest.html', prediction_text1 = 'P-value is: {}, which means that the result {}'.format(str(pvalue), pvalue_explanation))

@app.route("/pvalueconversion", methods = ['POST'])
def pvalue_conversion_page():
    message = [item for item in request.form.values()]
    
    numerator_control = int(message[0])
    denominator_control = int(message[1])

    numerator_test = int(message[2])
    denominator_test = int(message[3])    

    pvalue = formulas.get_pvalue_conversion(denominator_control, numerator_control, denominator_test, numerator_test)
    pvalue = float(pvalue)
    pvalue = round(pvalue,4)

    if pvalue < 0.05:
      pvalue_explanation = 'is statistically significant and you can reject the null hypothesis. You can be 95% confident that the results are not due to chance.'
    else:
      pvalue_explanation = 'is not statistically significant and you can accept the null hypothesis.'


    return render_template('two_sample_proportion.html', prediction_text2 = 'P-value is: {}, which means that the result {}'.format(str(pvalue), pvalue_explanation))

if __name__  == '__main__': 
    app.run(debug=True)