import requests
import json

def emotion_detector(text_to_analyze):
    # defining variables for request
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myObj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # sending request and getting response
    response = requests.post(URL, json=myObj, headers=header)

    # user entered a blank entry
    if (response.status_code == 400):
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        highest = None
    # user entered a valid entry
    else:
        # extracting information
        formatted_response = json.loads(response.text)

        emotion_dict = formatted_response["emotionPredictions"][0]["emotion"]
        
        anger_score = emotion_dict["anger"]
        disgust_score = emotion_dict["disgust"]
        fear_score = emotion_dict["fear"]
        joy_score = emotion_dict["joy"]
        sadness_score = emotion_dict["sadness"]
        
        highest = max(emotion_dict, key=emotion_dict.get)
    
    # preparing output
    output = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': highest
    }

    return output
