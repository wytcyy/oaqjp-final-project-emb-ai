# pip3 install requests
import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=input_json, headers=headers)
    
    # Check for HTTP errors and return None if unsuccessful
    if response.status_code != 200:
        return {
            'anger': None, 'disgust': None, 'fear': None,
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)
    
    # Extract emotion scores safely
    emotions = formatted_response['emotion_predictions'][0]['emotion']
    
    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)
    
    # Find the dominant emotion
    emotion_scores = {
        'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score,
        'joy': joy_score, 'sadness': sadness_score
    }
    
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Return the required dictionary format
    return {
        'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score,
        'joy': joy_score, 'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
