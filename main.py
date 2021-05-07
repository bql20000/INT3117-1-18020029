MAX_WEIGHT = 50
MAX_DISTANCE = 30
BULKY_ITEM_LIMIT = 10
BULKY_ITEM_SURCHARGE = 10000
INIT_COST = 15000
NEAR_DISTANCE_LIMIT = 5
NEAR_DISTANCE_COST = 7000
FAR_DISTANCE_COST = 10000


def calculate_ship_cost(weight, distance):
    if weight < 0 or weight > MAX_WEIGHT or distance < 0 or distance > MAX_DISTANCE:
        return -1

    cost = INIT_COST
    if weight > BULKY_ITEM_LIMIT:
        cost += BULKY_ITEM_SURCHARGE

    cost += min(NEAR_DISTANCE_LIMIT, distance) * NEAR_DISTANCE_COST
    cost += max(distance - NEAR_DISTANCE_LIMIT, 0) * FAR_DISTANCE_COST
    return cost

