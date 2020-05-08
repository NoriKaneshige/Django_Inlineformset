from django import forms
from .models import Post, File


class PostCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Post
        fields = '__all__'

# This is inlineformset!
# Post is parent models, File it models of inlineformset, in this case here
# max_num can limit mmaximum number of files
FileFormset = forms.inlineformset_factory(
    Post, File, fields='__all__',
    extra=5, max_num=5, can_delete=False
)