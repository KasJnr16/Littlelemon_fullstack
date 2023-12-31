from django.shortcuts import render
from .serializers import(
    MenuSerializer,
    BookingSerializer,

)
from .models import(
    MenuAPI,
    BookingAPI,
)
from rest_framework.response import Response
from rest_framework.decorators import(
    api_view,
    permission_classes,
)
from rest_framework.permissions import(
    IsAuthenticated,
)
from rest_framework import status

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def bookingView(request):
    details = BookingAPI.objects.all()
    details_serializer = BookingSerializer(details, many=True)
        
    if request.method == "GET":
        
        return Response(details_serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        details_serializer = BookingSerializer(data=request.data)
        if details_serializer.is_valid():
            details_serializer.save()

            return Response({"message":"Booking Successfully Created"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"error {details_serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def menuView(request, pk = None):
    menu = MenuAPI.objects.all()
    menu_serializer = MenuSerializer(menu, many=True)
    if request.method == 'GET':
        if pk:
            menu_item = MenuAPI.objects.get(id=pk)
            item_serializer = MenuSerializer(menu_item, many=False)
            return Response(item_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(menu_serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        menu_serializer = MenuSerializer(data=request.data)
        if menu_serializer.is_valid():
            menu_serializer.save()
            return Response({"message":f"Has added {menu_serializer.data}"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"error {menu_serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)

