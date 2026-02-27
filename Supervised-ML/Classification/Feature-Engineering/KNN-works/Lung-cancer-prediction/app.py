import streamlit as st
import joblib
st.title(":red[Lung Cancer Prediction]")
model = joblib.load("C:\\Users\\libin_urv2w13\\Desktop\\mljourney\\Supervised-ML\\Classification\\Feature-Engineering\\KNN-works\\Lung-cancer-prediction\\dt_model.pkl")
scaler = joblib.load("C:\\Users\\libin_urv2w13\\Desktop\\mljourney\\Supervised-ML\\Classification\\Feature-Engineering\\KNN-works\\Lung-cancer-prediction\\scaler.pkl")
'ALLERGY ', 'WHEEZING', 'ALCOHOL CONSUMING', 'COUGHING'
ALLERGY = st.number_input("ALLERGY")
WHEEZING = st.number_input("WHEEZING")
ALCOHOL_CONSUMING = st.number_input("ALCOHOL_CONSUMING")
COUGHING = st.number_input("COUGHING")
if st.button("PREDICT DISEASE"):
    test_data = [[ALLERGY,WHEEZING,ALCOHOL_CONSUMING,COUGHING]]
    result = model.predict(scaler.transform(test_data))[0]
    disease_map = {0:'No',1:'Yes'}
    st.success(disease_map.get(result))

