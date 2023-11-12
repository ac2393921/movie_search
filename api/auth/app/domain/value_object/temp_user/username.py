from pydantic import constr

from app.domain.value_object.value_object import ValueObject


class UserName(ValueObject):
    value: constr(min_length=1, max_length=50)  # usernameは少なくとも1文字以上50文字以下
