filename = 'high_score.txt'
# with open(filename, 'a') as file_object:
#     file_object.truncate()

f=open(filename, "r+")
f.truncate()