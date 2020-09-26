<template>
	<view class="container">
		<navigator url='/pages/bi/orderlist/index'>
			<view>查看订单</view>
		</navigator>
		<navigator url='/pages/bi/datavisualization/index'>
			<view>数据可视化</view>
		</navigator>
	</view>	
</template>

<script>
	export default {
		data() {
			return {
				title: 'BI'
			}
		},
		onLoad() {

		},
		methods: {

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
