from django.http import Http404, HttpResponse
from django.shortcuts import render

from apps.post.models import Post, PostComment

from apps.post.forms import PostCommentForm



def post_list_view(request):
    post_qs = Post.objects.all()
    responce = render(request, 'main.html', context={'post_list': post_qs})
    return responce


def post_detail_view(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'post_single.html', {'post': post})


def post_comment_view(request, pk):
    if request.method == 'POST':
        print(request.POST)
        post_request_data = request.POST
        comment_form = PostCommentForm(post_request_data)
        if comment_form.is_valid():
            comment = PostComment.objects.create(
                text=comment_form.data['text'],
                user_name=comment_form.data['name'],
                user_email=comment_form.data['email'],
                article_id=pk)
            return HttpResponse(content='Комментарий успешно добавлен')

        else:
             return HttpResponse(content=f'Вы неправильно заполнили форму: {comment_form.errors}')

