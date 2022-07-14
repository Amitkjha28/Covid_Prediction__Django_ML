import pickle
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
with open("covidapp/save_model/rfc_model.pkl","rb") as myfile :
    mymodel= pickle.load(myfile)
def myindex(request):
    # return HttpResponse('<h1> covid prediction app</h1>')
    return render(request, 'index.html')

def myresult(request):
    name = request.POST.get('username')
    age = request.POST.get('age')
    sex = request.POST.get('sex')
    ptype = request.POST.get('ptype')
    intube = request.POST.get('intube')
    pneumonia = request.POST.get('pneumonia')
    pregnancy = request.POST.get('pregnancy')
    diabetes = request.POST.get('diabetes')
    copd = request.POST.get('copd')
    asthma = request.POST.get('asthma')
    inmsupr = request.POST.get('inmsupr')
    hypertension = request.POST.get('hypertension')
    cardiovascular = request.POST.get('cardiovascular')
    obesity = request.POST.get('obesity')
    renalchronic = request.POST.get('renalchronic')
    tobacco = request.POST.get('tobacco')
    contactothercovid = request.POST.get('contactothercovid')
    icu = request.POST.get('icu')
    otherdisease = request.POST.get('otherdisease')
    # print(" Name : {}\n Age : {}\n Sex : {}\n patient_type :{}\n intubed :{}\n pneumonia : {}\n pregnancy : {}\n"
    #       " diabetes : {}\n copd : {}\n asthma : {}\n inmsupr : {}\n hypertension : {}\n other_disease : {}\n "
    #       "cardiovascular : {}\n obesity : {}\n renal_chronic : {}\n tobacco : {}\n contact_other_covid : {}\n "
    #       "icu : {}\n".format( name,age,sex,ptype,intube,pneumonia,pregnancy,diabetes,copd,asthma,inmsupr,
    #                            hypertension,otherdisease,cardiovascular,obesity,renalchronic,tobacco,
    #                            contactothercovid,icu))
    Prediction = mymodel.predict_proba([[age, sex, ptype, intube, pneumonia, pregnancy, diabetes, copd,
                                         asthma, inmsupr,hypertension,otherdisease, cardiovascular, obesity,
                                         renalchronic, tobacco, contactothercovid, icu]])
    # print("Prediction : ", Prediction)
    result_predict =round(Prediction[[0]][0][0]*100,2)

    return render(request,'result.html',{'resultpredict':result_predict,'name':name})