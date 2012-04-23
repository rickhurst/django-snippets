from django.http import HttpResponse
from snippets.models import Snippet
from django.template import Context, loader, RequestContext
from django.conf import settings

common_template_vars = {}

def edit_snippet(request, slug, mode):
    if request.user.has_perm('change_snippet'):
        t = loader.get_template('edit_snippet.html')
        try:
            snippet = Snippet.objects.get(slug=slug)
        except:       
            snippet = False

        updated = False
        
        # if this is a post, get the posted HTML 
        if request.POST:
            snippet.html = request.POST['snippet_html']
            # TODO - validation..
            snippet.save()
            updated = True
            
            if request.is_ajax():
                return HttpResponse('1')
                
            if mode == 'popup':
                return HttpResponse('<script>window.opener.popUpCallBack();</script>')
            
        context = {
            'slug': slug,
            'snippet' : snippet,
            'updated' : updated,
            'mode' : mode
        }
        context.update(common_template_vars)

        c = RequestContext(request, context)
        return HttpResponse(t.render(c))
    else:
        return HttpResponse('user not authenticated, or does not have permission to edit the snippet');

