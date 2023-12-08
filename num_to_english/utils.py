def convert_number_to_english(number):
    if number == 0:
        return 'zero'

    if number < 0:
        return 'negative ' + convert_number_to_english(abs(number))

    if number > 99999999:  # Limit to 8 digits
        raise ValueError('Number exceeds the maximum limit of 8 digits')

    units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    result_parts = []

    # Convert millions, thousands, and hundreds
    for scale, name in [(1000000, 'million'), (1000, 'thousand'), (100, 'hundred')]:
        if number >= scale:
            result_parts.append(f'{convert_number_to_english(number // scale)} {name}')
            number %= scale

    # Convert tens and units
    if number >= 20 or number == 10:
        result_parts.extend([tens[number // 10], units[number % 10]])
    elif number >= 10:
        result_parts.append(teens[number - 10])
    else:
        result_parts.append(units[number])

    return ' '.join(result_parts).strip()


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def num_to_english(request):
    if request.method == 'GET':
        number = request.GET.get('number', '')
        data = {'number': number}
    elif request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            number = data.get('number', '')
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON format'}, status=400)

    try:
        # Validate number length
        if len(str(number)) > 8:
            raise ValueError('Number exceeds the maximum limit of 8 digits')

        num_in_english = convert_number_to_english(int(number))
        return JsonResponse({'status': 'ok', 'num_in_english': num_in_english})
    except ValueError as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
