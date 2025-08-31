import asyncio
from nonebot import on_notice
from nonebot.log import logger
from nonebot.adapters.onebot.v11 import Bot, GroupIncreaseNoticeEvent, Message, MessageSegment
from nonebot.exception import ActionFailed

# 创建一个事件响应器，用于处理群成员增加的通知事件
# priority=5 表示事件处理的优先级，数值越小优先级越高
group_increase_handler = on_notice(priority=5)

@group_increase_handler.handle()
async def _(bot: Bot, event: GroupIncreaseNoticeEvent):
    """
    处理新成员入群事件的函数
    当有新用户加入群聊时，此函数将被触发
    """
    # 检查加入群的是否是机器人自身，如果是，则不执行任何操作
    if event.user_id == int(bot.self_id):
        return

    # 欢迎图片在服务器上的本地路径
    # Lagrange.OneBot协议支持通过 file:/// 协议头发送本地图片
    image_url = "file:///./welcome.jpg"
    
    # 构造欢迎消息
    # 1. @新成员
    # 2. 欢迎文字
    # 3. 欢迎图片
    # MessageSegment.at(event.user_id) 用于生成@用户的消息段
    # MessageSegment.text() 用于生成纯文本消息段
    # MessageSegment.image() 用于生成图片消息段
    welcome_message = (
        MessageSegment.at(event.user_id) +
        MessageSegment.text("欢迎新人！") +
        MessageSegment.image(image_url)
    )

    # 为了防止新成员刚入群就被大量消息刷屏，延迟1秒发送欢迎语
    await asyncio.sleep(1)

    try:
        # 记录将要发送的欢迎消息和目标群号
        logger.info(f"向群 {event.group_id} 发送欢迎消息，欢迎新成员 {event.user_id}")
        
        # 调用 aio-libs 的 API 发送消息
        await bot.send_group_msg(
            group_id=event.group_id,
            message=welcome_message
        )
        logger.info(f"成功向群 {event.group_id} 发送欢迎消息")

    except ActionFailed as e:
        # 如果发送失败（例如，机器人被禁言），则记录错误日志
        logger.error(f"向群 {event.group_id} 发送欢迎消息失败: {e}")
    except Exception as e:
        # 捕获其他可能的异常，例如网络问题或文件路径问题
        logger.error(f"发送欢迎消息时发生未知错误: {e}")