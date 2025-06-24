# pip install requests
import requests # 用于发送HTTP请求

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    try:
        response = requests.post(url, json=input_json, headers=headers)
        response.raise_for_status() # 检查HTTP响应状态码
        return response.text # 返回API响应的原始文本
    except requests.exceptions.RequestException as e:
        print(f"request Watson NLP error: {e}")
        return None
    except Exception as e:
        print(f"unkown error: {e}")
        return None
