from django import template

register = template.Library()

# Make snippets available
from snippets.models import Snippet

# this was adapted from http://docs.djangoproject.com/en/dev/howto/custom-template-tags/


def do_get_snippet(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, slug = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
    if not (slug[0] == slug[-1] and slug[0] in ('"', "'")):
        raise template.TemplateSyntaxError("%r tag's argument should be in quotes" % tag_name)
    return SnippetNode(slug[1:-1])


class SnippetNode(template.Node):
    def __init__(self, slug):
        self.slug = slug
        
    def render(self, context):
        
        user_obj = template.resolve_variable('user', context)
        snippet = False
        try:
            snippet = Snippet.objects.get(slug=self.slug)
        except:
            
            # snippet does not exist, so create it, if the user has permission
            if user_obj.has_perm('add_snippet'):
                #TODO validate slug format
                snippet = Snippet(slug=self.slug, html='(new snippet: ' + self.slug + ')')
                snippet.save()
        if snippet:
            if user_obj.has_perm('change_snippet'):
                return '<span class="snippet" data-slug="' + self.slug + '"><a href="/admin/snippets/snippet/' + str(snippet.id) + '">edit</a>' + snippet.html + '</span>'
            else:
                return snippet.html
        else:
            return ''



register.tag('get_snippet', do_get_snippet)

# # TODO create method to append an array of named snippets to common_template vars
# def get_snippet(slug):
#     snippet = Snippet.objects.get(slug=slug)
#     return snippet