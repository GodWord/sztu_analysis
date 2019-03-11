function processInnderDiv(domDiv, filters) {
        var click_timestamp = new Date().getTime();
        var click_url = domDiv.getAttribute("href");
        var click_dom_name = domDiv.innerText;
        if (filters.length !== 0 && !filters.includes(click_dom_name)) {
            return
        }
        $.ajax({
            type: "get", //数据发送的方式（post 或者 get）
            url: "http://127.0.0.1:8000/click_api.gif", //要发送的后台地址
            data: {
                'url': click_url,
                'access_time': click_timestamp,
                'dom_name': click_dom_name

            }, //要发送的数据（参数）格式为{'val1':"1","val2":"2"}
            dataType: "json", //后台处理后返回的数据格式
            success: function (data) {//ajax请求成功后触发的方法

            },
            error: function (msg) {//ajax请求失败后触发的方法

            }
        });
    }

    document.getElementById("DHMenu").addEventListener("click", function (event) {
        var menu_not_filters = [];
        processInnderDiv(event.target, menu_not_filters);
    }, false);
    document.querySelector("div.header-navs").addEventListener("click", function (event) {
        var navs_not_filters = ['组织机构'];
        processInnderDiv(event.target, navs_not_filters);
    }, false);
    document.querySelector("div.header-right").addEventListener("click", function (event) {
        var right_not_filters = ['内部网'];
        processInnderDiv(event.target, right_not_filters);
    }, false);