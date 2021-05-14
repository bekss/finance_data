import re
import os
import csv
import urllib

from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, View
from .forms import UrlForms, ReceivedForms
from .models import Url_File, ReceivedFile
from finance.settings import MEDIA_ROOT
from django.http import JsonResponse
from .request import create_tables, chek_if_table, commit_psql


class ContentView(View):
    form_class = UrlForms
    form_class_csv = ReceivedForms

    def get(self, request):
        return render(request, 'content/content.html', {'forms': self.form_class})

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST, request.FILES)
        if forms.is_valid():

            self.file_read(request.FILES['url_file'])
            return render(request, 'content/success.html', {'file': 'aasf'})
        else:
            return HttpResponse('Not Found Plese choose correct file')

    def file_read(self, txt_file):
        new_doc = Url_File(url_file=txt_file)
        new_doc.save()
        stl_path = f"{MEDIA_ROOT}/{new_doc.url_file.name}"
        sq = f"{MEDIA_ROOT}/received_csv"
        os.chdir(sq)
        with open(stl_path, 'r') as f:
            text = f.read()
            l = text.split()
            for i in l:
                link = str(i)
                b = re.sub("[,]", "", link)
                sec_url = b[b.find("d/") + 2:]
                third_url = '-'.join(sec_url.split('?')[:-1])
                tab_name = third_url.lower()
                if not chek_if_table(tab_name):
                    create_tables(tab_name)
                name_csv = f"{third_url}.csv".lower()
                commit_psql(name_csv, sq, tab_name)
                csv = urllib.request.urlretrieve(b, name_csv)
                path = 'received_csv/' + csv[0]
                entry = ReceivedFile.objects.create(url_file=path)
                entry.save()


class Detail(ListView):
    model = ReceivedFile
    context_object_name = 'file_url'
    template_name = 'content/file.html'


class Json(View):
    sq = f"{MEDIA_ROOT}/received_csv"

    def get(self, request, slug):
        csv_rows = []
        sq = f"{MEDIA_ROOT}/received_csv"
        os.chdir(sq)
        l = os.listdir(os.getcwd())
        csvv = slug + '.csv'
        if csvv in l:
            for i in l:
                files = i.split('.')[0]
                if str(i) == str(slug + '.csv'):
                    filaname = i
            with open(filaname) as csvfile:
                reader = csv.DictReader(csvfile)
                field = reader.fieldnames
                for row in reader:
                    csv_rows.extend([{field[i]: row[field[i]] for i in range(len(field))}])
            return JsonResponse(csv_rows, safe=False)
        else:
            return JsonResponse({'message': 'Not found'})
