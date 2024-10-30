import requests
import json

def emotion_detector(text_to_analyze):
    key_max_value = []
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(URL, json = Input, headers = Headers)
    if response.status_code == 200:
        json_response = json.loads(response.text)
    
        json_text = json_response['emotionPredictions'][0]['emotion']
        for key in json_text.keys():
            if len(key_max_value) > 0:
                if float(key_max_value[1]) < float(json_text[key]):
                    key_max_value = [key, json_text[key]]
            else:
                key_max_value = [key, json_text[key]]   
        json_text["dominant_emotion"] = key_max_value[0]
    elif response.status_code == 400:
        json_text = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    return json_text