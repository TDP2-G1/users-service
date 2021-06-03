from sqlalchemy import desc, func, select
from sqlalchemy.orm import session

from usersServiceApp.infra import create_in_db
from usersServiceApp.model import feedback


def create_feedback(post_data):
    _feedback = feedback(id_user_receiver=post_data['id_user_receiver'], id_user_giver=post_data['id_user_giver'],
                         feedback_description=post_data['feedback_description'])
    create_in_db(_feedback)
    feedback_created = feedback.query.filter_by(feedback_description=_feedback.feedback_description).first()
    return feedback_created


def get_feedback_by_description(description):
    return feedback.query.filter(feedback.feedback_description.ilike(description)).first()


def get_feedback_by_id(id_feedback):
    return feedback.query.filter_by(id_feedback=id_feedback).first()


def get_user_received_feedbacks_ordered(id_user):
    return feedback.query.filter_by(id_user_receiver=id_user).order_by(desc(feedback.date_created)).all()


def get_user_amount_received_feedbacks(id_user):
    return len(feedback.query.filter_by(id_user_receiver=id_user).all())


def get_all_feedbacks():
    return feedback.query.order_by(desc(feedback.date_created)).all()
