from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

def keyboard(request):
    return JsonResponse({
        'type':'buttons',
        'buttons':['상체', '하체']
    })

@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']

    if datacontent == '상체':
        upper = "벤치프레스"
        return JsonResponse({
            'message': {
                'text': upper
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['하체', '']
            }
        })
    elif datacontent == '하체':
        lower = "스쿼트"
        return JsonResponse({
            'message': {
                'text': lower
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['상체', '등']
            }
        })
    elif datacontent == '등':
        back = "데드리프트"
        return JsonResponse({
            'message': {
                'text':back
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['상체', '하체']
           }
        })