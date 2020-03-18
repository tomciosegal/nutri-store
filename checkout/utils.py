from checkout.models import OrderHistory, OrderItemHistory


def create_order_history(user, session):
    order = OrderHistory.objects.create(
        user=user,
        total_cost=session.get('total', 0)
    )

    cart = session.get('cart')
    for product_id, quantity in cart.items():
        OrderItemHistory.objects.create(
            order_history=order, 
            product_id=product_id,
            quantity=quantity
        )
