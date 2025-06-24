# pip3 install requests
import requests
import json # 确保你导入了json库

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    try:
        response = requests.post(url, json=input_json, headers=headers)
        response.raise_for_status() # 检查HTTP响应状态码

        # 将响应文本转换为字典
        formatted_response = json.loads(response.text)
        
        # 提取情感分数
        # 检查'emotion_predictions'和'emotion'是否存在，以避免KeyError
        if 'emotion_predictions' in formatted_response and \
           len(formatted_response['emotion_predictions']) > 0 and \
           'emotion' in formatted_response['emotion_predictions'][0]:
            
            emotions = formatted_response['emotion_predictions'][0]['emotion']
            
            anger_score = emotions.get('anger', 0)
            disgust_score = emotions.get('disgust', 0)
            fear_score = emotions.get('fear', 0)
            joy_score = emotions.get('joy', 0)
            sadness_score = emotions.get('sadness', 0)
            
            # 找出主导情感
            emotion_scores = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }
            
            # 找到分数最高的情感
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)

            # 返回所需格式的字典
            return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }
        else:
            # 如果API响应中没有情感数据
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

    except requests.exceptions.RequestException as e:
        print(f"请求Watson NLP服务时出错: {e}")
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    except json.JSONDecodeError as e:
        print(f"解析JSON响应时出错: {e}")
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    except Exception as e:
        print(f"发生未知错误: {e}")
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
