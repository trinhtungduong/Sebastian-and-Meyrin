from karen_data import *

#AI - data
bot_name = 'K.A.R.E.N.'
b_name = 'Karen'
user_name = 'Peter'
user_born = "March 20, 2001"
place_now = 'ct5,khu đô thị xala, hà đông, hà nội'
AI_pass = '2003'

#312-QA
chatbot_data = {
    1 : main_karen_data,
    2 : science_karen_data,
    3 : conversation_karen_data    
}

#total cmd = 63
chatbot_command = {
    'tắt nguồn' : [
        'tắt nguồn',
        'ngắt kết nối',
        'tắt kết nối',
        'tạm biệt',
        'tạm biệt karen',
        'chúc ngủ ngon',
        'ngủ ngon',
        'tôi ra ngoài',
        'tôi phải ra ngoài',        
    ],
    #9
    'giờ' : [
        'bây giờ là mấy giờ',
        'mấy giờ rồi',
        'bây giờ là'

    ],
    #3
    'ngày' : [
        'hôm nay là ngày nào',
        'hôm nay là',
        'hôm nay là ngày mấy',
        'hôm nay là ngày bao nhiêu',
        'nay là ngày bao nhiêu',
        'nay là ngày nào',
        'nay là ngày mấy'
    ],
    #7
    'thời tiết' : [
        'thời tiết hôm nay như thế nào',
        'thời tiết hôm nay',
        'thời tiết hôm nay như nào',
        'thời tiết hôm nay ra sao',
        'thời tiết như nào',
        'thời tiết thì sao',
        'thời tiết ra sao'
    ],
    #7
    'ở đâu' : [
        'tôi đang ở đâu',
        'vị trí hiện tại của tôi',
        'vị trí hiện tại',
        'đây là nơi nào',
        'định vị tôi',
        'định vị vị trí của tôi'
    ],
    #6
    'đi tới' : [
        'đi tới',
        'tới',
        'đường đi tới',
        'tìm đường đi tới',
        'cho tôi tới',        
    ],
    #5
    'thông tin' : [
        'tìm thông tin cho tôi',
        'cho tôi biết về',
        'tìm thông tin về',
        'cho tôi biết'                
    ],
    #4
    'web' : [
        'mở mạng cho tôi',
        'mở website cho tôi',
        'mở mạng',
        'mở web',
        'mở website',
        'mở web cho tôi',
        'mạng',
        'web',
        'website',
        'mở youtube',
        'mở google',
        'mở facebook'
    ],
    #12
    'nghỉ ngơi' : [
        'chế độ nghỉ ngơi',
        'ngủ trưa',
        'nghỉ ngơi',
        'nghỉ ngơi đi',
        'ok nghỉ ngơi đi',
        'im lặng',
        'im',
        'im miệng',
        'im mồm'
    ]
    #2   

}
