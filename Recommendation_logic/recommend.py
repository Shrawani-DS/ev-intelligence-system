def generate_recommendation(input_data):

    recs = []

    if input_data["Torque_Load"] > 0.6:
        recs.append("Reduce torque load for better efficiency")

    if input_data["MCU_Current_DC"] > 200:
        recs.append("High current usage detected - drive smoothly")

    if input_data["Speed"] > 80:
        recs.append("Maintain moderate speed for optimal efficiency")

    if len(recs) == 0:
        recs.append("Driving behavior is optimal")

    return recs