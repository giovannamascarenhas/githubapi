from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import filters
import requests
import json
from rest_framework import status
#from github_core.pagination import CustomPagination
from .models import Github
from .serializers import GithubSerializer

class GithubViewSet(viewsets.ViewSet):
    """
        New users class
    """
    def list(self, request):
        import ipdb; ipdb.set_trace()
        # all_users = {}
        # url = 'https://api.github.com/users'
        # response = requests.get(url)
        # all_users = response.json()
        # your_data = all_users[:10]
        # serializer = GithubSerializer(your_data, many=True).data
        # return Response(serializer)
        # teste = 'teste '

        if request.method == 'GET':
            all_users = {}
            valor_padrao = 10
            url = 'https://api.github.com/users'
            response = requests.get(url)
            all_users = response.json()
            num = self.request.query_params.get('num', None)
            your_data = all_users[:valor_padrao]
            username = self.request.query_params.get('username', None)
            if username is not None:
                username = int(username)
                your_data = all_users[:username]
            serializer = GithubSerializer(data=your_data, many=True)
            serializer.is_valid(raise_exception=True)
            serializer.create(validated_data=serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

            

        elif request.method == 'POST':
            serializer = GithubSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GithubtesteViewSet(viewsets.ViewSet):
    def list(self, request):
        search = request.GET.get('search', None)
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 10))
        if search:
            url = 'https://api.github.com/users/%s' % search
        else:
            url = 'https://api.github.com/users?since={0}&per_page={1}'.format(
                ((page - 1) * limit) + 1, limit)
       
        response = requests.get(url)
        user_list = response.json()

        next_page = page + 1
        previous_page = page - 1 if page > 1 else 0
        scheme = request._request.scheme
        host = request._request.get_host()
        path = request._request.get_full_path().split('?')[0]
        return Response({
            'next': f'{scheme}://{host}{path}?page={next_page}&limit={limit}',
            'previous': f'{scheme}://{host}{path}?page={previous_page}&limit={limit}' if previous_page else None,
            'count': None,
            'limit': limit,
            'results': user_list
        })

class GithubrepositoriosViewSet(viewsets.ViewSet):
        # filter_backends = (filters.SearchFilter,)
        # search_fields = ('username')
    def list(self, request):
        search = request.GET.get('search', None)
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 10))
        limit = 30 if limit > 30 else limit
        search = request.GET.get('search', None)
        if search:
            url = 'https://api.github.com/users/%s/repos' % search
           # https://api.github.com/users/giovannamascarenhas/repos
        else:
            url = 'https://api.github.com/users/repos{0}'.format(((page - 1) * limit) + 1)
        #repos = {}
        url = 'https://api.github.com/users/%s/repos' 
        response = requests.get(url)
        #import ipdb; ipdb.set_trace()
        repos_list = response.json()

        next_page = page + 1
        previous_page = page - 1 if page > 1 else 0
        scheme = request._request.scheme
        host = request._request.get_host()
        path = request._request.get_full_path().split('?')[0]
        return Response({
            'next': f'{scheme}://{host}{path}?page={next_page}&limit={limit}',
            'previous': f'{scheme}://{host}{path}?page={previous_page}&limit={limit}' if previous_page else None,
            'count': None,
            'limit': limit,
            'results': repos_list
        })


