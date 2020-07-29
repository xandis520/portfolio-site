from django.urls import path
from .views import (portfolio_list_view,
                    TrendLine,
                    ChartData,
                    ex_trend_line_view,
                    ExChartData,)

app_name = 'album'
urlpatterns = [
    path('', portfolio_list_view, name='portfolio-list'),
    path('trend_line/', TrendLine.as_view(), name='trend-line'),
    path('trend_line/chart/data/', ChartData.as_view(), name='chart-data'),
    path('trend_line/<int:id>/', ex_trend_line_view, name='trend-line-example'),
    path('trend_line/data/example/', ExChartData.as_view(), name='chart-data-example'),
    ]
