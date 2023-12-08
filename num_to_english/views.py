# num_to_english/views.py
from django.shortcuts import render

def default_view(request):
    return render(request, 'index.html')


from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import NumberSerializer
from .utils import convert_number_to_english

@api_view(['GET', 'POST'])
def num_to_english(request):
    if request.method == 'GET':
        number = request.query_params.get('number', '')
        data = {'number': number}
    elif request.method == 'POST':
        serializer = NumberSerializer(data=request.data)
        if serializer.is_valid():
            number = serializer.validated_data['number']
            data = {'number': number}
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid input', 'details': serializer.errors}, status=400)

    try:
        if len(str(number)) > 8:
            raise ValueError('Number exceeds the maximum limit of 8 digits')

        num_in_english = convert_number_to_english(int(number))
        return JsonResponse({'status': 'ok', 'num_in_english': num_in_english})
    except ValueError as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
