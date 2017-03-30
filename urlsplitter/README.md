大家都认识 URL, http://www.baidu.com 就是一个好例子

实现一个能拆解URL的方法. 百度这个例子的结果应该是：

    protocol: "http"
    domain: "www.google.se"
    path: 在本例中是空字符串

下面还有几个例子:

    "http://some.thing" 应该得到 
        protocol=="http"
        domain==some.thing
        path="
        
    "ftp://a.large.site" 应该得到
        protocol=="ftp"
        domain=="a.large.site"
        path=""
        
    "http://a.site.with/a-path" 应该得到 
        protocol=="http"
        domain==a.site.with
        path=="a-path"