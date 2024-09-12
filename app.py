from flask import Flask,request,render_template,jsonify
from Source.pipeline.prediction_pipeline import CustomData,PredictionPipeline
import pandas as pd

app = Flask(__name__)
@app.route('/')
def homepage():
    return render_template('index.html')
cut_categories = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
clarity_categories = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']
@app.route('/predict',methods=['GET','POST'])
def predict_data():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        data = CustomData(carat = float(request.form['carat']),
            table = float(request.form['table']),
            cut = request.form['cut'],
            color = request.form['color'],
            clarity = request.form['clarity'])
        if data.cut not in cut_categories:
            return jsonify({'error': 'Invalid value for cut'}), 400
        if data.color not in color_categories:
            return jsonify({'error': 'Invalid value for color'}), 400
        if data.clarity not in clarity_categories:
            return jsonify({'error': 'Invalid value for clarity'}), 400

        

        
            
        final_df = data.get_data_as_dataframe()
        predict_pipeline = PredictionPipeline()
        prediction = predict_pipeline.predict(final_df)
        result = prediction
        return render_template('result.html',final_result = result)

        















if __name__ == '__main__':
    app.run(debug = True)