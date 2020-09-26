<template>
    <view class="conatiner">
        <view class="filter">
            <view>filter</view>
        </view>
        <view class="table">
            <wyb-table ref="table" :headers="headers" :contents="OrderList" />
        </view>
    </view>
</template>

<script>
var app=getApp()
var moment = require('moment')
import wybTable from '@/components/wyb-table/wyb-table.vue';
export default {
    components:{
        wybTable
    },
    data(){
        return{
            headers: [{
                label: '订单日期',
                key: 'Billdate'
            }, {
                label: '商品数量',
                key: 'Qty'
            }, {
                label: '订单金额',
                key: 'Amount'
            }, {
                label: '品牌',
                key: 'Brand'
            }],
            OrderList:[ ]
        }
    },
    methods:{
        getOrder(){
            this.request({
                url:'http://localhost:8000/bi/api/getOrder?billdate1=2020-08-01&brand=fion'
            })
            .then(res=>{
                if(this.OrderList.length===0){
                    for(let i=0;i<res.length;i++){
                        this.OrderList.push({'Billdate':res[i].billdate1, 'Qty':res[i].qty,'Amount':res[i].amount,
                                            'Brand':res[i].brand})
                    }
                }
                console.log(res)
            })
        }
    },
    mounted(){
        this.getOrder()
    }
}
</script>

<style>
.filter{
    display:flex;
    height:20vh;
}
.table{
    display:flex;
    height:80vh;
}
</style>