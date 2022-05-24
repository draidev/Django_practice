from django.shortcuts import render
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm

# Create your views here.
def index(request):
    lottos = GuessNumbers.objects.all()
    # 브라우저로부터 넘어온 request를 그대로 template('default.html')에게 전달
    # {} 에는 추가로 함께 전달하려는 object들을 dict로 넣어줄 수 있음
    return render(request, 'lotto/default.html', {'lottos':lottos})


def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!")


def post(request):
    form = PostForm()
    return render(request,"lotto/form.html",{"form":form})