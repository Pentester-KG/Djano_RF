from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from movie_app.models import Movie, Director, Review


@api_view(['GET'])
def director_list_api_view(request):
    data = Director.objects.all()
    list_ = DirectorSerializer(data, many=True).data
    return Response(data=list_)


class DirectorListView(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


@api_view(['GET'])
def director_detail_api_view(request, id):
    director = Director.objects.get(id=id)
    data = DirectorSerializer(director).data
    return Response(data=data)


@api_view(['GET'])
def movie_list_api_view(request):
    data = Movie.objects.all()
    list_ = MovieSerializer(data, many=True).data
    return Response(data=list_)


@api_view(['GET'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'Error': 'Page not found'}, status=404)
    data = MovieSerializer(movie).data
    return Response(data=data)


@api_view(['GET'])
def review_list_api_view(request):
    data = Review.objects.all()
    list_ = ReviewSerializer(data, many=True).data
    return Response(data=list_)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'Error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
    data = ReviewSerializer(review).data
    return Response(data=data)


class MovieReviewListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
# class DirectorListView(generics.ListAPIView):
#     queryset = Director.objects.all()
#     serializer_class = DirectorSerializer
#
#
# class MovieReviewListView(generics.ListAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer


