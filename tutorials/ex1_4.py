# obtain the user input of seconds
user_input_seconds = int(input())
# calculations
hour = user_input_seconds // 60 // 60
minutes = (user_input_seconds - hour*60*60)//60
seconds = user_input_seconds - hour*60*60 - minutes*60
# output
print(f'{hour} : {minutes} : {seconds}')