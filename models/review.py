#!/usr/bin/python3
"""Define the review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review

    Attributes:
        place_id (str): place id
        user_id (str): user id
        text (str): review text
    """
    place_id: str = ""
    user_id: str = ""
    text: str = ""
