# OrderByTornado
基于tornado后台开发的微信小程序订餐系统

## 说明
该项目是来源于慕课网上的[Python Flask构建微信小程序订餐系统](https://coding.imooc.com/class/265.html)，考虑到tornado的高并发的性能优势，我将后台用tornado进行全部重写，并做了一些功能模块的简化（最主要的就是支付功能，毕竟支付功能只对商户开放）。如果你想在本地测试玩玩，只需要修改如下配置即可：
* 微信小程序app.js中`domain:"http://127.0.0.1:port/api"`
* orderbytornado/config.py中`domain:"http://127.0.0.1:port/api"`

运行
```
python mangae.py --port=yourport
```

## 关于微信小程序上线问题
* 微信小程序上线必须要有备案的域名
* 微信小程序上线使用的服务器必须要有https服务

## tornado生产环境部署
如何使用Tornado+Nginx+Supervisor部署生产环境，请参考文章[部署Tornado](https://mirrors.segmentfault.com/itt2zh/ch8.html)
![](https://ws1.sinaimg.cn/large/006tNc79gy1fvtvqq2cv7j30j407k0tr.jpg)

