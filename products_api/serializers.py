from rest_framework import serializers
from product.models import products, productStock, dailyDeals, category, subCat, productVariation, productVariationOpt, productCombination, productStock, imageGallery, productImage, seasonProduct


class categorySerializer(serializers.ModelSerializer):
    # categoryName = serializers.CharField(max_length=200)

    class Meta:
        model = category
        fields = '__all__'


class subCatSerializer(serializers.ModelSerializer):
    # catID = categorySerializer()

    class Meta:
        model = subCat
        fields = '__all__'


class seasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = seasonProduct
        fields = '__all__'


class productSerializer(serializers.ModelSerializer):
    categoryID = categorySerializer()
    subCatID = subCatSerializer()
    seasonID = seasonSerializer()

    class Meta:
        model = products
        fields = '__all__'  # ['categoryID']


class productVarSerializer(serializers.ModelSerializer):
    productID = productSerializer()

    class Meta:
        model = productVariation
        fields = '__all__'


class productVarOptSerializer(serializers.ModelSerializer):
    productVariationID = productVarSerializer()

    class Meta:
        model = productVariationOpt
        fields = '__all__'


class productCombSerializer(serializers.ModelSerializer):
    productID = productSerializer()

    class Meta:
        model = productCombination
        fields = '__all__'


class productStockSerializer(serializers.ModelSerializer):
    productID = productSerializer()
    productCombinationID = productCombSerializer()

    class Meta:
        model = productStock
        fields = '__all__'


class gallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = imageGallery
        fields = '__all__'


class productImageSerializer(serializers.ModelSerializer):
    imageGalleryID = gallerySerializer()
    productVariationID = productVarSerializer()

    class Meta:
        model = productImage
        fields = '__all__'


class dealSerializer(serializers.ModelSerializer):
    productID = productSerializer()

    class Meta:
        model = dailyDeals
        fields = '__all__'

    # class Meta:

    #     model = productStock
    #     fields = ['unitPrice']
