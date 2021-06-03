from usersServiceApp.core.register_logic import validate_user_id_exists, get_user_pictures
from usersServiceApp.infra.db_feedback import create_feedback, get_user_received_feedbacks_ordered
from usersServiceApp.infra.db_user import get_user_by_id


def validate_and_create_feedback(post_data):
    validate_user_id_exists(post_data['id_user_receiver'])
    validate_user_id_exists(post_data['id_user_giver'])
    return create_feedback(post_data)


def get_feedbacks_info(id_feedback_receiver):
    feedbacks = get_user_received_feedbacks_ordered(id_feedback_receiver)
    _feedbacks = []
    for feedback in feedbacks:
        _user_giver = get_user_by_id(feedback.id_user_giver)
        _feedbacks.append(format_feedback(feedback, _user_giver))
    return _feedbacks


def format_feedback(feedback, _user_giver):
    pictures = get_user_pictures(_user_giver.id_user)
    _feedback = {
        "id_user_giver": _user_giver.id_user,
        "first_name": _user_giver.first_name,
        "profile_picture": pictures[0].url_picture,
        "feedback_description": feedback.feedback_description,
        "date": feedback.date_created.strftime("%d/%m/%Y")
    }
    return _feedback
