from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from prediction.prediction_Model import prd_Model
# Create your views here.

def home(request):
    return render(request,'prediction/index.html')
def register(request):

    # print(request.GET)
    # fname=request.GET['fname']
    # lname=request.GET['lname']
    # con={'variable':'hi'}
    # print(request.GET)
    print(request.GET)
    template=loader.get_template('prediction/result.html')
    # context={'variable':'123','hi':'32343',}
    # data={'HT':request.GET['HT'],
    #         'HD':request.GET['HD']}
            # 'LT':request.GET['LT'],
    prd_value=prd_Model.prd(request.GET['HT'],request.GET['HD'],request.GET['LT'])
   
    data={'result':prd_value}


    # context={'HT':request.GET[''],'lname':request.GET['lname']}
    # print(request.GET['fname'])
    
    # return render(context,'prediction/register.html')
    return HttpResponse(template.render(data,request))
