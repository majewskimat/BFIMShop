from .basket import Basket

app_name = 'basket'

def basket(request):
    return {'basket': Basket(request)}