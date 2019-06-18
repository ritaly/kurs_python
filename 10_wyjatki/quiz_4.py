def get_prize(points):
    result = []
    if points <= 50:
        result.append("Rabbit!")
    elif points <= 150:
        result.append("Oh dear, no prize this time.")
    elif points <= 180:
        result.append("Balloons")
    else:
        result.append("Ping-pong table")

    return result


print(get_prize(176))
