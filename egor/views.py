import requests
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'POST':
        api_key = 'sk-rClWekb6qEtUILnOEW6GKz8UO9voCnCgy4qiPCzyKPd8T3kqdKK9xpDZnJoK'
        input = {
            "messages": [
            {
                "role": "user",
                "content": request.POST['value']
            }
        ],
            "is_sync": True,
        }

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }

        url_endpoint = "https://api.gen-api.ru/api/v1/networks/chat-gpt-3"
        response = requests.post(url_endpoint, json=input, headers=headers)
        return render(request, 'index.html', {'msg': response.json()['choices'][0]['message']['content']})
    return render(request, 'index.html')