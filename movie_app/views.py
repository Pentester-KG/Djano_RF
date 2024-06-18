from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from movie_app.models import Movie, Director, Review


@api_view(['GET', 'POST'])
def director_list_api_view(request):
    if request.method == 'GET':
        data = Director.objects.all()
        list_ = DirectorSerializer(data, many=True).data
        return Response(data=list_)
    elif request.method == "POST":
        name = request.data.get('name')

    director = Director.objects.create(
        name=name,
    )
    return Response(data={'name': name}, status=status.HTTP_201_CREATED)


class DirectorListView(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


@api_view(['GET', 'PUT'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Not found'}, status=404)
    if request.method == 'GET':
        data = DirectorSerializer(director).data
        return Response(data=data)
    elif request.method == 'POST':
        director.name = request.data.get('name')
    director.save()
    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def movie_list_api_view(request):
    if request.method == 'GET':
        data = Movie.objects.all()
        list_ = MovieSerializer(data, many=True).data
        return Response(data=list_)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')

        print(request.data)
        movie = Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
            director_id=director_id

        )

        return Response(data={'movie_id': movie.id, 'title': movie.title,
                              'duration': movie.duration, 'director_id': director_id},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'Error': 'Page not found'}, status=404)
    if request.method == 'GET':
        data = MovieSerializer(movie).data
        return Response(data=data)
    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')

        movie.save()
        return Response(status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        data = Review.objects.all()
        list_ = ReviewSerializer(data, many=True).data
        return Response(data=list_)
    if request.method == 'POST':
        text = request.data.get('text')
        movie_id = request.data.get('movie_id')
        stars = request.data.get('stars')

        review = Review.objects.create(
            text=text,
            movie_id=movie_id,
            stars=stars
        )
        return Response(data={'text': text, 'movie_id': movie_id}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'Error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ReviewSerializer(review).data
        return Response(data=data)
    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.stars = request.data.get('stars')
        review.movie_id = request.data.get('movie_id')
        return Response(status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieReviewListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



