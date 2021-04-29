import json

INVALID_REGISTER = json.dumps(
    {'first_name': 'Steven', 'last_name': 'Seagal', 'email': 'steven@seagal.com', 'genre': 0,
     'native_language': 0, 'practice_language': 0, 'actual_level': 0,
     'topics_descriptions': 'Kung Fu and Killing Bad Guys'})

VALID_REGISTER = json.dumps(
    {'first_name': 'Steven', 'last_name': 'Seagal', 'email': 'steven@seagal.com', 'genre': 1,
     'native_language': 1, 'practice_language': 1, 'actual_level': 1,
     'topics_descriptions': 'Kung Fu and Killing Bad Guys'})
