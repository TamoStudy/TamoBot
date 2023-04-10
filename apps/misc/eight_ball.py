import random

class EightBall:
    @staticmethod
    def get_response():
        response_num = random.randint(1, 20)
        
        if response_num == 1:
            response = "It is certain."
        elif response_num == 2:
            response = "It is decidedly so."
        elif response_num == 3:
            response = "Without a doubt."
        elif response_num == 4:
            response = "Yes - definitely."
        elif response_num == 5:
            response = "You may rely on it."
        elif response_num == 6:
            response = "As I see it, yes."
        elif response_num == 7:
            response = "Most likely."
        elif response_num == 8:
            response = "Outlook good."
        elif response_num == 9:
            response = "Yes."
        elif response_num == 10:
            response = "Signs point to yes."
        elif response_num == 11:
            response = "Reply hazy, try again."
        elif response_num == 12:
            response = "Ask again later."
        elif response_num == 13:
            response = "Better not tell you now."
        elif response_num == 14:
            response = "Cannot predict now."
        elif response_num == 15:
            response = "Concentrate and ask again."
        elif response_num == 16:
            response = "Don't count on it."
        elif response_num == 17:
            response = "Outlook not so good."
        elif response_num == 18:
            response = "My sources say no."
        elif response_num == 19:
            response = "Very doubtful."
        else:
            response = "My reply is no."

        return response