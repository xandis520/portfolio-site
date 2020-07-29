from django.shortcuts import render
from django.views.generic import View
from .models import TrendLineExample

# Trend line
from .trend_line import *

# Rest framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

def portfolio_list_view(request, *args, **kwargs):
    context = {
        "instagram": 'https://www.instagram.com/adrian__wlodarczyk/',
        "behance": 'https://www.behance.net/adrianwlod',
        "github": 'https://github.com/xandis520?tab=repositories',
        "github_website": 'https://github.com/xandis520?tab=repositories'
    }
    return render(request, 'album/portfolio_list.html', context)

class TrendLine(View):
    template_name = 'album/trend_line.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None, *args, **kwargs):
        table = [280, 290, 320, 340, 350, 360, 420, 410, 350, 320, 310, 280, 220, 200, 180, 160, 120, 110, 100, 70, 65,
                 60, 45, 30, 20, 18, 15, 16, 17, 18, 20, 22, 25, 28, 35, 39, 45, 46, 50, 52, 56, 60, 80, 90, 92, 93, 95,
                 100, 110, 120]
        default_items = table_all(table=table, step=4)
        data = {
            'labels': default_items[0],
            'default': default_items[1:],
        }
        return Response(data)

def ex_trend_line_view(request, id):
    data = TrendLineExample.objects.get(id=id)
    context = {
        'id': id,
        'data': data,
    }
    return render(request, "album/trend_line_example.html", context)

class ExChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None, *args, **kwargs):
        import ast
        obj = TrendLineExample.objects.all()
        labels = []
        default_items = []
        trend = []
        for object in obj:
            table = ast.literal_eval(object.stock_data)
            item = table_all(table=table, step=int(object.step))
            labels.append(item[0])
            default_items.append(item[1:4])
            trend.append(item[4:])

        data = {
            'labels': labels,
            'default': default_items,
            'trend': trend,
        }
        return Response(data)