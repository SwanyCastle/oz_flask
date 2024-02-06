from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_restful import Api, Resource, reqparse

items = []

class Item(Resource):
    # 특정 아이템 조회
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'message': 'Item not found'}, 404 # error msg, error code
    
    # 아이템 생성
    def post(self, name):
        for item in items:
            if item['name'] == name:
                return {'message': 'already exists'}, 409 # error msg, error code
        data = request.get_json()
        new_item = {'name': name, 'price': data['price']}
        items.append(new_item)
        return new_item
    
    # 아이템 수정
    def put(self, name):
        data = request.get_json()

        for item in items:
            if item['name'] == name:
                item['price'] = data['price']
                return item

        # 만약, 업데이트 하고자하는 아이템 데이터가 없다면 -> 추가
        new_item = {'name': name, 'price': data['price']}
        items.append(new_item)
        return new_item

    # 아이템 삭제
    def delete(self, name):
        global items

        items = [item for item in items if item['name']!= name]
        return {'message': 'deleted'}, 200