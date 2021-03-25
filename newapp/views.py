from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    print("ccccc")
    return render(request, 'newapp/index.html')

def form_page(request):
    print("dddd1")
    form = forms.UserInfo()
    print("dddd2")
    if request.method == 'POST':
        print("dddd3")
        # Formで送られたデータを取り出す
        form = forms.UserInfo(request.POST)
        if form.is_valid():# バリデーション(フィールドが正しいかチェック)
            print('バリデーション成功')
            # print(
            #     f"name: {form.cleaned_data['name']}, mail: {form.cleaned_data['mail']}, age: {form.cleaned_data['age']}"
            # )
            print(form.cleaned_data)
            print(form.cleaned_data['name'])
            print("aaaaaaaaaaaaaa")

    print("dddd4")
    return render(
        request, 'newapp/form_page.html', context={
            'form': form
        }
    )
