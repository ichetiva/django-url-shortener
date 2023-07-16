from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from shortener.services import LinkSerivce
from shortener.forms import ShortLinkForm


class CreateShortLinkView(View):
    def get(self, request):
        form = ShortLinkForm()
        return render(request, 'shortener/create_link_form.html', {'form': form})

    def post(self, request):
        form = ShortLinkForm(request.POST)
        if form.is_valid():
            service = LinkSerivce()
            code = service.create_link(form.data['url'])
            service.close()
            return HttpResponse(
                f'Your shorted <a href={service.get_short_url(code)}>link</a>: {service.get_short_url(code)}'
            )
        else:
            return HttpResponse('Non-valid form')


class RedirectShortLinkView(View):
    def get(self, request, code):
        service = LinkSerivce()
        service.register_usage(code)
        url = service.get_url(code)
        service.close()
        return redirect(url)


class GetUsageCountOfShortLinkView(View):
    def get(self, request):
        if not (code := request.GET.get('code', None)):
            return HttpResponse('Field "code" is not found')
        service = LinkSerivce()
        usage_count = service.get_usage_count(code)
        service.close()
        return HttpResponse(
            f'Short <a href="{service.get_short_url(code)}">link</a> '
            f'{service.get_short_url(code)} was used {usage_count} times.'
        )
