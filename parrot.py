prompt = "\nTell me something and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program"
active = True #active는 플래그 픟래그가 true이면 계속 실행 false로 바꾸는 이벤트가 일어나면 엄춤
while active:
    message = input(prompt)
    if message == 'quit':
        active = false
    else:
        print(message)
