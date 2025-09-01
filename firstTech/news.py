from django.http import HttpResponse
def todaysNews(request):
          return HttpResponse("<h1>Today is Friday</h1>"
                             +"<h1>Today is Friday</h1>" +"<h2>This is a subtitle</h2>");
def todaysWeather(request):
          return HttpResponse("<h3>It's raining cats and dogs!</h3>" + "<p>it is also a cold day.</p>")