
from rest_framework.routers import DefaultRouter
from products_api.views import dailyDeal, produtList, catList, subCatList, produtImage, seasonProdut, newProdutList

router = DefaultRouter()
router.register('product', newProdutList, basename='product')
router.register('deal', dailyDeal, basename='deal')
router.register('category', catList, basename='category')
router.register('sub-category', subCatList, basename='sub-category')
router.register('Image', produtImage, basename='Image')
router.register('season', seasonProdut, basename='season')


urlpatterns = router.urls

# urlpatterns = [
#     path('api/', produtList.as_view(), name="product"),
#     # path('api/<int:pk>', productDetail.as_view(), name="productDetail"),
# ]
