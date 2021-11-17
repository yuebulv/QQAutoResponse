from botoy import Botoy, GroupMsg, Action, FriendMsg
from botoy.parser import group as gp  # 群消息(GroupMsg)相关解析
from botoy.parser import friend as fp # 好友消息(FriendMsg)相关解析
from botoy.parser import event as ep # 事件(EevntMsg)相关解析
global status
status = True
bot = Botoy(qq=297358842, use_plugins=False)


@bot.on_group_msg
def group(ctx: GroupMsg):
    print('收到群消息，群号为', ctx.FromGroupId)
    global status
    if status == True:
        if ctx.FromGroupId == 28764036 and ctx.FromUserId != 297358842:
            # Action(ctx.CurrentQQ).sendGroupText(ctx.FromGroupId, 'ok2')
            # sendFriendText_tran(ctx.CurrentQQ, 43863156, ctx.Content)
            # 向firend发消息，
            # 注意：同一条消息文字、图片、声音等顺序会跟原文件不同
            pic_data = gp.pic(ctx)
            if pic_data is not None:
                for pic in pic_data.GroupPic:
                    sendFriendText_tran(CurrentQQ=ctx.CurrentQQ, friendId=43863156, content=None, picurl=pic.Url,
                                        voice_url=None)
                sendFriendText_tran(CurrentQQ=ctx.CurrentQQ, friendId=43863156, content=pic_data.Content, picurl=None,
                                    voice_url=None)
            elif ctx.Content is not None:
                sendFriendText_tran(CurrentQQ=ctx.CurrentQQ, friendId=43863156, content=ctx.Content, picurl=None,
                                    voice_url=None)
            if gp.voice(ctx) is not None:
                sendFriendText_tran(CurrentQQ=ctx.CurrentQQ, friendId=43863156, content=None, picurl=None,
                                    voice_url=gp.voice(ctx).Url)
        else:
            None


@bot.on_friend_msg
def friend(ctx: FriendMsg):
    print('收到好友消息，帐号为', ctx.FromUin)
    # 向group发消息，
    # 注意：同一条消息文字、图片、声音等顺序会跟原文件不同
    if ctx.Content == 'test' and ctx.FromUin != 297358842:
        Action(ctx.CurrentQQ).sendFriendText(ctx.FromUin, 'ok')
        sendGroupText_tran(ctx.CurrentQQ, 28764036, ctx.Content)
    else:
        None

    if ctx.Content == 'quit':
        global status
        status = False
    elif ctx.FromUin != 297358842:
        pic_data = fp.pic(ctx)
        if pic_data is not None:
            for pic in pic_data.FriendPic:
                sendGroupText_tran(CurrentQQ=ctx.CurrentQQ, groupId=28764036, content=None, picurl=pic.Url,
                                    voice_url=None)
            sendGroupText_tran(CurrentQQ=ctx.CurrentQQ, groupId=28764036, content=pic_data.Content, picurl=None,
                                voice_url=None)
        elif ctx.Content is not None:
            sendGroupText_tran(CurrentQQ=ctx.CurrentQQ, groupId=28764036, content=ctx.Content, picurl=None,
                                voice_url=None)
        if fp.voice(ctx) is not None:
            sendGroupText_tran(CurrentQQ=ctx.CurrentQQ, groupId=28764036, content=None, picurl=None,
                                voice_url=fp.voice(ctx).VoiceUrl)
        status = True


# 向指定群发指定内容
def sendGroupText_tran(CurrentQQ: int, groupId: int, content, picurl, voice_url):
    # Action(CurrentQQ).sendGroupText(groupId, content)
    if content is not None:
        Action(CurrentQQ).sendGroupText(groupId, content)
    if picurl is not None:
        Action(CurrentQQ).sendGroupPic(groupId, picUrl=picurl)
    if voice_url is not None:
        Action(CurrentQQ).sendGroupVoice(groupId, voiceUrl=voice_url)


# 向指定好友发指定内容
def sendFriendText_tran(CurrentQQ: int, friendId: int, content, picurl, voice_url):
    if content is not None:
        Action(CurrentQQ).sendFriendText(friendId, content)
    if picurl is not None:
        Action(CurrentQQ).sendFriendPic(friendId, picUrl=picurl)
    if voice_url is not None:
        Action(CurrentQQ).sendFriendVoice(friendId, voiceUrl=voice_url)


if __name__ == '__main__':
    bot.run()