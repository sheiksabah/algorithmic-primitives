def activity_selection(activities : list) -> list:
    
    sorted_activities = sorted(activities, key = lambda activity : activity[1])

    result = [sorted_activities[0]]

    for activity in sorted_activities[1:]:
        if activity[0] >= result[-1][1]:
            result.append(activity)
     
    return result
