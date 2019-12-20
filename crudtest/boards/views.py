from django.shortcuts import render, redirect
from .models import Board

# Create your views here.

def index(request):
    boards = Board.objects.all()
    context = {
        'boards' : boards,
    }
    return render(request, 'index.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET['title']
    content = request.GET['contents']
    creator = request.GET['creator']
    
    new_board = Board.objects.create(title=title, content=content, creator=creator)
    
    return redirect(f'/boards/{new_board.id}')

def show(request, id ):
    board = Board.objects.get(id=id)
    context = {
        'board' : board,
    }
    return render(request, 'show.html', context)

def edit(request, id):
    # 원래 있던 내용이 들어있는 Form
    board = Board.objects.get(id=id)
    context = {
        'board': board
    }
    return render(request, 'edit.html', context)

def update(request, id):
    # 실제로 update가 일어나는 곳
    board = Board.objects.get(id=id)
    title = request.GET['title']
    contents = request.GET['contents']

    board.title = title
    board.content = contents
    board.save()

    context = {
        'board': board
    }
    # render 직접 뿌리기
    # redirect : 다른곳으로 연결
    return redirect(f'/boards/{board.id}')

def delete(request, id):
    board = Board.objects.get(id=id)
    board.delete()
    return redirect(f'/boards')