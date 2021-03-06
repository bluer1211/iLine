from app import line_bot_api
from app.custom_models import utils, CallDatabase, PhoebeFlex

from linebot.models import TextSendMessage, ImageSendMessage, TemplateSendMessage, FlexSendMessage
from linebot.models import ImageCarouselTemplate, ImageCarouselColumn, URIAction

import random
    
def query_record(event):
    #pretty_echo(event)
    if '查詢訓練紀錄' in event.message.text:
        line_bot_api.reply_message(
            event.reply_token, 
            FlexSendMessage(alt_text='query record: index', contents=PhoebeFlex.index_FlexMessage())
        )
        return True
    elif '綁定個人化服務' in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='想不開嗎? 您需要吉吉、美美、綾綾、RR還有AA的開導喔~')
            )
        '''
        line_bot_api.reply_message(
            event.reply_token, 
            FlexSendMessage(alt_text='綁定個人化服務', contents=PhoebeFlex.index_FlexMessage())
        )
        '''
        return True
    elif '抗疫我挺你' in event.message.text:
        line_bot_api.reply_message(
            event.reply_token, 
            FlexSendMessage(alt_text='query record: index', contents=PhoebeFlex.carousel_covid19_FlexMessage())
        )
        return True
    elif '小遠贏了-五星主廚教學' in event.message.text:
        line_bot_api.reply_message(
            event.reply_token, 
            FlexSendMessage(alt_text='query record: index', contents=PhoebeFlex.small_FEIB_cook_FlexMessage())
        )
        return True
    elif '小遠贏了' in event.message.text:
        line_bot_api.reply_message(
            event.reply_token, 
            FlexSendMessage(alt_text='query record: index', contents=PhoebeFlex.carousel_small_feib_FlexMessage())
        )
        return True
    elif '最新活動' in event.message.text:
        line_bot_api.reply_message(
            event.reply_token, 
            FlexSendMessage(alt_text='query record: index', contents=PhoebeFlex.carousel_FEIB_news_FlexMessage())
        )

        return True
    elif '理專配對' in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='財富翻倍!!!')
            )    
        return True
    elif '更多服務' in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='筆筆累了~')
            )    
        '''
        line_bot_api.reply_message(
            event.reply_token, 
            FlexSendMessage(alt_text='query record: index', contents=PhoebeFlex.index_FlexMessage())
        )
        '''
        return True
    else:
        line_bot_api.reply_message(
            event.reply_token, 
            FlexSendMessage(alt_text='query record: index', contents=PhoebeFlex.can_not_find_FlexMessage())
        )        
        return False
    
def query_record_i(event):
    query = event.postback.data
    column_name = query.split(':')[1]
    dataclip = CallDatabase.line_select_distinct(column_name)
    line_bot_api.reply_message(
        event.reply_token, 
        FlexSendMessage(
            alt_text=f'query record: column {column_name}', 
            contents=PhoebeFlex.column_FlexMessage(column_name, dataclip))
    )
    
def query_record_ii(event):
    query = event.postback.data
    column_query = query.split(':')[1]
    line_bot_api.reply_message(
        event.reply_token, 
        FlexSendMessage(alt_text='query record: number', contents=PhoebeFlex.number_FlexMessage(column_query))
    )

def query_record_iii(event):
    query = event.postback.data
    column_query = query.split(':')[1]
    number_query = query.split(':')[2]
    dataclip = CallDatabase.line_select_record(column_query, number_query)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=str(dataclip))
    )

def insert_record(event):
    if '遠銀寶貝訓練紀錄' in event.message.text:
        try:
            record_list = utils.prepare_record(event.message.text)
            result = CallDatabase.line_insert_record(record_list)
            
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=result)
            )
            
            return True
        except:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='失敗了')
            )
            return True
    else:
        return False


def isch_reply(event):
    try:
        print(event)
        target = event.message.text
        engine, method = CallDatabase.query_rich_menu_setting(event.source.user_id)
        print(engine, method)
        img_url, random_img_list = utils.image_search(engine, target)
        method == 'Image'
        if method == 'Image':
            line_bot_api.reply_message(
                event.reply_token, ImageSendMessage(
                    original_content_url=img_url,
                    preview_image_url=img_url
                )
            )
        elif method == 'Carousel':
            img_template = ImageCarouselTemplate(
                columns=[ImageCarouselColumn(image_url=url, action=URIAction(label=f'image{i}', uri=url)) for i, url in enumerate(random_img_list)]
            )
            print(img_url)
            line_bot_api.reply_message(
                event.reply_token,
                TemplateSendMessage(
                    alt_text=f'ImageCarousel template {target}',
                    template=img_template
                )
            )
        
        return True

    except:
        return False
    

def pretty_echo(event):
    
    pretty_note = '♫♪♬'
    pretty_text = ''

    for i in event.message.text:
        pretty_text += i
        pretty_text += f" {random.choice(pretty_note)} "
    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=pretty_text)
    )
    
    return True