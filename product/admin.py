from django.contrib import admin
from product.models import Product
from order.models import Order, OrderItem
from django.utils.safestring import mark_safe
from jet.admin import CompactInline

#admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # 필드 선택
    list_display = [ 'id', 'pro_name', 'pro_status', 'pro_price', 'pro_stock', 'content_size', 'orderitem_count']

    fieldsets = [
        ('상품정보', {
            'fields': ('pro_name', 'pro_status', 'pro_price','pro_stock','pro_img','pro_desc',),
        }),
        ('추가정보', {
            'fields': (('pro_new', 'pro_hot'), 'pro_display','pro_day','pro_like'),
        }),
    ]

    # 링크로 지정할 필드
    list_display_links = [ 'id', 'pro_name', ]

    # 목록에서 수정할 필드
    list_editable = [ 'pro_stock' ]

    # 페이지별로 보여줄 갯수(default:100)
    list_per_page = 4

    # 필터 옵션 제공(카테고리로 사용?)
    list_filter = [ 'pro_price']

    # 검색
    search_fields = ('pro_name',)

    # action목록
    actions = ['make_fruit','make_phone', 'make_computer'] 

    # ordering
    ordering = ('id', )


    # Tag Escape
    def content_size(self, product):
        return mark_safe('<u>{}</u>글자'.format(len(product.pro_desc)))
    content_size.short_description = '글자수'

    def orderitem_count(self, obj):
        return OrderItem.objects.filter(product=obj).count()
    orderitem_count.short_description = '주문건수'

    def make_phone(self, request, queryset):
        update_count = queryset.update(pro_status='p')
        self.message_user(request, '{}개의 상품을 Phone으로 변경'.format(update_count))
    make_phone.short_description = '지정 상품을 Phone으로 변경'
    
    def make_computer(self, request, queryset):
        update_count = queryset.update(pro_status='c')
        self.message_user(request, '{}개의 상품을 Computer로 변경'.format(update_count))
    make_computer.short_description = '지정 상품을 Computer로 변경'

    def make_fruit(self, request, queryset):
        update_count = queryset.update(pro_status='f')
        self.message_user(request, '{}개의 상품을 Fruit로 변경'.format(update_count))
    make_fruit.short_description = '지정 상품을 Fruit로 변경'

