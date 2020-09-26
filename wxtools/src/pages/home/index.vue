<template>
	<view class="content">
		<view v-for="(item,index) in postList" :key="index">
			<view class="container">
				<uni-card 
				:title="item.title"
				mode="title" 
				:is-shadow="true" 
				:note="item.created_time"
				@click="toDetail(item.id)"
				> {{item.excerpt}} 
				</uni-card>
			</view>
		</view>
	</view>
</template>

<script>
	var app = getApp()
	var moment = require('moment');
	import {uniCard} from '@dcloudio/uni-ui'

	export default {
		data() {
			return {
				title: 'Hello',
				postList:[],
			}
		},
		onLoad() {
			
		},
		methods: {
			getPost(){
				this.request({
					url:'http://localhost:8000/blog/api/getPost/'
				})
				.then(res=>{
					console.log(res)
					for(let i=0;i<res.length;i++){
						this.postList.push({'id':res[i].id,'title':res[i].title,'excerpt':res[i].excerpt,'created_time':res[i].created_time})
					}
				})
			},
			toDetail(value){
				uni.navigateTo({
					url:"/pages/home/detail/index?id="+value
				});
			}
		},
		mounted(){
			this.getPost()
		},
		components: {
			uniCard,
		}
	}
</script>

<style>
	.content {
		text-align: center;
		height: 400upx;
	}

	.logo {
		height: 200upx;
		width: 200upx;
		margin-top: 200upx;
	}

	.title {
		font-size: 36upx;
		color: #8f8f94;
	}
</style>
