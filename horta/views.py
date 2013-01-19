from django.http import HttpResponse

def home(request):
    # using a basic view, as shown in escalant3's django-ember-example
    # repository on github, in order to bypass any possible django and
    # handlebars conflicts... to be revised
    template_file = open('horta/templates/index.html')
    html_content = template_file.read()
    template_file.close()
    return HttpResponse(html_content)
