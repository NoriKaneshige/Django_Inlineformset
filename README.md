# Django_Inlineformset


[referred blog](https://narito.ninja/blog/detail/32/)

![inlineformset](inlineformset.gif)

> ## models.py
``` python
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField('title', max_length=200)
    text = models.TextField('content')
    date = models.DateTimeField('date', default=timezone.now)

    def __str__(self):
        return self.title

class File(models.Model):
    name = models.CharField('file name', max_length=255)
    src = models.FileField('attach file')
    target = models.ForeignKey(
        Post, verbose_name='related post',
        blank=True, null=True,
        on_delete=models.SET_NULL
    )
```

> ## admin.py
``` python

```

> ## views.py
``` python

```

> ## urls.py
``` python

```

> ## base.html
``` python

```

> ## post_list.html
``` python

```
> ## post_form.html
``` python

```
