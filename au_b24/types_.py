from enum import StrEnum

class EntityType(StrEnum):
    LEAD = "lead"
    DEAL = "deal"
    CONTACT = "contact"
    PRODUCT = "product"
    ACTIVITY = "activity"