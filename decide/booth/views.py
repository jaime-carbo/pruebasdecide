import json
from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404

from base import mods


# TODO: check permissions and census
class BoothView(TemplateView):
    template_name = 'booth/booth.html'

    def get_context_data(self, **kwargs):
        print("BoothView: Entering get_context_data")
        context = super().get_context_data(**kwargs)
        vid = kwargs.get('pk', 0)
        print("BoothView: Voting ID =", vid)

        try:
            r = mods.get('voting', params={'id': vid})
            # Casting numbers to string to manage in javascript with BigInt
            # and avoid problems with js and big number conversion
            print("BoothView: Voting data =", r)
            for k, v in r[0]['pub_key'].items():
                r[0]['pub_key'][k] = str(v)

            context['voting'] = json.dumps(r[0])
        except:
            raise Http404

        context['KEYBITS'] = settings.KEYBITS

        return context
