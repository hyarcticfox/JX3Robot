import nonebot
from . import get_over
from . import live_subscription
__plugin_name = 'Bilibili'
import pickle

rcnbot = nonebot.get_bot().config
#将其定义为命令组，用于声明一组有相同名称前缀的命令。
#Bilibili = nonebot.CommandGroup('Bilibili')

@on_command('checkInfo', aliases=('订阅查询'))
async def check(session: CommandSession):
    report = await readSubscriptionInfo(session.ctx['user_id'])
    if report:
        msg = "你订阅的直播有："+ ",".join(report)
    else:
        msg = "你未订阅任何直播"
    await session.finish(msg)




async def readSubscriptionInfo(user=None):
    filename = getDataFolder('Bilibili','subscription.pkl')
    try:
        allInfo = pickle.load(open(filename, 'rb'), encoding='utf-8')
    except:
        # 首次运行读取没数据会报错

        allInfo = []

    if user:
        roomList = []
        for item in allInfo:
            for u in item['userset']:
                if str(user) in u:
                    tmp_list.append(item['room_id'])

        return roomList

