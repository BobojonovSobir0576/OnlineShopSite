from django.urls import path
from catalog.views.season_views import *
from catalog.views.cartype_views import *
from catalog.views.country_manufacter_views import *
from catalog.views.brands_views import *
from catalog.views.guide_characteristic_views import *
from catalog.views.guide_units_measurement_views import *


urlpatterns = [
    # season
    path('season_create/',SeasonCreateViews.as_view(),name='create_season'),
    path('season_list/',season_list,name='list_season'),
    path('season_delete/',seaseonDelete,name="season_delete"),
    path('season_detail/',SeasonDetailViews.as_view(),name='season_detail'),
    path('season_update/',SeasonUpdateViews.as_view(),name='season_update'),
    
    # cartypes
    path('cartypes_create/',CarTypesCreateViews.as_view(),name='create_cartypes'),
    path('cartypes_list/',cartypes_list,name='list_cartypes'),
    path('cartypes_delete/',cartypesDelete,name="cartypes_delete"),
    path('cartypes_detail/',CarTypesDetailViews.as_view(),name='cartypes_detail'),
    path('cartypes_update/',CarTypesUpdateViews.as_view(),name='cartypes_update'),

    # countryManafacture
    path('countryManufacter_create/',CountryManufacterCreateViews.as_view(),name='create_countryManufacter'),
    path('countryManufacter_list/',countryManufacter_list,name='list_countryManufacter'),
    path('countryManufacter_delete/',countryManufacterDelete,name="countryManufacter_delete"),
    path('countryManufacter_detail/',CountryManufacterDetailViews.as_view(),name='countryManufacter_detail'),
    path('countryManufacter_update/',CountryManufacterUpdateViews.as_view(),name='countryManufacter_update'),

    # brands
    path('brands_create/',BrandsCreateViews.as_view(),name='create_brands'),
    path('brands_list/',brands_list,name='list_brands'),
    path('brands_delete/',brandsDelete,name="brands_delete"),
    path('brands_detail/',BrandsDetailViews.as_view(),name='brands_detail'),
    path('brands_update/',BrandsUpdateViews.as_view(),name='brands_update'),

    # guideCharacteristic
    path('guideCharacteristic_create/',GuideCharacteristicCreateViews.as_view(),name='create_guideCharacteristic'),
    path('guideCharacteristic_list/',guideCharacteristic_list,name='list_guideCharacteristic'),
    path('guideCharacteristic_delete/',guideCharacteristicDelete,name="guideCharacteristic_delete"),
    path('guideCharacteristic_detail/',GuideCharacteristicDetailViews.as_view(),name='guideCharacteristic_detail'),
    path('guideCharacteristic_update/',GuideCharacteristicUpdateViews.as_view(),name='guideCharacteristic_update'),

    # guideUnitsMeasurement
    path('guideUnitsMeasurement_create/',GuideUnitsMeasurementCreateViews.as_view(),name='create_guideUnitsMeasurement'),
    path('guideUnitsMeasurement_list/',guideUnitsMeasurement_list,name='list_guideUnitsMeasurement'),
    path('guideUnitsMeasurement_delete/',guideUnitsMeasurementDelete,name="guideUnitsMeasurement_delete"),
    path('guideUnitsMeasurement_detail/',GuideUnitsMeasurementDetailViews.as_view(),name='guideUnitsMeasurement_detail'),
    path('guideUnitsMeasurement_update/',GuideUnitsMeasurementUpdateViews.as_view(),name='guideUnitsMeasurement_update'),

]   
