# candidate_dict = dict()
#
# accept_input = True
# while accept_input:
#     print('candidate name? or done.')
#     candidate_name = input()
#
#     if 'done' == candidate_name:
#         break
#     if not(candidate_name in candidate_dict):
#         candidate_dict[candidate_name] = 1
#     else:
#         candidate_dict[candidate_name] += 1
#
# for name in candidate_dict:
#     print('Candidate' , name , ' has ' , candidate_dict[name] , 'votes')

candidate_dict = dict()

accept_input = True

while accept_input:
    print('Enter candidate name to vote or done to end and tally')
    candidate_name = input()
    accept_input = candidate_name != 'done'
#do it this way below
    # if candidate_name == 'done'
        #accept_input = false
    #might need to use == not !=

    if not(candidate_name in candidate_dict):
        candidate_dict[candidate_name] = 1
    else:
        candidate_dict[candidate_name] += 1

candidate_dict.pop('done')

#print(candidate_dict)

for name in candidate_dict:
    print('Candidate' , name , ' has ' , candidate_dict[name] , 'votes')

candidate_dict.items()
# winner =
#
vote_total = candidate_dict.values()
#print(candidate_dict.get(max(candidate_dict.items())))
winner = max(candidate_dict, key=candidate_dict.get)

print('winning candidate is ' , winner , 'with ' , max(vote_total) , 'votes')
