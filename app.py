import pandas as pd
import numpy as np
import joblib
import streamlit

model=open("model.pkl","rb")
XGBR_model=joblib.load(model)
def xgbr_prediction(var_1,var_2,var_3,var_4,var_5,var_6,var_7,var_8):
    pred_arr=np.array([var_1,var_2,var_3,var_4,var_5,var_6,var_7,var_8])
    preds=pred_arr.reshape(1,-1)
    preds=preds.astype(int)
    model_prediction=XGBR_model.predict(preds)
    return model_prediction

def run():
    streamlit.title("Compressive strength of cement")
    html_temp="""
    """
    streamlit.markdown(html_temp)
    var_1=streamlit.text_input("cement")
    var_2=streamlit.text_input("slag")
    var_3=streamlit.text_input("fly_ash")
    var_4=streamlit.text_input("water")
    var_5=streamlit.text_input("superplasticizer")
    var_6=streamlit.text_input("coarse_aggregate")
    var_7=streamlit.text_input("fine_aggregate")
    var_8=streamlit.text_input("age")

    prediction=""
    if streamlit.button("predict"):
        prediction=xgbr_prediction(var_1,var_2,var_3,var_4,var_5,var_6,var_7,var_8)


        streamlit.success("compressive strength is : {}".format(prediction))

if __name__=='__main__':
    run() 
   

