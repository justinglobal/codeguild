
from django.http import HttpResponse

def render_madlib1(request):
    verb = request.GET['verb']
    noun = request.GET['noun']
    name = request.GET['name']
    adj = request.GET['adj']
    lib = ('once upon a ' + noun + '. There was a man called ' + name + '. He was very ' + adj + ', but he could ' + verb + ' all night long')
    return HttpResponse(lib)

def render_madlib2(request):
    verb = request.GET['verb']
    noun = request.GET['noun']
    name = request.GET['name']
    adj = request.GET['adj']
    lib = ('once upon a ' + noun + '. There was a man called ' + name + '. He was very ' + adj + ', but he could ' + verb + ' all night long')
    return HttpResponse(lib)

def render_madlib3(request):
    verb = request.GET['verb']
    noun = request.GET['noun']
    name = request.GET['name']
    adj = request.GET['adj']
    lib = ('one day a ' + noun + ' was found on the street by ' + name + '. It was very ' + adj + ', but he could ' + verb + ' all night long')
    if verb == '' or noun == '' or name == '' or adj == '':
        return HttpResponse(status = 400)
    return HttpResponse(lib)


# def render_plus(request):
#     lhs = int(request.GET['x'])
#     rhs = int(request.GET['y'])
#     total = lhs + rhs
#     return HttpResponse(str(total))
#
#
# def render_minus(request):
#     lhs = int(request.GET['x'])
#     rhs = int(request.GET['y'])
#     diff = lhs - rhs
#     if diff <= 0:
#         return HttpResponse(status=400)
#     return HttpResponse(str(diff))
