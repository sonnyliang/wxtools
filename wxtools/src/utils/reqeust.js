// es6   promise   微信小程序的api的铺垫
export default(params)=>{

    // 加载中
    uni.showLoading({
        title:'加载中'
    })

    return new Promise((resolve,reject)=>{

        // 微信原生请求
        wx.request({
            ...params,
            // 若成功则返回结果
            success(res){
                resolve(res.data);
            },
            // 若失败则返回错误
            fail(err){
                reject(err);
            },
            complete(){
                // 如果完成了就把“加载中”隐藏
                uni.hideLoading();
            }
        })
    })
}