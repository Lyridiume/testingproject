from decimal import Decimal

from core.models import Dish


class Basket():

    def __init__(self,request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add_dish(self,dish,dish_qty):
        dish_id = str(dish.id)

        if dish_id in self.basket:
            self.basket[dish_id]['qty'] = dish_qty
        else:
            self.basket[dish_id] = {'price': str(dish.price), 'qty': int(dish_qty)}

        self.session.modified = True

    def __iter__(self):
        dish_ids = self.basket.keys()
        dishes = Dish.dishes.filter(id__in=dish_ids)
        basket = self.basket.copy()

        for dish in dishes:
            basket[str(dish.id)]['dish'] = dish

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['qty'] * item['price']
            yield item

    def __len__(self):
        return sum(item['qty'] for item in self.basket.values())

    def delete(self,dish):
        dish_id = str(dish)

        if dish_id in self.basket:
            del self.basket[dish_id]
            print(dish_id)

        self.session.modified = True

    def update(self,dish,qty):
        dish_id = str(dish)
        qty = qty

        if dish_id in self.basket:
            self.basket[dish_id]['qty'] = qty

        self.session.modified = True

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())

