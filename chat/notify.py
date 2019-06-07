from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


async def push_data():
    channel_layer = get_channel_layer()
    await channel_layer.group_send('lobby', {
        # This "type" defines which handler on the Consumer gets
        # called.
        'type': 'chat_message',
        'message': {},
    })
