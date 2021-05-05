import json

VALID_REGISTER = json.dumps(
    {'fb_user_id': "u23y48298", 'first_name': 'Steven', 'last_name': 'Seagal', 'email': 'steven@seagal.com', 'genre': 1,
     'native_language': 1, 'practice_language': 1, 'actual_level': 1, 'birth_date': '10/04/1952',
     'topics_descriptions': 'Kung Fu and Killing Bad Guys',
     'profile_picture': "https://images.mubicdn.net/images/cast_member/28365/cache-3386-1478101707/image-w856.jpg?size=400x"})


INVALID_MINOR_REGISTER = json.dumps(
    {'fb_user_id': "u23y48218", 'first_name': 'Little', 'last_name': 'Kid', 'email': 'little@kid.com', 'genre': 1,
     'native_language': 1, 'practice_language': 1, 'actual_level': 1, 'birth_date': '10/04/2006',
     'topics_descriptions': 'Child topics'})


INVALID_REGISTER_DATE_FORMAT = json.dumps(
    {'fb_user_id': "u23y48298", 'first_name': 'Steven', 'last_name': 'Seagal', 'email': 'steven@seagal.com', 'genre': 1,
     'native_language': 1, 'practice_language': 1, 'actual_level': 1, 'birth_date': '10/04/52',
     'topics_descriptions': 'Kung Fu and Killing Bad Guys',
     'profile_picture': "https://images.mubicdn.net/images/cast_member/28365/cache-3386-1478101707/image-w856.jpg?size=400x"})
