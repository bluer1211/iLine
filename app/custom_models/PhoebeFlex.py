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

#抗疫合集            
def carousel_covid19_FlexMessage():
    carousel_contents = covid19_FlexMessage(), cook_FlexMessage(), WFH_FlexMessage()
    FlexMessage = {'type': 'carousel',
                   'contents':carousel_contents}  
    print(FlexMessage)  
    return FlexMessage
#小遠合集            
def carousel_small_feib_FlexMessage():
    carousel_contents = small_FEIB_543_FlexMessage(), small_FEIB_finance_FlexMessage()
    FlexMessage = {'type': 'carousel',
                   'contents':carousel_contents}  
    print(FlexMessage)  
    return FlexMessage

#最新消息合集            
def carousel_FEIB_news_FlexMessage():
    carousel_contents = FEIB_retire_FlexMessage(),FEIB_credit_card_FlexMessage(),FEIB_online_loan_FlexMessage()
    FlexMessage = {'type': 'carousel',
                   'contents':carousel_contents}  
    print(FlexMessage)  
    return FlexMessage

#抗疫我挺你！
def covid19_FlexMessage():
    hero_image_url = 'https://imgcdn.cna.com.tw/www/WebPhotos/1024/20200531/1152x768_20200531000039.jpg'
    body_contents = [logo_in_FlexMessage(), 
                     title_in_FlexMessage('抗疫我挺你！'), 
                     separator_in_FlexMessage(), 
                     note_in_FlexMessage('#全民拚防疫，當握最新疫情資訊'),

#                      heading_in_FlexMessage('training'), 
#                      note_in_FlexMessage('# 按照 training 查詢'), 
                     separator_in_FlexMessage()]
    footer_contents = [button_uri_in_FlexMessage('衛福部疾管署網站', 'https://www.cdc.gov.tw/?openExternalBrowser=1'),
                       button_uri_in_FlexMessage('遠銀數位平台不打祥', 'https://www.feib.com.tw/upload/IndividualBank/Event/20210610/index.html?openExternalBrowser=1')]
                    
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
#'居家自「煮」
def cook_FlexMessage():
    hero_image_url = 'https://wowlavie-aws.hmgcdn.com/file/article_all/%E5%BB%9A%E6%88%BF%E5%B8%B8%E5%82%99%E4%B9%BE%E8%B2%A81.jpg'
    body_contents = [logo_in_FlexMessage(), 
                     title_in_FlexMessage('居家自「煮」健康管理'), 
                     separator_in_FlexMessage(), 
                     note_in_FlexMessage('#煮到懷疑人生?快看線上烹飪示範！ '),

                     separator_in_FlexMessage()]
    footer_contents = [button_text_in_FlexMessage('小遠贏了-五星主廚教學', '小遠贏了-五星主廚教學'),
                       button_uri_in_FlexMessage('線上網購蔬菜箱', 'https://epost.coa.gov.tw/theme_data.php?theme=epost&sub_theme=photo&id=115&openExternalBrowser=1')]

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
#小遠-居家自「煮」
def small_FEIB_cook_FlexMessage():
    hero_image_url = 'https://magazine.feg.com.tw/magazine/upload/article/363E0601.jpg'
    body_contents = [logo_in_FlexMessage(), 
                     title_in_FlexMessage('居家自「煮」健康管理'), 
                     separator_in_FlexMessage(), 
                     note_in_FlexMessage('#吃膩外送餐點還是煮到懷疑人生？五星主廚線上示範享飪秘訣，宅在家也能吃的健康又美味！'),

                     separator_in_FlexMessage()]
    footer_contents = [button_uri_in_FlexMessage('清燉獅子頭', 'https://m.youtube.com/watch?v=Jfodsy2Hx88&list=PLF3_3bQ2C7KFqnFxUBwB839p6Em96Evte&index=14&openExternalBrowser=1'),
                       button_uri_in_FlexMessage('豌豆雞排', 'https://m.youtube.com/watch?v=Jfodsy2Hx88&list=PLF3_3bQ2C7KFqnFxUBwB839p6Em96Evte&index=14&openExternalBrowser=1'),
                       button_uri_in_FlexMessage('蔥燒烏參', 'https://m.youtube.com/watch?v=v4xo7KfWXaI&list=PLF3_3bQ2C7KFqnFxUBwB839p6Em96Evte&index=8&openExternalBrowser=1')]

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

#宅家工作
def WFH_FlexMessage():
    hero_image_url = 'https://www.incimages.com/uploaded_files/image/1920x1080/getty_769729163_200013341653767170567_404088.jpg'
    body_contents = [logo_in_FlexMessage(), 
                     title_in_FlexMessage('宅家工作娛樂全功略'), 
                     separator_in_FlexMessage(), 
                     note_in_FlexMessage('#在家工作或是假日不出門，有哪些可做呢？'),

                     separator_in_FlexMessage()]
    footer_contents = [button_uri_in_FlexMessage('用「五感」開啟WFH的一天！', 'https://blog.zerozero.com.tw/29817/5_ways_to_wfh/?openExternalBrowser=1&efr=1'),
                       button_uri_in_FlexMessage('療癒型PODCAST頻導推薦', 'https://blog.zerozero.com.tw/29781/podcast_2/?openExternalBrowser=1&efr=1')]

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

#小遠543
def small_FEIB_543_FlexMessage():
    hero_image_url = 'https://angelnumber.org/wp-content/uploads/2020/03/543-Angel-Number-700x400.jpg'
    body_contents = [logo_in_FlexMessage(), 
                     title_in_FlexMessage('報馬仔543'), 
                     separator_in_FlexMessage(), 
                     note_in_FlexMessage('#你生活充滿「享樂」「樂富」「樂知」～'),

                     separator_in_FlexMessage()]
    footer_contents = [button_uri_in_FlexMessage('立即觀看', 'https://m.youtube.com/playlist?list=PLF3_3bQ2C7KFqnFxUBwB839p6Em96Evte&openExternalBrowser=1&efr=1')]

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

#小遠財金
def small_FEIB_finance_FlexMessage():
    hero_image_url = 'https://pic.pimg.tw/begabung/1540499670-3386203240.png'
    body_contents = [logo_in_FlexMessage(), 
                     title_in_FlexMessage('最新市場觀點'), 
                     separator_in_FlexMessage(), 
                     note_in_FlexMessage('#一手掌握市場未來趨勢，生活理財好Easy～'),

                     separator_in_FlexMessage()]
    footer_contents = [button_uri_in_FlexMessage('立即觀看', 'https://m.youtube.com/playlist?list=PLF3_3bQ2C7KGLeVA6vQ7xRgY7RZczCeti&openExternalBrowser=1&efr=1')]

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

#即時貸
def FEIB_loan_FlexMessage():
    hero_image_url = 'https://pic.pimg.tw/begabung/1540499670-3386203240.png'
    body_contents = [logo_in_FlexMessage(), 
                     title_in_FlexMessage('快樂退 全民計畫'), 
                     separator_in_FlexMessage(), 
                     note_in_FlexMessage('#快樂退定期定額新戶申購手續費終身0%'),

                     separator_in_FlexMessage()]
    footer_contents = [button_uri_in_FlexMessage('立即申請', 'https://www.feib.com.tw/upload/IndividualBank/WM/happypension/index.html?openExternalBrowser=1')]

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

#快樂退
def FEIB_retire_FlexMessage():
    hero_image_url = 'https://www.feib.com.tw/upload/IndividualBank/WM/happypension/webroot/images/kv_pc.jpg'
    body_contents = [logo_in_FlexMessage(), 
                     title_in_FlexMessage('快樂退 全民計畫'), 
                     separator_in_FlexMessage(), 
                     note_in_FlexMessage('#快樂退定期定額新戶申購手續費終身0%'),

                     separator_in_FlexMessage()]
    footer_contents = [button_uri_in_FlexMessage('立即申請', 'https://www.feib.com.tw/upload/IndividualBank/WM/happypension/index.html?openExternalBrowser=1')]

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

#樂加＋卡
def FEIB_credit_card_FlexMessage():
    hero_image_url = 'https://iapp.feib.com.tw/iapp/images/creditCard/017MS.jpg'
    body_contents = [logo_in_FlexMessage(), 
                     title_in_FlexMessage('快樂退 全民計畫'), 
                     separator_in_FlexMessage(), 
                     note_in_FlexMessage('#首張專注親子禮遇信用卡'),

                     separator_in_FlexMessage()]
    footer_contents = [button_uri_in_FlexMessage('立即申請', 'https://www.feib.com.tw/upload/creditcard/YACard/index.html?empbranch=VD2033&openExternalBrowser=1')]

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

#Online隨時貸
def FEIB_online_loan_FlexMessage():
    hero_image_url = 'https://www.feib.com.tw/upload/personalloan/event/2021Q3/img/icon_phone.png'
    body_contents = [logo_in_FlexMessage(), 
                     title_in_FlexMessage('Online隨時貸'), 
                     separator_in_FlexMessage(), 
                     note_in_FlexMessage('#優惠利率1.8%起(浮)，線上申請且撥款成功月月抽【開辦費全額回饋】'),

                     separator_in_FlexMessage()]
    footer_contents = [button_uri_in_FlexMessage('立即了解', 'https://www.feib.com.tw/upload/personalloan/event/2021Q3/index.html?openExternalBrowser=1')]

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

#很抱歉，目前查不到您要的資料
def can_not_find_FlexMessage():
    hero_image_url = 'https://books.cw.com.tw/upload_article/201709/article_1505885369_1.jpg'
    body_contents = [logo_in_FlexMessage(), 
                     title_in_FlexMessage('很抱歉，目前查不到您要的資料'), 
                     separator_in_FlexMessage(), 
                     note_in_FlexMessage('#建議可以『遠銀智能客服』做進一步詢問～謝謝'),

                     separator_in_FlexMessage()]
    footer_contents = [button_uri_in_FlexMessage('遠銀智能客服', 'https://robot.feib.com.tw/Webhook/'),
                       button_text_in_FlexMessage('查詢更多服務', '查詢更多服務')]

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
                     note_in_FlexMessage('# 查詢所有資料'),
                     heading_in_FlexMessage('alpaca_name'), 
                     note_in_FlexMessage('# 按照 alpaca_name 查詢'),
#                      heading_in_FlexMessage('training'), 
#                      note_in_FlexMessage('# 按照 training 查詢'), 
                     separator_in_FlexMessage()]
    footer_contents = [button_in_FlexMessage('Overall', '::', '查詢 Overall'),
                       button_in_FlexMessage('alpaca_name', ':alpaca_name', '查詢 alpaca_name')]
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
    footer_contents = [button_in_FlexMessage(f"{i}", f":{column_name}='{i}':", f"查詢 {i}") for i in dataclip]
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
                     note_in_FlexMessage('# 查詢最後一筆資料'),
                     heading_in_FlexMessage('Last 10'), 
                     note_in_FlexMessage('# 查詢最後十筆資料'),
                     separator_in_FlexMessage()]
    footer_contents = [button_in_FlexMessage('Last 1', f":{column_query}:1:", f"查詢 {column_query} 最後一筆"),
                       button_in_FlexMessage('Last 10', f":{column_query}:10:", f"查詢 {column_query} 最後十筆")]
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