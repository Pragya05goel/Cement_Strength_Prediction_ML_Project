from flask import Flask, render_template, jsonify, request
from src.exception import CustomException
from src.logger import logging as lg
import os,sys
import pandas as pd
from src.pipeline.train_pipeline import TrainPipeline
from src.pipeline.predict_pipeline import CustomData
from src.pipeline.predict_pipeline import PredictionPipeline

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/train")
def train_route():
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()

        return jsonify("Training Successfull.")

    except Exception as e:
        raise CustomException(e,sys)
    

@app.route("/predict", methods = ['POST', 'GET'])
def predict_datapoint():
        if request.method== "GET":
             return "Welcome Back"
        else:
            data=CustomData(
            cement=float(request.form.get('cement')),
            blast_furnace_slag = float(request.form.get('blast_furnace_slag')),
            fly_ash = float(request.form.get('fly_ash')),
            water = float(request.form.get('water')),
            superplasticizer= float(request.form.get('superplasticizer')),
            coarse_aggregate = float(request.form.get('coarse_aggregate')),
            fine_aggregate = request.form.get('fine_aggregate'),
            age= request.form.get('age'))
            
            final_new_data=data.get_data_as_dataframe()
            predict_pipeline=PredictionPipeline()
            pred=predict_pipeline.predict(final_new_data)

            results=round(pred[0],2)

            return render_template('index.html',final_result=results)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug= True)  


    

