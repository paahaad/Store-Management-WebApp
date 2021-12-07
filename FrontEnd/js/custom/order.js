var productPrices = {};

$(function () {
    //Json data by api call for order table
    $.get(productListApiUrl, function (response) {
        productPrices = {}
        if(response) {
            var options = '<option value="">--Select--</option>';
            $.each(response, function(index, product) {
                options += '<option value="'+ product.productId +'">'+ product.productName +'</option>';
                productPrices[product.productId] = product.pricePerUnit;
            });
            $(".product-box").find("select").empty().html(options);
        }
    });
});

$("#addMoreButton").click(function () {
    var row = $(".product-box").html();
    $(".product-box-extra").append(row);
    $(".product-box-extra .remove-row").last().removeClass('hideit');
    $(".product-box-extra .product-price").last().text('0.0');
    $(".product-box-extra .product-qty").last().val('1');
    $(".product-box-extra .product-total").last().text('0.0');
});

$(document).on("click", ".remove-row", function (){
    $(this).closest('.row').remove();
    calculateValue();
});

$(document).on("change", ".cart-product", function (){
    var product_id = $(this).val();
    var price = productPrices[productId];

    $(this).closest('.row').find('#product_price').val(price);
    calculateValue();
});

$(document).on("change", ".product-qty", function (e){
    calculateValue();
});

$("#saveOrder").on("click", function(){
    var formData = $("form").serializeArray();
    var requestPayload = {
        customerName: null,
        total: null,
        orderdetails: []
    };
    var orderDetails = [];
    for(var i=0;i<formData.length;++i) {
        var element = formData[i];
        var lastElement = null;

        switch(element.name) {
            case 'customerName':
                requestPayload.customerName = element.value;
                break;
            case 'product_grand_total':
                requestPayload.total = element.value;
                break;
            case 'product':
                requestPayload.orderdetails.push({
                    productId: element.value,
                    quantity: null,
                    totalPrice: null
                });                
                break;
            case 'qty':
                lastElement = requestPayload.orderdetails[requestPayload.orderdetails.length-1];
                lastElement.quantity = element.value
                break;
            case 'item_total':
                lastElement = requestPayload.orderdetails[requestPayload.orderdetails.length-1];
                lastElement.totalPrice = element.value
                break;
        }

    }
    callApi("POST", orderSaveApiUrl, {
        'data': JSON.stringify(requestPayload)
    });
});