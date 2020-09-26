<template>
  <view class="container">
      <navigator url='/pages/todo/list/index'>
          <view>工作列表</view>
      </navigator>
    <view class="add-list">
        +
    </view>
  </view>
</template>

<script>
export default {
    methods:{
        // listDetail(){
        //     console.log('点击')
        //     uni.navigateTo({
        //         url:'/pages/todo/list/index'
        //     });
        // }
    }
}
</script>

<style>
.container{
    display:flex;
}
.add-list{
    position:absolute;
    bottom: 100rpx;
    right: 100rpx;
}
</style>