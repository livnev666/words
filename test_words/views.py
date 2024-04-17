from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Text
from .forms import FileForm, ProfileSearchForm
from collections import defaultdict

# Create your views here.


class File_View(CreateView):

    model = Text
    form_class = FileForm
    template_name = 'test_words/add_file.html'
    success_url = 'list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить файл'
        return context


class List_Words(ListView):

    model = Text
    form_class = ProfileSearchForm
    template_name = 'test_words/list_words.html'
    context_object_name = 'word'
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class(self.request.GET)
        if form.is_valid():
            my_object = Text.objects.all().last()
            with my_object.file_name.open('r') as file:
                lines = file.readline().split()
                all_words = []
                while lines:
                    all_words.extend(lines)
                    lines = file.readline().split()
                    res = [',', ':', ';', '.']
                    for i in res:
                        for word in all_words:
                            if i in word:
                                word = word.replace(i, '')
                                all_words.append(word)
                    idf = defaultdict(float)
                    for doc in all_words:
                        idf[doc] += 1
                    idf = {key: (1 / value) for (key, value) in idf.items()}

        context.update({

            'word': all_words[:50],
            'count': all_words[:50].count(form.cleaned_data['name']),
            'idf': sorted(idf.values()),

            # Эта строка кода работает, когда открыт url list/
            # 'idf': idf[form.cleaned_data['name']]

        })
        return context





