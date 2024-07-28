cot_prompt = '''{input}'''

standard_prompt = '''{input}'''

vote_prompt = '''You are guiding a robot to its target location given a natural language insturction. Given an instruction and several choices, decide which choice is most promising. Analyze each choice in detail, then conclude in the last line "The best choice is {s}", where s the integer id of the choice.
'''

compare_prompt = '''Briefly analyze the practicality of the following two plans of action. Conclude in the last line "The more practical approach is 1", "The more practical approach is 2", or "The two approaches are similarly practical".
'''

score_prompt = '''Analyze the following plan of action, then at the last line conclude "Thus the practicality score is {s}", where s is an integer from 1 to 10.
'''