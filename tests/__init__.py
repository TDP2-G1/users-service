import json

from sqlalchemy import true

VALID_REGISTER = json.dumps(
    {'fb_user_id': "u23y48298", 'first_name': 'Steven', 'last_name': 'Seagal', 'email': 'steven@seagal.com', 'genre': 1,
     'native_language': 1, 'practice_language': 1, 'actual_level': 1, 'birth_date': '10/04/1952',
     'topics_descriptions': 'Kung Fu and Killing Bad Guys',
     'profile_picture': "https://images.mubicdn.net/images/cast_member/28365/cache-3386-1478101707/image-w856.jpg?size=400x"})

ANOTHER_VALID_REGISTER = json.dumps(
    {'fb_user_id': "548975739", 'first_name': 'Jean Claude', 'last_name': 'Van Damme', 'email': 'jc@vd.com', 'genre': 1,
     'native_language': 1, 'practice_language': 1, 'actual_level': 1, 'birth_date': '10/04/1952',
     'topics_descriptions': 'Kung Fu Tournaments',
     'profile_picture': "https://cdn.hobbyconsolas.com/sites/navi.axelspringer.es/public/styles/1200/public/media/image/2020/10/jean-claude-van-damme-2104337.jpg?itok=Ijy1-cuj"})

INVALID_MINOR_REGISTER = json.dumps(
    {'fb_user_id': "u23y48218", 'first_name': 'Little', 'last_name': 'Kid', 'email': 'little@kid.com', 'genre': 1,
     'native_language': 1, 'practice_language': 1, 'actual_level': 1, 'birth_date': '10/04/2006',
     'topics_descriptions': 'Child topics'})

INVALID_REGISTER_DATE_FORMAT = json.dumps(
    {'fb_user_id': "u23y48298", 'first_name': 'Steven', 'last_name': 'Seagal', 'email': 'steven@seagal.com', 'genre': 1,
     'native_language': 1, 'practice_language': 1, 'actual_level': 1, 'birth_date': '10/04/52',
     'topics_descriptions': 'Kung Fu and Killing Bad Guys',
     'profile_picture': "https://images.mubicdn.net/images/cast_member/28365/cache-3386-1478101707/image-w856.jpg?size=400x"})

VALID_FEEDBACK = json.dumps(
    {
        "feedback_description": "I hate you man!",
        "id_user_giver": 2,
        "id_user_receiver": 1
    })

VALID_FOLLOWER = json.dumps(
    {
        "id_user_1": 2,
        "id_user_2": 1
    })

VALID_REPORT = json.dumps(
    {
        "id_report_type": 1,
        "id_user_reported": 1,
        "id_user_reported_by": 2
    })

VALID_OTHER_REPORT = json.dumps(
    {
        "id_report_type": 1,
        "id_user_reported": 1,
        "id_user_reported_by": 2,
        "other_text": "Cosas feas"
    })


VALID_UPDATE_REPORT_FALSE = json.dumps(
    {
        "is_pending": False
    })

VALID_UPDATE_REPORT_TRUE = json.dumps(
    {
        "is_pending": True
    })

VALID_DISABLED_ACCOUNT = json.dumps(
    {
        "is_disabled": True
    });

VALID_BLOCK = json.dumps(
    {
        "id_user_blocker": 2,
        "id_user_blocked": 1,
        "status_enabled": True
    })

VALID_UNBLOCK = json.dumps(
    {
        "id_user_blocker": 2,
        "id_user_blocked": 1,
        "status_enabled": False
    })

VALID_ADMIN_REGISTER = json.dumps(
    {'first_name': 'Steven', 'last_name': 'Seagal', 'email': 'steven@seagal.com', 'password': 'HateJCVannDamme'
     })

INVALID_ADMIN_REGISTER = json.dumps(
    {'first_name': 'Steven', 'last_name': '', 'email': 'steven@seagal.com', 'password': 'HateJCVannDamme'
     })

VALID_ADMIN_LOGIN = json.dumps(
    {'email': 'steven@seagal.com', 'password': 'HateJCVannDamme'})

INVALID_ADMIN_LOGIN = json.dumps(
    {'email': 'steven@seagal.com', 'password': 'LoveJCVannDamme'})

INVALID_USER_STATUS_1 = json.dumps(
    {'id_user': 1, 'user_status': ''})

INVALID_USER_STATUS_2 = json.dumps(
    {'id_user': 1})

VALID_USER_STATUS_1 = json.dumps(
    {'id_user': 1, 'user_status': 'Busy'})

VALID_USER_STATUS_2 = json.dumps(
    {'id_user': 1, 'user_status': 'offline'})

VALID_USER_STATUS_3 = json.dumps(
    {'id_user': 1, 'user_status': 'oNlinE'})

VALID_LOGIN_1 = json.dumps(
    {'id_user': 1})

VALID_LOGIN_2 = json.dumps(
    {'id_user': 2})
