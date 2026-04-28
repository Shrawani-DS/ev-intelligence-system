def get_recommendations(prediction, features):
    recs = []

    speed = features.get("Speed", 0)
    current = features.get("MCU_AC_Current", 0)
    motor_temp = features.get("Motor_temp", 0)

    if prediction == "Aggressive":
        recs.append("Reduce acceleration and torque demand")
        recs.append("Avoid high speed driving")
        if current > 200:
            recs.append("High current usage detected - optimize driving style")
        if motor_temp > 60:
            recs.append("Motor temperature high - allow cooling")

    elif prediction == "Eco":
        recs.append("Maintain current driving style")
        recs.append("Optimal energy usage detected")
        if speed < 30:
            recs.append("You can slightly increase speed for better efficiency")

    elif prediction == "Normal":
        recs.append("Maintain moderate speed")
        recs.append("Balanced driving detected")
        if speed > 80:
            recs.append("Reduce speed for better efficiency")
        if current > 150:
            recs.append("Try smoother acceleration")

    return recs