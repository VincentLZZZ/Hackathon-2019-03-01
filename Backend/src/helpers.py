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




