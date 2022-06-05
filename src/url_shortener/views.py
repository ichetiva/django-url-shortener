from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from .models import Link
from .services import _generate_code, _validate_url
from .forms import ShortLinkForm


class CreateShortLinkView(View):
    def get(self, request, *args, **kwargs):
        form = ShortLinkForm()
        return render(request, 'url_shortener/create_link_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ShortLinkForm(request.POST)
        if form.is_valid():
            db_link = Link(
                base_url=_validate_url(form.data['url']),
                code=_generate_code()
            )
            db_link.save()
            return HttpResponse(f'Your shorted <a href={db_link.short_url}>link</a>: {db_link.short_url}')
        else:
            return HttpResponse('Not valid form.')


class RedirectShortLinkView(View):
    def get(self, request, *args, **kwargs):
        db_link = Link.objects.get(code=kwargs['code'])
        db_link.usage_count += 1
        db_link.save()
        return redirect(db_link.base_url)


class GetUsageCountOfShortLinkView(View):
    def get(self, request, *args, **kwargs):
        code = request.GET.get('code', default=None)
        if not code:
            return HttpResponse('Field "code" is not found.')
        db_link = Link.objects.get(code=code)
        return HttpResponse(f'Short <a href="{db_link.short_url}">link</a> {db_link.short_url} was used {db_link.usage_count} times.')
