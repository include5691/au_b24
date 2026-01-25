from enum import StrEnum

class EntityType(StrEnum):
    LEAD = "lead"
    DEAL = "deal"
    CONTACT = "contact"
    COMPANY = "company"
    PRODUCT = "product"
    ACTIVITY = "activity"