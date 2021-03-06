from app import line_bot_api
from linebot.models import RichMenu, RichMenuSize, RichMenuArea, RichMenuBounds, MessageAction,PostbackAction, URIAction
from linebot.models import TextSendMessage
import os

from app.custom_models import CallDatabase


RichMenu_main = RichMenu(size=RichMenuSize(width=2500, height=1686),
          selected=False,
          name="Main_Tab",
          chat_bar_text="探索iLine",
          areas=[RichMenuArea(bounds=RichMenuBounds(x=17, y=16, width=800, height=811),
                              #action=MessageAction(label='message', text='綁定個人化服務')),
                              action=URIAction(label='personal', uri='https://linebc.feib.com.tw/LineBC/memberBind?linkToken=poWOhjzutOduYv4uchBFyt7bESEDNrj5')),
                 RichMenuArea(bounds=RichMenuBounds(x=851, y=16, width=800, height=811),
                              #action=MessageAction(label='support', text='抗疫我挺你')),
                              action=MessageAction(label='support', text='理專配對')),
                 RichMenuArea(bounds=RichMenuBounds(x=1684, y=16, width=800, height=811),
                              action=MessageAction(label='new', text='小遠贏了')),
                 RichMenuArea(bounds=RichMenuBounds(x=17, y=859, width=800, height=811),
                              action=MessageAction(label='news', text='最新活動')),
                 RichMenuArea(bounds=RichMenuBounds(x=851, y=859, width=800, height=811),
                              #action=MessageAction(label='more', text='更多服務')),
                              action=URIAction(label='vouchers', uri='https://ecard.feib.com.tw/Activity/TCMP/index.do')),
                 RichMenuArea(bounds=RichMenuBounds(x=1684, y=859, width=800, height=811),
                              action=URIAction(label='robot', uri='https://robot.feib.com.tw/Webhook/'))])
'''
#PostbackAction
RichMenu_main = RichMenu(size=RichMenuSize(width=2500, height=1686),
          selected=False,
          name="Main_Tab",
          chat_bar_text="iLine",
          areas=[RichMenuArea(bounds=RichMenuBounds(x=17, y=16, width=800, height=811),
                              action=PostbackAction(label='personal', display_text='綁定個人化服務', data='RichMenu:Main_Tab')),
                 RichMenuArea(bounds=RichMenuBounds(x=851, y=16, width=800, height=811),
                              action=PostbackAction(label='support', display_text='抗疫我挺你', data='RichMenu:Main_Tab')),
                 RichMenuArea(bounds=RichMenuBounds(x=1684, y=16, width=800, height=811),
                              action=PostbackAction(label='new', display_text='小遠贏了', data='RichMenu:Main_Tab')),
                 RichMenuArea(bounds=RichMenuBounds(x=17, y=859, width=800, height=811),
                              action=PostbackAction(label='news', display_text='最新活動', data='RichMenu:Main_Tab')),
                 RichMenuArea(bounds=RichMenuBounds(x=851, y=859, width=800, height=811),
                              action=PostbackAction(label='more', display_text='更多服務', data='RichMenu:Main_Tab')),
                 RichMenuArea(bounds=RichMenuBounds(x=1684, y=859, width=800, height=811),
                              action=URIAction(label='robot', uri='https://robot.feib.com.tw/Webhook/'))])

'''
'''
RichMenu_main = RichMenu(size=RichMenuSize(width=2500, height=1686),
          selected=False,
          name="Main_Tab",
          chat_bar_text="Main Settings",
          areas=[RichMenuArea(bounds=RichMenuBounds(x=17, y=16, width=800, height=811),
                              action=PostbackAction(
                                  label='EngineSetting', 
                                  display_text='Search Engine Setting', 
                                  data='RichMenu:Engine_Tab')),
                 RichMenuArea(bounds=RichMenuBounds(x=850, y=16, width=800, height=811),
                              action=PostbackAction(
                                  label='MethodSetting', 
                                  display_text='Image Method Setting', 
                                  data='RichMenu:Method_Tab')),
                 RichMenuArea(bounds=RichMenuBounds(x=1683, y=16, width=800, height=811),
                              action=URIAction(label='ReadInfo', uri='https://i-line.herokuapp.com'))])
'''

RichMenu_engine = RichMenu(size=RichMenuSize(width=2500, height=1686),
          selected=False,
          name="Engine_Tab",
          chat_bar_text="Set Engine",
          areas=[RichMenuArea(bounds=RichMenuBounds(x=17, y=16, width=800, height=811),
                              action=PostbackAction(label='Google', display_text='Engine: Google', data='RichMenu:Engine_Tab:Google')),
                 RichMenuArea(bounds=RichMenuBounds(x=850, y=16, width=800, height=811),
                              action=PostbackAction(label='iStock', display_text='Engine: iStock', data='RichMenu:Engine_Tab:iStock')),
                 RichMenuArea(bounds=RichMenuBounds(x=1683, y=16, width=800, height=811),
                              action=PostbackAction(label='BackMain', display_text='Back to Main', data='RichMenu:Main_Tab'))])

RichMenu_method = RichMenu(size=RichMenuSize(width=2500, height=1686),
          selected=False,
          name="Method_Tab",
          chat_bar_text="Set Method",
          areas=[RichMenuArea(bounds=RichMenuBounds(x=17, y=16, width=800, height=811),
                              action=PostbackAction(label='Image', display_text='Method: Image', data='RichMenu:Method_Tab:Image')),
                 RichMenuArea(bounds=RichMenuBounds(x=850, y=16, width=800, height=811),
                              action=PostbackAction(
                                  label='Carousel', 
                                  display_text='Method: Carousel', 
                                  data='RichMenu:Method_tab:Carousel')),
                 RichMenuArea(bounds=RichMenuBounds(x=1683, y=16, width=800, height=811),
                              action=PostbackAction(label='BackMain', display_text='Back to Main', data='RichMenu:Main_Tab'))])

target_dir = 'app/static/imgRichMenu/'
static_rich_menu_list = [(RichMenu_engine, f'{target_dir}m5.jpg'), 
                         (RichMenu_method, f'{target_dir}m5.jpg'),
                         (RichMenu_main, f'{target_dir}m5.jpg')]

'''
static_rich_menu_list = [(RichMenu_engine, f'{target_dir}RichMenuENGINE.png'), 
                         (RichMenu_method, f'{target_dir}RichMenuMETHOD.png'),
                         (RichMenu_main, f'{target_dir}RichMenuMAIN.png')]
'''
def rich_menu_i(event):
    # event.postback.data is in the category of 'RM:R'
    target_tab = event.postback.data.split(':')[1]
    rich_menu_list = line_bot_api.get_rich_menu_list()
    print('target_tab', target_tab)
    target_rich_menu_id = [i.rich_menu_id for i in rich_menu_list if i.name == target_tab][0]
    print('target_rich_menu_id', target_rich_menu_id)
    target_user_id = event.source.user_id
    print('target_user_id', target_user_id)
    line_bot_api.link_rich_menu_to_user(target_user_id, target_rich_menu_id)
    
def rich_menu_ii(event):
    col, setting = event.postback.data.split(':')[1:]
    target_user_id = event.source.user_id
    CallDatabase.update_rich_menu_setting(target_user_id, col[:-4].lower(), setting)
    line_bot_api.reply_message(
        event.reply_token, 
        TextSendMessage(text=f'已為您將 {col[:-4]} 設定為 {setting}')
    )
        
def initialize_rich_menu(static_rich_menu_list=static_rich_menu_list):
        
    # 取得使用中的 rich menu
    rich_menu_list = line_bot_api.get_rich_menu_list()
    print('old rich_menu_list:', rich_menu_list)
    
    # 刪去舊的 rich menu
    for old_rich_menu in rich_menu_list:
        print(old_rich_menu.rich_menu_id)
        line_bot_api.delete_rich_menu(old_rich_menu.rich_menu_id)
    
    # 建立新的 rich menu
    for rich_menu, image_path in static_rich_menu_list:
        rich_menu_id = line_bot_api.create_rich_menu(rich_menu)
        print('get rich menu:', rich_menu_id)
        print('getcwd:', os.getcwd())
        print('listdir:', os.listdir())
        with open(image_path, 'rb') as f:
            line_bot_api.set_rich_menu_image(rich_menu_id, 'image/png', f)
        print('successfully set rich menu image for', rich_menu_id)
        
    line_bot_api.set_default_rich_menu(rich_menu_id)