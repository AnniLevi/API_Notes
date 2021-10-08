from rest_framework.decorators import api_view
from notes.models import Note
from api.serializers import NoteSerializer, ThinNoteSerializer
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (ListModelMixin, CreateModelMixin, RetrieveModelMixin,
                                   UpdateModelMixin, DestroyModelMixin)
from rest_framework.viewsets import ModelViewSet


# viewsets
class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    # http_method_names = ('get', 'post')

    def list(self, request, *args, **kwargs):  # не обязательно
        notes = Note.objects.all()
        context = {'request': request}
        serializer = ThinNoteSerializer(notes, many=True, context=context)
        return Response(serializer.data)


# generics
class NoteListGView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def list(self, request, *args, **kwags):  # не обязательно
        notes = Note.objects.all()
        context = {'request': request}
        serializer = ThinNoteSerializer(notes, many=True, context=context)
        return Response(serializer.data)


class NoteDetailGView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


# mixins
class NoteListMView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get(self, request, *args, **kwargs):
        self.serializer_class = ThinNoteSerializer
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class NoteDetailMView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get(self, request, *args, **kwags):
        return self.retrieve(request, *args, **kwags)

    def put(self, request, *args, **kwags):
        return self.update(request, *args, **kwags)

    def delete(self, request, *args, **kwags):
        return self.destroy(request, *args, **kwags)


# APIView
class NoteListView(APIView):
    def get(self, request, format=None):
        notes = Note.objects.all()
        context = {'request': request}
        serializer = ThinNoteSerializer(notes, many=True, context=context)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = NoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class NoteDetailView(APIView):
    def get(self, request, pk, format=None):
        note = get_object_or_404(Note, pk=pk)
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        note = get_object_or_404(Note, pk=pk)
        serializer = NoteSerializer(note, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk, format=None):
        note = get_object_or_404(Note, pk=pk)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# functions
@api_view(['GET', 'POST'])
def notes_list(request, format=None):
    if request.method == 'GET':
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def notes_detail(request, pk, format=None):
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = NoteSerializer(note)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = NoteSerializer(note, data=request.data)
        serializer.is_valid(raise_exception=True)
        # аналогично
        # if not serializer.is_valid():
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
