from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def siginup(request):    
    if request.method=="POST":
        # firstName=request.POST['firstName']
        # lastName=request.POST['lastName']
        # email=request.POST['email']
        # password=request.POST['password']
        # print(f"DB에 {firstName}, {lastName}, {email}, {password} 정보의 고객이 등록되었습니다.")
        return JsonResponse({"message": "회원가입 성공"})

    # post 요청이 왔을때 안의 내용
    """
    오는 요청
        {
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string"
        }
    응답
    {
    "message": "회원가입 성공",
    }
    """

    return JsonResponse({"hello":"world"})