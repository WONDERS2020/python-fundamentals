#/usr/bin/python3
""" Write a function that takes a nested dictionary like:"""
def transpose_scores(nested_dict):
    
    result = {}
    for subject, scores in nested_dict.items():
        for student, score in scores.items():
            if student not in result:
                result[student] = {}
            result[student][subject] = score
    return result
data = {
    "Math": {"Ali": 90, "Zara": 88},
    "Science": {"Ali": 80, "Zara": 95}
}
transposed = transpose_scores(data)
print(transposed)
# Output: {'Ali': {'Math': 90, 'Science': 80}, 'Zara': {'Math': 88, 'Science': 95}}
