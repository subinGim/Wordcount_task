from django.shortcuts import render, redirect, get_object_or_404
from .models import Fulltext
from .forms import FulltextForm

# Create your views here.
def home(request):
    return render(request, 'wordcount/home.html')

def about(request):
    return render(request, 'wordcount/about.html')

def result(request):
    # text = get_object_or_404(Fulltext)
    text = request.GET['fulltext']
    words = text.split() #문자열을 공백 기준으로 리스트에 저장해줌.
    word_dict = {}#딕셔너리 사용하여 단어 개수 측정 ex.{내:1, 이름은:2, 민철이야:1, .... }
    
    for word in words:
        if word in word_dict:
            word_dict[word]+=1
        else:
            word_dict[word]=1

    return render(request, 'wordcount/result.html', {'full':text, 'total':len(words), 'dict':word_dict.items})
    # return resultform(request, text)

# def resultform(request, fulltext=None):
#     if request.method == 'POST':
#         form = FulltextForm(request.POST, instance=fulltext)
#         if form.is_valid():
#             fulltext = form.save()
#             return redirect('home')
    
#     else:
#         form = FulltextForm(instance=fulltext)
#         return render(request, 'wordcount/home.html', {'form':form})