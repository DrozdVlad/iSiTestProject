from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from Chat.models import Thread, Message
from Chat.serializers import ThreadSerializer, MessageSerializer


class CreateThread(generics.CreateAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        tread = serializer.validated_data['participants']
        all_objs = [obj for obj in self.queryset.values_list('participants', flat=True)]

        if tread in all_objs or tread[:-1] in all_objs:
            obj = self.queryset.filter(participants__in=[tread, tread[:-1]]).values()[0]
            return Response(obj, status=status.HTTP_200_OK)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED, )


class ListOfTreads(generics.ListAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = (IsAuthenticated,)


class DestroyThread(generics.DestroyAPIView):
    queryset = Thread.objects
    serializer_class = ThreadSerializer
    permission_classes = (IsAuthenticated,)


class CreateMessage(generics.CreateAPIView):
    queryset = Message.objects
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs, ):
        data = request.data
        data['thread'] = kwargs['pk']
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RetrieveMessage(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        instance.is_read = True
        instance.save()
        return Response(serializer.data)


class CountUnreadMessages(generics.ListAPIView):
    queryset = Message.objects.all()
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(is_read=False, sender=kwargs['pk'])
        return Response(data={"count_of_unread_messages": queryset.count()})
