def get_grade(s1, s2, s3):
    # Code here
    avg_score = (s1 + s2 + s3) / 3

    # if avg_score <= 100 and avg_score >= 90:
    #     return "A"
    # elif avg_score < 90 and avg_score >= 80:
    #     return "B"
    # elif avg_score < 80 and avg_score >= 70:
    #     return "C"
    # elif avg_score < 70 and avg_score >= 60:
    #     return "D"
    # else:
    #     return "F"
    #
    if avg_score >= 90:
        return "A"
    elif avg_score >= 80:
        return "B"
    elif avg_score >= 70:
        return "C"
    elif avg_score >= 60:
        return "D"
    else:
        return "F"

print(get_grade(70, 70, 70))