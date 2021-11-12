from django.http.response import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from .models import Movie, Genre
import requests
# Create your views here.

def index(request):
    movies = get_list_or_404(Movie)

    context  = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


def recommend(request):
    # user_gerne = request.user.genre
    # User에 장르 값 필요해서 일단 이렇게만 놔둠
    # 장르 값 찾기  filter에 
    genre = Movie.objects.filter(pk=3).values('genres')[0]['genres']
    recommend_movies = Movie.objects.filter(genres=genre)

    context={
        'movies': recommend_movies
    }

    return render(request, 'movies/recommend.html', context)

def weather(request):
    # URL 과 API키로 날씨 받아오기. city를 넣어줘서 도시 기준으로 했는데 이부분 현재 위치 구하는 기능 구현해서 위도경도로 현재 날씨 구할 수 있도록 해야할듯.
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=API_KEY'
    city = 'Tokyo'
    city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
    # 필요한 정보들만 가져오기
    weather = {
        'city' : city,
        'main' : city_weather['weather'][0]['main'],
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }
    
    # 일단 딕셔너리로 날씨에 장르들 하나씩을 선택 하도록 함(더 좋은 방법 있으면 그걸로 구현)
    lst = {'clear sky': 28 ,'few clouds': 12,'overcast cloud':16,'drizzle':35,'rain':80,'shower rain':99,'thunderstorm':18,
            'snow':10751, 'mist':14,'broken clouds':27,'scattered clouds':10749}
    genre = lst[weather['description']]
    # 장르와 같은 영화 정보들 가지고오기 
    movies = Movie.objects.filter(genres=genre)
    context = {
        'weather' : weather,
        'movies':movies,
        }

    return render(request, 'movies/weather.html',context)




    url = 'api.openweathermap.org/data/2.5/weather?q=daegu&appid=b1a32c0fd2033a695051df3761f95526'
    city= 'Daegu'
    city_weather = request.get(url).json()
    

    # return HttpResponse(city_weather)