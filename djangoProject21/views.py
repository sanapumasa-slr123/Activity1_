from django.shortcuts import render


def tweet(request):
    return render(request, "home.html", {})
def tweet_detail_view(request, id=1):
    return render(request, 'tweet/detail_view.html'. {})

def tweet_list_view(request):
    return render(request, 'tweets/detailed_view.html'. {})
