from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from .serializers import dealSerializer, productSerializer, categorySerializer, subCatSerializer, productImageSerializer, seasonSerializer
from product.models import products, dailyDeals, category, subCat, productImage, seasonProduct
from rest_framework.response import Response
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
# Create your views here.


class produtList(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = productSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['productName', 'catName', 'seasonName', 'subCatName']

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(products, productSlug=item)


class newProdutList(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = products.objects.all().order_by('-id')
    serializer_class = productSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['productName', 'catName', 'seasonName', 'subCatName']


class dailyDeal(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = dailyDeals.objects.all()
    serializer_class = dealSerializer


class seasonProdut(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = seasonProduct.objects.all()
    serializer_class = seasonSerializer
    filterset_fields = ['seasonName']


class catList(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = category.objects.all()
    serializer_class = categorySerializer


class subCatList(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = subCat.objects.all()
    serializer_class = subCatSerializer


class produtImage(viewsets.ModelViewSet):
    queryset = productImage.objects.all()
    serializer_class = productImageSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')

        return get_object_or_404(products, productSlug=item)

    # class produtList(viewsets.ViewSet):
    #     permission_classes = [IsAuthenticated]
    #     queryset = products.objects.all()

    #     def list(self, request):
    #         serializer_class = productSerializer(self.queryset, many=True)
    #         return Response(serializer_class.data)

    #     def retrieve(self, request, pk=None):
    #         post = get_object_or_404(self.queryset, pk=pk)
    #         serializer_class = productSerializer(post)
    #         return Response(serializer_class.data)

    # class produtList(generics.ListCreateAPIView):
    #     queryset = products.objects.all()
    #     serializer_class = productSerializer

    # class productDetail(generics.RetrieveAPIView):
    #     queryset = products.objects.all()
    #     serializer_class = productSerializer
