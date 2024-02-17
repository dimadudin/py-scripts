can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001


def can_create_bits(user_permissions):
    return can_create_guild & user_permissions 


def can_review_bits(user_permissions):
    return can_review_guild & user_permissions 


def can_delete_bits(user_permissions):
    return can_delete_guild & user_permissions 


def can_edit_bits(user_permissions):
    return can_edit_guild & user_permissions 

