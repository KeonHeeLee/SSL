openMSG = "안녕하세요!"
leaveMSG = "나중에 뵈요~ :)"

def openEvent():
    # Get open_event_message
    return openMSG


def leaveEvent():
    # Get leave_event_message
    return leaveMSG


def sendEvent(message):
    if message == "안녕하세요":
        return "안녕하세요!"
    elif message == "밥 줘":
        return "싫은데"
    elif message == "날씨 어때?":
        return "더워 그냥"
    elif message == "오반아 휘파람을 불어라! 오반아!":
        return "삐 삐삐삐 삐삐삐삐"
    elif message == "예비군 언제가지?":
        return "6월 30일에 갑니다!"

    else:
        return "뭐라하는지 모르겠어"

def setData(user, sendMSG):
    postBodyMessage = {
        "event": "send",
        "user": user,
        "textContent": {
            "text": sendMSG
        }
    }
    return postBodyMessage

def get_handler(data):
    sendMSG = "None"
    user = data["user"]

    if data["event"] == "open":
        sendMSG = openEvent()

    elif data["event"] == "leave":
        sendMSG = leaveEvent()

    elif data["event"] == "send":
        message = data["textContent"]["text"]
        if data["textContent"]["inputType"] == "typing":
            sendMSG = sendEvent(message=message)
        else:
            sendMSG = "현재 지원하지 않는 타입의 메세지예요 ㅠㅠ"

    return setData(user=user, sendMSG=sendMSG)
