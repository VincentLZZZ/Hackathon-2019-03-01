def gcloud_to_food(post_body):
    """Convert the gcloud json result to a specific type of food

    """
    with open('./test/classes.txt', 'r') as f:
        foods = f.read().splitlines()
    possible_food = []
    for item in post_body.get("labelAnnotations"):
        possible_food.append(item["description"])
    for food in possible_food:
        if food.lower() in map(lambda x:x.lower(),foods):
            return food


def calc_emission_driver(mdf, division, carline, g_to_m, d):
    return mdf[division][carline][g_to_m] / d * 9.072 / 1000


def calc_emission(persona):
    if persona == "driver":
        return 120
    if persona == "Farmers/Producers":
        return 80
    if persona == "Storage companies":
        return 50
    if persona == "Food processor":
        return 50
    if persona == "Trader/Distributor":
        return 60






