
class Bot:
    async def on_message(self, context):
        if context.activity.type == "message" and context.activity.text:
            send_info = "Did you say: '{}'".format(context.activity.text)
            await context.send_activity(send_info)
