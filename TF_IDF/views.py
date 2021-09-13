from collections import defaultdict
import string

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UploadFileForm

from .models import Words, Files
# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file
# import django_tables2 as tables DONT WORK WITH SLICE

# DONT WORK WITH SLICE
# class FinTable(tables.Table):
#     class Meta:
#         model = Words
#         fields = ('word', 'tf', 'idf')


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            queryset = handle_uploaded_file(request.FILES['file'])
            # table = FinTable(queryset[0:50]) DONT WORK WITH SLICE
            return render(request, "TF_IDF/table.html", {"words": queryset})# context_instance=RequestContext(request)
            # return HttpResponse(content)
    else:
        form = UploadFileForm()
    return render(request, template_name='TF_IDF/upload.html', context={'form': form})


def handle_uploaded_file(upload_file):
    file_instance = create_new_file(upload_file)
    create_new_words(upload_file,file_instance)
    query = Words.objects.filter(file=file_instance).order_by('-idf').values('word', 'tf', 'idf' )
    return query

def create_new_words(upload_file,file_instance):
    # file_id = create_new_file(f)
    file_words = defaultdict(int)  # TODO how we can use collections.Counter
    file_words_count = 0
    for chunk in upload_file.chunks():
        chunk_string = chunk.decode("utf-8")
        chunk_string = chunk_string.translate(str.maketrans('', '', string.punctuation))
        chunk_words = chunk_string.split()
        for word in chunk_words:
            file_words[word] += 1
        file_words_count += len(chunk_words)
    for word, count in file_words.items():
        tf = count / file_words_count
        word = Words(word=word, tf=round(tf,3), file=file_instance)
        word.save()
        files_count = Words.objects.all().values('file').distinct().count()
        count = Words.objects.filter(word=word.word).count()
        idf = count / files_count
        word.idf = round(idf,3)
        word.save()


def create_new_file(f):
    new_file = Files(file_name=f.name)
    new_file.save()
    return new_file

# def calc_idf(word, files_count):
#     # for_render = defaultdict(dict)
#     # files_count = Words.objects.all().values('file').distinct().count()
#     # words = Words.objects.all().values('word').distinct()[:50]
#     # for i in words:
#     # word = i['word']
#     # tf = Words.objects.filter(word=word).values('tf')
#     count = Words.objects.filter(word=word).count()
#     idf = count / files_count

    #     for_render[word]=dict(word=word, tf=tf, idf=idf)
    # print(for_render)



        # (User.objects
        #  .values('is_active')
        #  .annotate(total=Count('id')))
