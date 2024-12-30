from django.shortcuts import render, HttpResponse
from .models import *
from django.http import JsonResponse




def login(request):
    return render(request,"login.html")


def register(request):
    return render(request,"registration.html")


def main(request):
    return render(request,"main.html")


def customers_list(request):
    customers = Customer.objects.all()
    data = [
        {
            'id': customer.id,
            'first_name': customer.first_name,
            'second_name': customer.second_name,
            'email': customer.email,
            'mobile': customer.mobile,
        }
        for customer in customers
    ]
    return JsonResponse(data, safe=False)

def debts_list(request):
    debts = Debt.objects.select_related('customer').all()
    data = [
        {
            'id': debt.id,
            'amount_debt': debt.amount_debt,
            'status_debt': debt.status_debt,
            'customer_name': f"{debt.customer.first_name} {debt.customer.second_name}",
        }
        for debt in debts
    ]
    return JsonResponse(data, safe=False)



def select_customer(request):
    pass
    # if request.method == 'POST':
    #     try:
    #         print(request.body)

    #         data = json.loads(request.body)
    #         item_id = data.get('item_id')
    #         customer_id = data.get('customer_id')
            
    #         customer_select=Customer.objects.get(id=customer_id)
    #         item=Item.objects.get(id=item_id)
            
    #         item.customer=customer_select
    #         item.isAvailble=False
    #         item.sold_date=datetime.now()
    #         item.save()
    #         return JsonResponse({'success': True, 'message': f'{item.name_item} was sold Successfully by {customer_select.first_name} {customer_select.second_name} ! '})
        
    #     except json.JSONDecodeError as e:
    #         return JsonResponse({
    #     "error": "Invalid JSON format",
    #     "message": str(e)
    # }, status=400)
    # else:
    #         return JsonResponse({"error": "Invalid request method"}, status=405)



def customers_view(request):
    try:
        customers = Customer.objects.all().values('id', 'first_name', 'second_name')
        return JsonResponse(list(customers), safe=False)
    except Exception as e:
        print(f"Error fetching customers: {e}")
        return JsonResponse({'error': 'Failed to retrieve customers'}, status=500)