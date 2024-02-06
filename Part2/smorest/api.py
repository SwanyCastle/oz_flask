from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import ItemSchema

# 블루프린트 생성 : 'items'라는 이름으로, URL 접두사는 '/items'
# 1번 째 인자 : 해당 블루 프린트의 이름
# 2번 째 인자 : api 의 주소 명 (items라고 통일 시키거나 / __name__ 으로도 사용)
# url_prefix : 이 블루프린트를 사용하는 모든 API 들은 'items' 로 시작하겠다
# description : 해당 블루프린트에 대한 설명
blp = Blueprint('items', 'items', url_prefix='/items', description='Operations on items')

# 간단한 데이터 저장소 역할을 하는 리스트
items = []

# 'ItemList' 클래스 - GET 및 POST 요청을 처리
@blp.route('/')
class ItemList(MethodView):
    @blp.response(200, description='Success')
    def get(self):
        # 모든 아이템을 반환하는 GET 요청 처리
        return items
    
    # 받은 데이터를 저장할 때 @blp.argument(ItemSchema)를 사용해서 제대로 값이 들어있는지 체크하는것
    @blp.arguments(ItemSchema)
    @blp.response(201, description='Item added successfully')
    def post(self, new_item):
        # 새 아이템을 추가하는 POST 처리
        items.append(new_item)
        return new_item

# 'Item' 클래스 - 특정 아이템을 GET, PUT, DELETE 요청을 처리 
@blp.route('/<int:item_id>')
class Item(MethodView):
    @blp.response(200, 'Success')
    def get(self, item_id):
        # 특정 ID를 가진 아이템을 반환하는 GET 요청 처리
        # next() -> 반복문에서 값이 있으면 값을 반환하고 없으면 None을 반환
        # next는 조건을 만족하는 첫 번째 아이템을 반환하고, 그 이후의 아이템은 무시
        item = next((item for item in items if item['id'] == item_id), None)
        if item is None:
            abort(404, message='Item not found')
        return item
    
    # 받은 데이터를 업데이트할 때 @blp.argument(ItemSchema)를 사용해서 제대로 값이 들어있는지 체크하는것
    @blp.arguments(ItemSchema)
    @blp.response(200, description='Item updated successfully')
    def put(self, item_id, new_item):
        # 특정 ID를 가진 아이템을 수정하는 PUT 요청 처리
        item = next((item for item in items if item['id'] == item_id), None)
        if item is None:
            abort(404, message='Item not found')
        item.update(new_item)
        return item
    
    @blp.response(204, description='Item deleted successfully')
    def delete(self, item_id):
        # 특정 ID를 가진 아이템을 삭제하는 DELETE 요청 처리
        global items
        # any() -> 반복 가능한 자료형을 인자로 받고 그 인자로 받은 요소중 하나라도 True 이면 True, False 이면 False를 반환하는 함수
        if not any(item for item in items if item['id'] == item_id):
            abort(404, message='Item not found')
        items = [item for item in items if item['id']!= item_id]
        return ''
    
# flask-smorest 블루프린트를 사용하게 되면 따로 등록하지 않아도 된다.
# 각 클래스를 블루프린트에 등록 - 이건 flask 에서 제공하는 블루프린트를 사용할 때 등록하는 과정
# blp.register_view(ItemList, 'item_list', '/')
# blp.register_view(Item, 'item', '/<int:item_id>')