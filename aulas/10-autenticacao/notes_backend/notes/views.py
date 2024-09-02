from django.http import Http404
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer


@api_view(['GET', 'POST'])
def api_note_list(request):

    if request.method == "POST":
        new_note_data = request.data
        title = new_note_data['title']
        content = new_note_data['content']
        note = Note(title=title, content=content)
        note.save()

    notes = Note.objects.all()

    serialized_note = NoteSerializer(notes, many=True)
    return Response(serialized_note.data)


@api_view(['GET', 'POST', 'DELETE'])
def api_note(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        raise Http404()

    if request.method == 'POST':
        new_note_data = request.data
        note.title = new_note_data['title']
        note.content = new_note_data['content']
        note.save()

    if request.method == 'DELETE':
        note.delete()
        return Response(status=204)

    serialized_note = NoteSerializer(note)
    return Response(serialized_note.data)
