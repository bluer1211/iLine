# Define our theme color
alpaca_blue = '#066BAF'

def image_in_FlexMessage(url):
    return {"type": "image",
            "url": url,
            "size": "full",
            "aspect_ratio": "20:13",
            "aspect_mode": "cover"}

def text_in_FlexMessage(text, size, color, weight='regular', wrap=False):
    return {"type": "text",
            "text": text,
            "size": size,
            "color": color,
            "weight": weight,
            "wrap": wrap }

#def logo_in_FlexMessage(text='PhoebeFlex'):
def logo_in_FlexMessage(text='iLine'):
    return text_in_FlexMessage(text, size='md', color=alpaca_blue, weight='bold')

def title_in_FlexMessage(text):
    return text_in_FlexMessage(text, size='xl', color='#555555', weight='bold')

def heading_in_FlexMessage(text):
    return text_in_FlexMessage(text, size='xl', color='#555555')

def note_in_FlexMessage(text):
    return text_in_FlexMessage(text, size='md', color='#AAAAAA', wrap=True)

def separator_in_FlexMessage(margin='xl'):
    return {"type": "separator", "margin": margin}

def button_in_FlexMessage(label, data, display_text):
    return {"type": "button",
            "action": {
                "type": "postback",
                "label": label,
                "data": data,
                "display_text": display_text
            },
            "style": "link",
            "color": alpaca_blue,
            "height": "sm"}

def button_text_in_FlexMessage(label, text):
    return {"type": "button",
            "action": {
                "type": "message",
                "label": label,
                "text": text,
            },
            "style": "link",
            "color": alpaca_blue,
            "height": "sm"}

def button_uri_in_FlexMessage(label, uri):
    return {"type": "button",
            "action": {
                "type": "uri",
                "label": label,
                "uri": uri,
            },
            "style": "link",
            "color": alpaca_blue,
            "height": "sm"}

#????????????            
def carousel_covid19_FlexMessage():
    carousel_contents = covid19_FlexMessage(), cook_FlexMessage(), WFH_FlexMessage()
    FlexMessage = {'type': 'carousel',
                   'contents':carousel_contents}  
    print(FlexMessage)  
    return FlexMessage
#????????????            
def carousel_small_feib_FlexMessage():
    carousel_contents = small_FEIB_543_FlexMessage(), small_FEIB_finance_FlexMessage()
    FlexMessage = {'type': 'carousel',
                   'contents':carousel_contents}  
    print(FlexMessage)  
    return FlexMessage

#??????????????????            
def carousel_FEIB_news_FlexMessage():
    carousel_contents = FEIB_retire_FlexMessage(),FEIB_credit_card_FlexMessage(),FEIB_online_loan_FlexMessage()
    FlexMessage = {'type': 'carousel',
                   'contents':carousel_contents}  
    print(FlexMessage)  
    return FlexMessage

#??????????????????
def covid19_FlexMessage():
    hero_image_url = 'https://imgcdn.cna.com.tw/www/WebPhotos/1024/20200531/1152x768_20200531000039.jpg'
    body_contents = [logo_in_FlexMessage(), 
                     title_in_FlexMessage('??????????????????'), 
                     separator_in_FlexMessage(), 
                     note_in_FlexMessage('#??????????????????????????????????????????'),

#                      heading_in_FlexMessage('training'), 
#                      note_in_FlexMessage('# ?????? training ??????'), 
                     separator_in_FlexMessage()]
    footer_contents = [button_uri_in_FlexMessage('????????????????????????', 'https://www.cdc.gov.tw/?openExternalBrowser=1'),
                       button_uri_in_FlexMessage('???????????????????????????', 'https://www.feib.com.tw/upload/IndividualBank/Event/20210610/index.html?openExternalBrowser=1')]
                    
#                       button_in_FlexMessage('training', 'training')]
    FlexMessage = {'type': 'bubble',
                   'hero': image_in_FlexMessage(hero_image_url),
                   'body': {
                       'type': 'box', 
                       'layout': 'vertical', 
                       'spacing': 'md', 
                       'contents':body_contents},
                   'footer': {
                       'type': 'box',
                       'layout': 'vertical',
                       'contents': footer_contents}}
    return FlexMessage
#'??????????????????
def cook_FlexMessage():
    hero_image_url = 'https://wowlavie-aws.hmgcdn.com/file/article_all/%E5%BB%9A%E6%88%BF%E5%B8%B8%E5%82%99%E4%B9%BE%E8%B2%A81.jpg'
    body_contents = [logo_in_FlexMessage(), 
                     title_in_FlexMessage('??????????????????????????????'), 
                     separator_in_FlexMessage(), 
                     note_in_FlexMessage('#?????????????????????????????????????????????? '),

                     separator_in_FlexMessage()]
    footer_contents = [button_text_in_FlexMessage('????????????-??????????????????', '????????????-??????????????????'),
                       button_uri_in_FlexMessage('?????????????????????', 'https://epost.coa.gov.tw/theme_data.php?theme=epost&sub_theme=photo&id=115&openExternalBrowser=1')]

    FlexMessage = {'type': 'bubble',
                   'hero': image_in_FlexMessage(hero_image_url),
                   'body': {
                       'type': 'box', 
                       'layout': 'vertical', 
                       'spacing': 'md', 
                       'contents':body_contents},
                   'footer': {
                       'type': 'box',
                       'layout': 'vertical',
                       'contents': footer_contents}}
    return FlexMessage
#??????-??????????????????
def small_FEIB_cook_FlexMessage():
    hero_image_url = 'https://magazine.feg.com.tw/magazine/upload/article/363E0601.jpg'
    body_contents = [logo_in_FlexMessage(), 
                     title_in_FlexMessage('??????????????????????????????'), 
                     separator_in_FlexMessage(), 
                     note_in_FlexMessage('#???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????'),

                     separator_in_FlexMessage()]
    footer_contents = [button_uri_in_FlexMessage('???????????????', 'https://m.youtube.com/watch?v=Jfodsy2Hx88&list=PLF3_3bQ2C7KFqnFxUBwB839p6Em96Evte&index=14&openExternalBrowser=1'),
                       button_uri_in_FlexMessage('????????????', 'https://m.youtube.com/watch?v=Jfodsy2Hx88&list=PLF3_3bQ2C7KFqnFxUBwB839p6Em96Evte&index=14&openExternalBrowser=1'),
                       button_uri_in_FlexMessage('????????????', 'https://m.youtube.com/watch?v=v4xo7KfWXaI&list=PLF3_3bQ2C7KFqnFxUBwB839p6Em96Evte&index=8&openExternalBrowser=1')]

    FlexMessage = {'type': 'bubble',
                   'hero': image_in_FlexMessage(hero_image_url),
                   'body': {
                       'type': 'box', 
                       'layout': 'vertical', 
                       'spacing': 'md', 
                       'contents':body_contents},
                   'footer': {
                       'type': 'box',
                       'layout': 'vertical',
                       'contents': footer_contents}}
    return FlexMessage

#????????????
def WFH_FlexMessage():
    hero_image_url = 'https://www.incimages.com/uploaded_files/image/1920x1080/getty_769729163_200013341653767170567_404088.jpg'
    body_contents = [logo_in_FlexMessage(), 
                     title_in_FlexMessage('???????????????????????????'), 
                     separator_in_FlexMessage(), 
                     note_in_FlexMessage('#?????????????????????????????????????????????????????????'),

                     separator_in_FlexMessage()]
    footer_contents = [button_uri_in_FlexMessage('?????????????????????WFH????????????', 'https://blog.zerozero.com.tw/29817/5_ways_to_wfh/?openExternalBrowser=1&efr=1'),
                       button_uri_in_FlexMessage('?????????PODCAST????????????', 'https://blog.zerozero.com.tw/29781/podcast_2/?openExternalBrowser=1&efr=1')]

    FlexMessage = {'type': 'bubble',
                   'hero': image_in_FlexMessage(hero_image_url),
                   'body': {
                       'type': 'box', 
                       'layout': 'vertical', 
                       'spacing': 'md', 
                       'contents':body_contents},
                   'footer': {
                       'type': 'box',
                       'layout': 'vertical',
                       'contents': footer_contents}}
    return FlexMessage

#??????543
def small_FEIB_543_FlexMessage():
    hero_image_url = 'https://angelnumber.org/wp-content/uploads/2020/03/543-Angel-Number-700x400.jpg'
    body_contents = [logo_in_FlexMessage(), 
                     title_in_FlexMessage('?????????543'), 
                     separator_in_FlexMessage(), 
                     note_in_FlexMessage('#??????????????????????????????????????????????????????'),

                     separator_in_FlexMessage()]
    footer_contents = [button_uri_in_FlexMessage('????????????', 'https://m.youtube.com/playlist?list=PLF3_3bQ2C7KFqnFxUBwB839p6Em96Evte&openExternalBrowser=1&efr=1')]

    FlexMessage = {'type': 'bubble',
                   'hero': image_in_FlexMessage(hero_image_url),
                   'body': {
                       'type': 'box', 
                       'layout': 'vertical', 
                       'spacing': 'md', 
                       'contents':body_contents},
                   'footer': {
                       'type': 'box',
                       'layout': 'vertical',
                       'contents': footer_contents}}
    return FlexMessage

#????????????
def small_FEIB_finance_FlexMessage():
    hero_image_url = 'https://pic.pimg.tw/begabung/1540499670-3386203240.png'
    body_contents = [logo_in_FlexMessage(), 
                     title_in_FlexMessage('??????????????????'), 
                     separator_in_FlexMessage(), 
                     note_in_FlexMessage('#????????????????????????????????????????????????Easy???'),

                     separator_in_FlexMessage()]
    footer_contents = [button_uri_in_FlexMessage('????????????', 'https://m.youtube.com/playlist?list=PLF3_3bQ2C7KGLeVA6vQ7xRgY7RZczCeti&openExternalBrowser=1&efr=1')]

    FlexMessage = {'type': 'bubble',
                   'hero': image_in_FlexMessage(hero_image_url),
                   'body': {
                       'type': 'box', 
                       'layout': 'vertical', 
                       'spacing': 'md', 
                       'contents':body_contents},
                   'footer': {
                       'type': 'box',
                       'layout': 'vertical',
                       'contents': footer_contents}}
    return FlexMessage

#?????????
def FEIB_loan_FlexMessage():
    hero_image_url = 'https://pic.pimg.tw/begabung/1540499670-3386203240.png'
    body_contents = [logo_in_FlexMessage(), 
                     title_in_FlexMessage('????????? ????????????'), 
                     separator_in_FlexMessage(), 
                     note_in_FlexMessage('#????????????????????????????????????????????????0%'),

                     separator_in_FlexMessage()]
    footer_contents = [button_uri_in_FlexMessage('????????????', 'https://www.feib.com.tw/upload/IndividualBank/WM/happypension/index.html?openExternalBrowser=1')]

    FlexMessage = {'type': 'bubble',
                   'hero': image_in_FlexMessage(hero_image_url),
                   'body': {
                       'type': 'box', 
                       'layout': 'vertical', 
                       'spacing': 'md', 
                       'contents':body_contents},
                   'footer': {
                       'type': 'box',
                       'layout': 'vertical',
                       'contents': footer_contents}}
    return FlexMessage

#?????????
def FEIB_retire_FlexMessage():
    hero_image_url = 'https://www.feib.com.tw/upload/IndividualBank/WM/happypension/webroot/images/kv_pc.jpg'
    body_contents = [logo_in_FlexMessage(), 
                     title_in_FlexMessage('????????? ????????????'), 
                     separator_in_FlexMessage(), 
                     note_in_FlexMessage('#????????????????????????????????????????????????0%'),

                     separator_in_FlexMessage()]
    footer_contents = [button_uri_in_FlexMessage('????????????', 'https://www.feib.com.tw/upload/IndividualBank/WM/happypension/index.html?openExternalBrowser=1')]

    FlexMessage = {'type': 'bubble',
                   'hero': image_in_FlexMessage(hero_image_url),
                   'body': {
                       'type': 'box', 
                       'layout': 'vertical', 
                       'spacing': 'md', 
                       'contents':body_contents},
                   'footer': {
                       'type': 'box',
                       'layout': 'vertical',
                       'contents': footer_contents}}
    return FlexMessage

#????????????
def FEIB_credit_card_FlexMessage():
    hero_image_url = 'https://iapp.feib.com.tw/iapp/images/creditCard/017MS.jpg'
    body_contents = [logo_in_FlexMessage(), 
                     title_in_FlexMessage('????????? ????????????'), 
                     separator_in_FlexMessage(), 
                     note_in_FlexMessage('#?????????????????????????????????'),

                     separator_in_FlexMessage()]
    footer_contents = [button_uri_in_FlexMessage('????????????', 'https://www.feib.com.tw/upload/creditcard/YACard/index.html?empbranch=VD2033&openExternalBrowser=1')]

    FlexMessage = {'type': 'bubble',
                   'hero': image_in_FlexMessage(hero_image_url),
                   'body': {
                       'type': 'box', 
                       'layout': 'vertical', 
                       'spacing': 'md', 
                       'contents':body_contents},
                   'footer': {
                       'type': 'box',
                       'layout': 'vertical',
                       'contents': footer_contents}}
    return FlexMessage

#Online?????????
def FEIB_online_loan_FlexMessage():
    hero_image_url = 'https://www.feib.com.tw/upload/personalloan/event/2021Q3/img/icon_phone.png'
    body_contents = [logo_in_FlexMessage(), 
                     title_in_FlexMessage('Online?????????'), 
                     separator_in_FlexMessage(), 
                     note_in_FlexMessage('#????????????1.8%???(???)??????????????????????????????????????????????????????????????????'),

                     separator_in_FlexMessage()]
    footer_contents = [button_uri_in_FlexMessage('????????????', 'https://www.feib.com.tw/upload/personalloan/event/2021Q3/index.html?openExternalBrowser=1')]

    FlexMessage = {'type': 'bubble',
                   'hero': image_in_FlexMessage(hero_image_url),
                   'body': {
                       'type': 'box', 
                       'layout': 'vertical', 
                       'spacing': 'md', 
                       'contents':body_contents},
                   'footer': {
                       'type': 'box',
                       'layout': 'vertical',
                       'contents': footer_contents}}
    return FlexMessage

#??????????????????????????????????????????
def can_not_find_FlexMessage():
    hero_image_url = 'https://books.cw.com.tw/upload_article/201709/article_1505885369_1.jpg'
    body_contents = [logo_in_FlexMessage(), 
                     title_in_FlexMessage('??????????????????????????????????????????'), 
                     separator_in_FlexMessage(), 
                     note_in_FlexMessage('#???????????????????????????????????????????????????????????????'),

                     separator_in_FlexMessage()]
    footer_contents = [button_uri_in_FlexMessage('??????????????????', 'https://robot.feib.com.tw/Webhook/'),
                       button_text_in_FlexMessage('??????????????????', '??????????????????')]

    FlexMessage = {'type': 'bubble',
                   'hero': image_in_FlexMessage(hero_image_url),
                   'body': {
                       'type': 'box', 
                       'layout': 'vertical', 
                       'spacing': 'md', 
                       'contents':body_contents},
                   'footer': {
                       'type': 'box',
                       'layout': 'vertical',
                       'contents': footer_contents}}
    return FlexMessage

def index_FlexMessage():
    hero_image_url = 'https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_2_restaurant.png'
    body_contents = [logo_in_FlexMessage(), 
                     title_in_FlexMessage('Into the alpaca_training'), 
                     separator_in_FlexMessage(), 
                     heading_in_FlexMessage('Overall'), 
                     note_in_FlexMessage('# ??????????????????'),
                     heading_in_FlexMessage('alpaca_name'), 
                     note_in_FlexMessage('# ?????? alpaca_name ??????'),
#                      heading_in_FlexMessage('training'), 
#                      note_in_FlexMessage('# ?????? training ??????'), 
                     separator_in_FlexMessage()]
    footer_contents = [button_in_FlexMessage('Overall', '::', '?????? Overall'),
                       button_in_FlexMessage('alpaca_name', ':alpaca_name', '?????? alpaca_name')]
#                       button_in_FlexMessage('training', 'training')]
    FlexMessage = {'type': 'bubble',
                   'hero': image_in_FlexMessage(hero_image_url),
                   'body': {
                       'type': 'box', 
                       'layout': 'vertical', 
                       'spacing': 'md', 
                       'contents':body_contents},
                   'footer': {
                       'type': 'box',
                       'layout': 'vertical',
                       'contents': footer_contents}}
    return FlexMessage

def column_FlexMessage(column_name, dataclip):
    body_contents = [logo_in_FlexMessage(), 
                     title_in_FlexMessage(f'Into the {column_name}'), 
                     separator_in_FlexMessage()]
    footer_contents = [button_in_FlexMessage(f"{i}", f":{column_name}='{i}':", f"?????? {i}") for i in dataclip]
    FlexMessage = {'type': 'bubble',
                   'body': {
                       'type': 'box', 
                       'layout': 'vertical', 
                       'spacing': 'md', 
                       'contents':body_contents},
                   'footer': {
                       'type': 'box',
                       'layout': 'vertical',
                       'contents': footer_contents}}
    return FlexMessage

def number_FlexMessage(column_query):
    body_contents = [logo_in_FlexMessage(), 
                     title_in_FlexMessage(f'Into the number'), 
                     separator_in_FlexMessage(),
                     heading_in_FlexMessage('Last 1'), 
                     note_in_FlexMessage('# ????????????????????????'),
                     heading_in_FlexMessage('Last 10'), 
                     note_in_FlexMessage('# ????????????????????????'),
                     separator_in_FlexMessage()]
    footer_contents = [button_in_FlexMessage('Last 1', f":{column_query}:1:", f"?????? {column_query} ????????????"),
                       button_in_FlexMessage('Last 10', f":{column_query}:10:", f"?????? {column_query} ????????????")]
    FlexMessage = {'type': 'bubble',
                   'body': {
                       'type': 'box', 
                       'layout': 'vertical', 
                       'spacing': 'md', 
                       'contents':body_contents},
                   'footer': {
                       'type': 'box',
                       'layout': 'vertical',
                       'contents': footer_contents}}
    return FlexMessage