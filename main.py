# This is a sample Python script.
from flask import Flask, request
import okta_jwt_verifier
from user import AngioUser
from flask_cors import CORS

APP = Flask('test_api')
cors = CORS(APP, resources={r"/api/*": {"origins": "*"}})
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

AUAngioUser = AngioUser


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#     user = getattr(AngioUser, 'angio_user_name')
#     print('User: ', user)


@APP.route('/api/user', methods=['POST', 'PUT'])
def add_user():
    req_json = get_req_json()
    print(req_json)


@APP.route('/', methods=['GET'])
def home():
    return 'Success', 200


def get_req_json():
    return request.json()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')
    APP.run(host='0.0.0.0', port=5000, threaded=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
