from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class MercadoList(APIView):
    def get(self, request):
        Mercados = Mercado.objects.all()
        serializer = MercadoSerializer(Mercados, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MercadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MercadoView(APIView):
    def get(self, request, mercado_pk):
        try:
            Mercados = Mercado.objects.get(id=mercado_pk)
        except Mercado.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MercadoSerializer(Mercados, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, mercado_pk):
        try:
            instance = Mercado.objects.get(id=mercado_pk)
        except Mercado.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response(status=status.HTTP_200_OK)

    def put(self, request, mercado_pk, item_pk):
        try:
            Mercados = Mercado.objects.get(id=mercado_pk)
            Items = Item.objects.get(id=item_pk)
        except Mercado.DoesNotExist or Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MercadoSerializer(Mercados)
        if serializer.is_valid():
            Mercados.estoque.add(item_pk)
            Mercados.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class EntregaView(APIView):
    def get(self, request):
        Entregas = Entrega.objects.all()
        return Response(EntregaSerializer(Entregas, many=True).data)

    def post(self, request):
        serializer = EntregaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, entrega_pk):
        try:
            instance = Entrega.objects.get(id=entrega_pk)
        except Entrega.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response(status=status.HTTP_200_OK)


class ItemList(APIView):
    def get(self, request):
        Itens = Item.objects.all()
        serializer = ItemSerializer(Itens, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, item_pk):
        try:
            instance = Item.objects.get(id=item_pk)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response(status=status.HTTP_200_OK)
