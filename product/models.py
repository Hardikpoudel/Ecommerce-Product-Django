from django.db import models
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.
from django.db import models

# Create your models here.


class category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'
    categoryName = models.CharField(max_length=500)
    categoryIconImg = models.ImageField(upload_to='', blank=True)

    def __str__(self):
        return f"{self.categoryName}"


class subCat(models.Model):
    subCatName = models.CharField(max_length=500)
    catID = models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subCatName}"


class seasonProduct(models.Model):
    seasonName = models.CharField(
        max_length=100, blank=False, default="Summer")

    def __str__(self):
        return self.seasonName


class products(models.Model):
    class Meta:
        verbose_name_plural = 'products'
    productName = models.CharField(max_length=500, blank=True)
    productSlug = models.SlugField(max_length=250, blank=True)
    seasonID = models.ForeignKey(seasonProduct, on_delete=models.CASCADE)
    categoryID = models.ForeignKey(category, on_delete=models.CASCADE)
    subCatID = models.ForeignKey(subCat, on_delete=models.CASCADE)
    catName = models.CharField(max_length=500)
    subCatName = models.CharField(max_length=500)
    seasonName = models.CharField(max_length=100, blank=True, null=True)
    previewImg = models.ImageField(upload_to='', blank=True)

    def __str__(self):
        return f"{self.productName}"

    def save(self, *args, **kwargs):
        if not self.productSlug:
            t_slug = slugify(self.productName)
            origin = 1
            unique_slug = t_slug
            while products.objects.filter(productSlug=unique_slug).exists():
                unique_slug = '{}{}'.format(t_slug, origin)
                origin += 1
            self.productSlug = unique_slug
        super().save(*args, **kwargs)


class dailyDeals(models.Model):
    class Meta:
        verbose_name_plural = 'daily deals'

    productID = models.ForeignKey(products, on_delete=models.CASCADE)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def __str__(self):
        return f"{self.productID}"

    def save(self, *args, **kwargs):
        ''' On save, update timestamps 
        created is only updated if id is not set
        i.e. item is first created
        '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(dailyDeals, self).save(*args, **kwargs)


class productVariation(models.Model):
    productID = models.ForeignKey(products, on_delete=models.CASCADE)
    variationName = models.CharField(max_length=500)


class productVariationOpt(models.Model):
    productVariationID = models.ForeignKey(
        productVariation, on_delete=models.CASCADE)
    variationName = models.CharField(max_length=500)


class productCombination(models.Model):
    combinationString = models.CharField(max_length=500)
    SKU = models.CharField(max_length=50)
    uniqueStrID = models.CharField(max_length=500)
    productID = models.ForeignKey(products, on_delete=models.CASCADE)
    variationName = models.CharField(max_length=500)
    availableStock = models.IntegerField()


class productStock(models.Model):
    productID = models.ForeignKey(products, on_delete=models.CASCADE)
    productCombinationID = models.ForeignKey(
        productCombination, on_delete=models.CASCADE)
    unitPrice = models.IntegerField()
    totalStock = models.IntegerField()


class imageGallery(models.Model):
    small = models.CharField(max_length=100)
    medium = models.CharField(max_length=100)
    large = models.CharField(max_length=100)


class productImage(models.Model):
    imageGalleryID = models.ForeignKey(imageGallery, on_delete=models.CASCADE)
    productVariationID = models.ForeignKey(
        productVariationOpt, on_delete=models.CASCADE)
    isFeatured = models.BooleanField(default=False)
