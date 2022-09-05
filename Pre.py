import streamlit as st
import pandas as pd
import numpy as np
import pickle


app_mode = st.sidebar.selectbox('Select Page',['Home','Predict_StudentStatus'])

if app_mode=='Home':
    st.title('Initiave Project - Smart Academic Advisory App') 
    st.write("""
Non-regular students is defined as student who have Grade Point Average less than 2.0 or the cumulate credits are not multiple of 15. 
This app predicts the probability of a student will be a NR student using student performance data.  
""")
    st.markdown('Dataset :')
    df=pd.read_excel (r'finaldataset.xlsx')
    df = pd.DataFrame(df)
    st.write(df.head())


elif app_mode == 'Predict_StudentStatus':

    st.subheader('Fill in employee details to get prediction ')
    st.sidebar.header("Other details :")
    prop = {'other' : 1,'binusian' : 2, 'regular':3 }
    prop1 = {'beginner': 1, 'intermediate': 2, 'advance': 3}
    prop2 = {'level1': 1, 'level2': 2, 'level3': 3}
    prop3 = {'level1': 1, 'level2': 2, 'level3': 3}
    prop4 = {'employee': 1, 'unemployment': 2, 'other': 3}
    prop5 = {'employee': 1, 'unemployment': 2, 'other': 3}
    prop6= {'alive': 1, 'died': 2}
    
    lokasi = st.selectbox('Campus Location',('Kemanggisan','Alam Sutera'))
    gender = st.selectbox('Gender',('Female', 'Male'))
    scholarship = st.sidebar.radio("Select Scholarship", tuple(prop.keys()))
    english = st.sidebar.radio("Select English Level", tuple(prop1.keys()))
    edufa = st.sidebar.radio("Select Father's' Education ", tuple(prop2.keys()))
    edumo = st.sidebar.radio("Select Mother's' Education ", tuple(prop3.keys()))
    jobfa = st.sidebar.radio("Select Father's' Job ", tuple(prop4.keys()))
    jobmo = st.sidebar.radio("Select MOther's' Job ", tuple(prop5.keys()))
    statmo = st.sidebar.radio("Select Mother's' Status ", tuple(prop6.keys()))
 
    LokasiKuliah_Kemanggisan, LokasiKuliah_AlamSutera = 0, 0 
    if lokasi == 'Kemanggisan': 
          LokasiKuliah_Kemanggisan = 1 
    elif lokasi == 'Alam Sutera': 
          LokasiKuliah_AlamSutera = 1 
    
    Gender_Female, Gender_Male = 0, 0 
    if gender == 'Female': 
          Gender_Female= 1 
    elif gender == 'Male': 
          Gender_Male = 1 
    

    ScholarshipStatus_Other, ScholarshipStatus_binusian, ScholarshipStatus_regular = 0,0,0
    if scholarship == 'other':
        ScholarshipStatus_Other = 1
    elif scholarship == 'binusian':
        ScholarshipStatus_binusian = 1
    elif scholarship == 'regular':
        ScholarshipStatus_regular = 1
    
    
    EnglishScore_Beginner, EnglishScore_Intermediate, EnglishScore_Advance=0,0,0
    if english == 'beginner':
        EnglishScore_Beginner = 1
    elif english == 'intermediate':
        EnglishScore_Intermediate = 1
    elif english == 'advance' :
        EnglishScore_Advance = 1
        
    EducationFa_level1, EducationFa_level2, EducationFa_level3 = 0,0,0
    if edufa == 'level1':
        EducationFa_level1 = 1
    elif edufa == 'level2':
        EducationFa_level2 = 1
    elif edufa == 'level3':
        EducationFa_level3 = 1
        
    EducationMo_level1, EducationMo_level2, EducationMo_level3 = 0,0,0
    if edumo == 'level1':
        EducationMo_level1 = 1
    elif edumo == 'level2':
        EducationMo_level2 = 1
    elif edumo == 'level3':
        EducationMo_level3 = 1
    
    FaJob_Employee, FaJob_Other,FaJob_Unemployement = 0,0,0
    if jobfa == 'employee':
        FaJob_Employee = 1
    elif jobfa == 'unemployment':
        FaJob_Unemployement = 1
    elif jobfa == 'other':
        FaJob_Other = 1
    
    
    MoJob_Employee, MoJob_Other,MoJob_Unemployement = 0,0,0
    if jobmo == 'employee':
        MoJob_Employee = 1
    elif jobmo == 'unemployment':
        MoJob_Unemployement = 1
    elif jobmo == 'other':
        MoJob_Other = 1
        
    StatusMo_alive, StatusMo_died = 0,0
    if statmo =='alive':
        StatusMo_alive = 1
    elif statmo == 'died': 
        StatusMo_died = 1
    
    subdata={
        'lokasi':[LokasiKuliah_Kemanggisan, LokasiKuliah_AlamSutera],
        'gender':[Gender_Female, Gender_Male] ,
        'scholarship':[ScholarshipStatus_Other, ScholarshipStatus_binusian, ScholarshipStatus_regular],
        'english':[EnglishScore_Beginner, EnglishScore_Intermediate, EnglishScore_Advance],
        'edufa': [EducationFa_level1, EducationFa_level2, EducationFa_level3],
        'edumo': [EducationMo_level1, EducationMo_level2, EducationMo_level3],
        'jobfa':[FaJob_Employee, FaJob_Other,FaJob_Unemployement],
        'jobmo':[MoJob_Employee, MoJob_Other,MoJob_Unemployement],
        'statmo':[ StatusMo_alive, StatusMo_died]
        }
        
    features = [subdata['gender'][1],subdata['gender'][0],subdata['scholarship'][0],subdata['scholarship'][1], subdata['scholarship'][2],subdata['english'][2],subdata['english'][0], subdata['english'][1], subdata['jobfa'][0],subdata['jobfa'][2], subdata['jobfa'][1],subdata['jobmo'][0],subdata['jobmo'][2], subdata['jobmo'][1],subdata['edufa'][0],subdata['edufa'][1], subdata['edufa'][2],subdata['edumo'][0],subdata['edumo'][1], subdata['edumo'][2], subdata['statmo'][0], subdata['lokasi'][1],subdata['lokasi'][0]]

    
    results = np.array(features).reshape(1, -1)

    if st.button("Predict"):

        picklefile = open("main/modelLogR.pkl", "rb")
        model = pickle.load(picklefile)

        prediction = model.predict(results)
        if prediction[0] == 0:
            st.success('student is non-NR')
        elif prediction[0] == 1:
            st.error( 'student is NR')
