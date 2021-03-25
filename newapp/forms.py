from django import forms


class UserInfo(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    mail = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd', 'class': 'myclass'}))
    is_married = forms.BooleanField()
    birtyday = forms.DateField()
    salary = forms.DecimalField()
    job = forms.ChoiceField(choices=(
        (1, '正社員'),
        (2, '自営業'),
        (3, '学生'),
        (4, '無職')
    ))
    hobbies = forms.MultipleChoiceField(choices=(
        (1, 'スポーツ'),
        (2, '読書'),
        (3, '映画鑑賞'),
        (4, 'その他')
    ))
    homepage = forms.URLField()
