from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from src.pipeline.predict_pipeline import CustomData, PredictPipeline


application = Flask(__name__)
app = application
# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data=CustomData(
            latitude=request.form.get("latitude"),
            longitude=request.form.get("longitude"),
            size_in_sqft=request.form.get("size_in_sqft"),
            no_of_bedrooms=request.form.get("no_of_bedrooms"),
            no_of_bathrooms=request.form.get("no_of_bathrooms"),
            quality=request.form.get("quality"),
            maid_room=request.form.get("maid_room"),
            unfurnished=request.form.get("unfurnished"),
            balcony=request.form.get("balcony"),
            barbecue_area=request.form.get("barbecue_area"),
            built_in_wardrobes=request.form.get("built_in_wardrobes"),
            central_ac=request.form.get("central_ac"),
            childrens_play_area=request.form.get("childrens_play_area"),
            childrens_pool=request.form.get("childrens_pool"),
            concierge=request.form.get("concierge"),
            covered_parking=request.form.get("covered_parking"),
            kitchen_appliances=request.form.get("kitchen_appliances"),
            lobby_in_building=request.form.get("lobby_in_building"),
            maid_service=request.form.get("maid_service"),
            networked=request.form.get("networked"),
            pets_allowed=request.form.get("pets_allowed"),
            private_garden=request.form.get("private_garden"),
            private_gym=request.form.get("private_gym"),
            private_jacuzzi=request.form.get("private_jacuzzi"),
            private_pool=request.form.get("private_pool"),
            security=request.form.get("security"),
            shared_gym=request.form.get("shared_gym"),
            shared_pool=request.form.get("shared_pool"),
            shared_spa=request.form.get("shared_spa"),
            study=request.form.get("study"),
            vastu_compliant=request.form.get("vastu_compliant"),
            view_of_landmark=request.form.get("view_of_landmark"),
            view_of_water=request.form.get("view_of_water"),
            walk_in_closet=request.form.get("walk_in_closet"),
            )
        pred_df = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        result = round(predict_pipeline.predict(pred_df)[0], -3)
        return render_template('home.html', results=f'Property price should be approx:- {result}')




if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)