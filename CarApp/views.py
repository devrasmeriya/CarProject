from django.shortcuts import render,HttpResponse
from CarApp.models import CarModel
import pickle
model=pickle.load(open('pick.pkl','rb'))


# Create your views here.
def index(request):
    if request.method=="POST":
        age=request.POST.get('age')
        salary=request.POST.get('salary')
        ans=model.predict([[age,salary]])
        if ans[0]==0:
            text="OOPS ! You should not buy a Car now" 
        else:
            text="Great! You should buy a new Car"
        return render(request,"index.html",context={"text":text})
       
        
    return render(request,"index.html")
