import datetime
import json
from flask import request, redirect, url_for
from vk_api import Captcha

from app import app
from app import db
from .vk_worker import VkWorker
from .models import SearchRecord


@app.route('/searchsaverecord', methods=['POST'])
def record_groups():
    """Function for search group and friends groups name on substring
    params:
            word: search word for group name
            phone: user phone
            pass: user pass
    """
    data = request.get_json()
    try:
        search_word = data.pop('word')
        user = data
    except KeyError:
        return 'Search word or phone and password is empty', 400
    try:
        worker = VkWorker(user['phone'], user['password'])
        groups = worker.get_user_groups()
    except Captcha:
        return redirect(url_for('captcha_handle', password=user['password'], phone=user['phone'], ))
    response = {}
    for group_id, group_name in groups.items():
        if search_word.lower() in group_name.lower():
            response[group_id] = group_name
            record = SearchRecord(owner=user['phone'], group_name=group_name, query_datetime=datetime.datetime.now(),
                                  search_word=search_word)
            db.session.add(record)
            db.session.commit()
    if len(response) == 0:
        return 'Not found', 404
    response = json.dumps(response, ensure_ascii=False)
    return response


@app.route('/getallrecords', methods=['GET'])
def get_all_records():
    """Function for get all group name in db

        """
    records = SearchRecord.query.all()
    response = [record.group_name for record in records]
    if len(response) == 0:
        return 'Not found', 404
    return response


@app.route('/searchrecord', methods=['POST'])
async def search_groups():
    """Function for search group name with substring without friends group
    and save it to db
        params:
                word: search word for group name
                phone: user phone
                pass: user pass
        """
    data = request.get_json()
    try:
        search_word = data.pop('word')
        user = data
    except KeyError:
        return 'Search word or phone and password is empty', 400
    try:
        worker = VkWorker(user['phone'], user['password'])
    except Captcha:
        return redirect(url_for('captcha_handle', password=user['password'], phone=user['phone'], ))
    groups = await worker.get_user_friends_groups()
    response = {}
    for group_id, group_name in groups.items():
        if search_word.lower() in group_name.lower():
            response[group_id] = group_name
    if len(response) == 0:
        return 'Not found', 404
    response = json.dumps(response, ensure_ascii=False)
    return response


@app.route('/captcha', methods=['GET', 'POST'])
def captcha_handle():
    """Function for captcha problem.
    Get params: phone, password
    Return captcha sid and captcha url
    then user should get captcha code and make
    POST request

    POST body:
    phone
    password
    sid
    key
    Return success response
    """
    if request.method == 'GET':
        phone = request.args['phone']
        password = request.args['password']
        handler = VkWorker.captcha_handle(phone, password)
        response = handler
        return response
    if request.method == 'POST':
        data = request.get_json()
        solver = VkWorker.captcha_solver(data)
        response = solver
        return response
