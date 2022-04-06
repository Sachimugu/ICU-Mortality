from django.shortcuts import render
import joblib
# Create your views here.

def Home(request):

    if request.method == "POST":

        model=joblib.load('job_rf.pkl')
        data= []
        data.append(request.POST["index0"])
        data.append(request.POST["index1"])
        data.append(request.POST["index2"])
        data.append(request.POST["index3"])
        data.append(request.POST["index4"])
        data.append(request.POST["index5"])
        data.append(request.POST["index6"])
        data.append(request.POST["index7"])
        data.append(request.POST["index8"])
        data.append(request.POST["index9"])
        data.append(request.POST["index10"])
    
        prediction=model.predict([data])[0]

        if prediction > 0:
            context = {'pred_result':'ICU MORTALITY IS HIGH'}
        else:
            context = {'pred_result':'ICU MORTALITY IS LOW'}
    else:
        context={}

    return render(request, 'IcuMortality/home.html', context=context )

