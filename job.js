var fs = require("fs");
var page = require('webpage').create();

page.onConsoleMessage = function(msg) {
  console.log('Page log:' + msg);
};

var url = 'http://www.sgx.com/wps/portal/sgxweb/home/marketinfo/historical_data/derivatives/';
page.open(url, function() {
    page.includeJs("http://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js", function() {
        var data = page.evaluate(function() {
            var arr = new Array;
            var trlist = $(".sgxTableGrid tbody tr");
            trlist.each(function (idx, tr){
                var tdlist = tr.children;
                var items = [
                    tdlist[0].innerText,
                    tdlist[1].innerText, tdlist[1].children[0].href,
                    tdlist[2].innerText, tdlist[2].children[0].href,
                    tdlist[3].innerText, tdlist[3].children[0].href,
                ];

                var content = JSON.stringify(items);
                console.log(content);
                arr.push(items);
            });

            return JSON.stringify(arr);
        });

        fs.write("data.txt", data);
        phantom.exit();
    });
});
