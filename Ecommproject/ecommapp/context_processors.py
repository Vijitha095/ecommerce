from ecommapp.models import Cart

def count_context(request):
    if request.user.is_authenticated:
        count=Cart.objects.filter(user_id=request.user).exclude(status='order-placed').count()
        return {'count':count}
    else:
        return {'count':0}