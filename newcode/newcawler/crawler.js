var page = require('webpage').create();
var system = require('system');

var args = system.args;
var site = 'http://www.walmart.ca' + args[1].substr(6,args[1].length - 7);

phantom.addCookie({
    'name': 'walmart.nearestPostalCode',
    'value': 'N2A1A0',
    'domain': '.walmart.ca'
});
phantom.addCookie({
    'name': 'walmart.preferredstore',
    'value': '1156',
    'domain': '.walmart.ca'
});

page.open(site, function(status){
    window.setInterval(function(){
        page.injectJs("jquery-2.1.0.js");
        window.setTimeout(function () {
        var p = page.evaluate(function() {   
            $.post( "http://www.walmart.ca/ws/store/products", {stores:"%5B%221156%22%2C%221111%22%2C%223156%22%2C%221155%22%5D&products=%5B%7B%22productid%22%3A%226000045061034%22%2C%22skus%22%3A%5B%7B%22skuid%22%3A%22000006020098773%22%2C%22storeeligible%22%3Atrue%7D%5D%7D%5D "});

            var name = $($("#product-desc > h1")).text();

            var instock = $($("#store-0 > .instock")).css("display");
            var limited = $($("#store-0 > .limited")).css("display");
            var outofstock = $($("#store-0 > .outofstock")).css("display");

            var image = $($("div.centered-img-wrap > img")[0]).attr("src");

            var category = "";
            var categoryList = $("nav.breadCrumb > ul >li >a");
            for (var i = 0; i < categoryList.length; i++) {
                category += "->" + $(categoryList[i]).text();
            }
			
            var discription = $($("div.mobile-hide > div > p")).text();
            if ( discription == ""){
                discription = $("div.mobile-hide > div >div > p").text();
            }
			if ( discription == ""){
                discription = $($("div.mobile-hide > div > ul > li")[0]).text();
            }if ( discription == ""){
                discription = $("div.mobile-hide > div > div > div > p").text();
            }
			
            var price = $($('div.price-current')[0]).html();
			var localprice1 = $($('span#store-price')[0]).html();
			var localprice2 = $($('span#store-price')[1]).html();
			var localprice3 = $('div#store-0 > .price').html();
			var pricewas1 = $('div#pricing > .price-was').text();
			var pricewas2 = $('div#store-0 > .was-price').html();


            return instock + '","' + limited + '","' + outofstock + '","' + name + '","' + category + '","' + discription + '","' + image + '","' + price + '","' +  localprice1 + '","' + localprice2 + '","' + localprice3 + '","' + pricewas1 + '","' + pricewas2 + '"';
        });
        console.log('"' + site + '","' + p);
        phantom.exit();
        }, 10000);
    });
});

