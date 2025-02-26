# 1.The most appropriate data structure to represent the studens score is a dict with key:value (name:score) pairs
students_score = {
    'Ivan': 5.00,
    'Alex': 3.50,
    'Maria': 5.50,
    'Georgy':5.00
}

# 2. Create a new data structure from the dict above, storing the information only for students with scores greater than 4.00 . Not sure how to iterate over the dict values to create the new dict.
# In order to get the following dict
# best_students_score = {
#     'Ivan': 5.00,
#     'Maria': 5.50,
#     'Georgy':5.00
# }

# # 3. Print out the names and score from best_students_scores in order to get the following output:
# #Ivan     - 5.00
# Maria    - 5.50
# Georgy   - 5.00
# Iterate over keys and values should be used with dict.items() in order to obtain this output. The keys should be aligned to the left, the values to the right. 

best_students_score = {
    'Ivan' :  5.00,
    'Maria':  5.50,
    'Georgy': 5.00
 }
for name,score in best_students_score.items():
    print(f'{name:<13} {score:>13}')