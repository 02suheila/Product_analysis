from django.shortcuts import render
from .models import FlipkartData,AmazonData,AJIOData,MyntraData
from django.db import connection
from django.db.models import Q  # Import Q for complex queries
# Create your views here.
from collections import defaultdict


def index(request):
    return render(request,'index.html')

def details(request,platform):
  
    print(platform)
    if platform == "Flipkart":
        Data = FlipkartData.objects.all()
    #print(flipkartData)
    elif platform == "Amazon":
        Data = AmazonData.objects.all()
        #print(Data)
    elif platform == "Ajio":
        Data = AJIOData.objects.all()
    elif platform == "Myntra":
        Data = MyntraData.objects.all()
    else:
        Data = []
    #print("data", Data)


    search_query = request.GET.get('search')
    print("search_query",search_query)
    if search_query:
        if platform == "Flipkart":
            Data = Data.filter(Q(name__icontains=search_query) | Q(email__icontains=search_query))
            print(type(Data))
            #print((Data))
        elif platform == "Amazon":
            Data = Data.filter(Q(name__icontains=search_query) | Q(email__icontains=search_query))
        elif platform == "Ajio":
            Data = Data.filter(Q(name__icontains=search_query) | Q(email__icontains=search_query))
        elif platform == "Myntra":
            Data = Data.filter(Q(name__icontains=search_query) | Q(email__icontains=search_query))
            #print(Data)

    context = {'platform': platform.capitalize(),
               'data' : Data,
               }
    return render(request, "details.html", context)

def all_details(request):
    flipkart_details = FlipkartData.objects.all()
    amazon_details = AmazonData.objects.all()
    ajio_details = AJIOData.objects.all()
    myntra_details = MyntraData.objects.all()

    # Add platform information manually
    for detail in flipkart_details:
        detail.platform = 'Flipkart'
    for detail in amazon_details:
        detail.platform = 'Amazon'
    for detail in ajio_details:
        detail.platform = 'AJIO'
    for detail in myntra_details:
        detail.platform = 'Myntra'
        
    # Combine all names into a single list (set to avoid duplicates)
    all_d = list(flipkart_details) + list(amazon_details) + list(ajio_details) + list(myntra_details)

    # Dictionary to store aggregated results, using (name, email) as the key
    aggregated_data = defaultdict(lambda: {
        'name': '',
        'email': '',
        'orders': 0,
        'returns': 0,
        'deliveries': 0,
        'platforms': set()  # To store the platforms the user is using
    })
    #print("a",aggregated_data)

    # Loop through each detail and aggregate data by name and email
    for detail in all_d:
        key = (detail.name, detail.email)
        #print(key)
        # Aggregate the data
        aggregated_data[key]['name'] = detail.name
        aggregated_data[key]['email'] = detail.email
        aggregated_data[key]['orders'] += detail.orders
        aggregated_data[key]['returns'] += detail.returns
        aggregated_data[key]['deliveries'] += detail.deliveries
        aggregated_data[key]['platforms'].add(detail.platform)
    #print(aggregated_data)
    # Convert platforms set to list for each user
    for key in aggregated_data:
        aggregated_data[key]['platforms'] = list(aggregated_data[key]['platforms'])
    #print(aggregated_data)
    search_query = request.GET.get('search')
    print("search_query",search_query)
    if search_query:
        filtered_data = [
            data for data in aggregated_data.values()
            if search_query.lower() in data['name'].lower()
        ]
    else:
        # If no search query, return all data
        filtered_data = aggregated_data.values()

    # Pass the filtered or unfiltered data to the context
    context = {'aggregated_data': filtered_data}

    return render(request, 'all_details.html', context)
    
    


   