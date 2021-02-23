from django.shortcuts import render
from googleapiclient.discovery import build
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def custom_query(request,query):
    api_key = "AIzaSyCj7RXHNUZ4QWTjKsLOXQTy4WCEqAw7Gbw"
    cse_id = "9715ddd07cdfd470b"
    query_service = build("customsearch","v1",developerKey=api_key)
    query_results = query_service.cse().list(q=query,cx=cse_id,num=5).execute()
    results= query_results['items']
    my_results_dic = {}
    for result in results:
        my_results_dic[result['title']]=result['link']
    return Response(my_results_dic)



