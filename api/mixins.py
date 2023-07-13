from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class ListUpdateViewSet(mixins.ListModelMixin,
                        mixins.UpdateModelMixin, GenericViewSet):
    pass


class CreateListUpdateViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                              mixins.UpdateModelMixin, GenericViewSet):
    pass

