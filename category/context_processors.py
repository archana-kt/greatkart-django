from .models import Catergory


def menu_links(request):
    links = Catergory.objects.all()
    return dict(links=links)
