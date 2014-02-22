# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView
from django.shortcuts import render_to_response
from djangoblog.models import Post

def hello(request):
    template = get_template('hello.html')
    html = template.render(Context({'name': "World"}))
    return HttpResponse(html)


class HelloTemplate(TemplateView):
    template_name = 'hello.html'
    
    def get_context_data(self, **kwargs):
        context = super(HelloTemplate, self).get_context_data(**kwargs)
        context['name'] = 'World'
        return context
    
def posts(request):
    return render_to_response('blogmain.html', 
                              {'posts': Post.objects.all() })
    
def posting_individual(response, posting_id=1):
    print 'individual posting: %s selected' %(posting_id)
    return render_to_response('blogposting.html',
                              {'post': Post.objects.get(id=posting_id) })
