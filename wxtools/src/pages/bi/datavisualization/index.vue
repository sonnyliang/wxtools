<template>
	<view class="qiun-columns">
		<view class="qiun-bg-white qiun-title-bar qiun-common-mt" >
			<view class="qiun-title-dot-light">仪表盘</view>
		</view>
		<view class="qiun-charts" >
			<canvas canvas-id="canvasGauge" id="canvasGauge" class="charts"></canvas>
		</view>
	</view>
</template>

<script>
    import uCharts from '@/components/u-charts/u-charts.js';
    var _self;
    var canvaGauge=null;
    var app=getApp()
    var moment = require('moment')
   
	export default {
		data() {
			return {
				// 仪表盘参数
				cWidth:'',
				cHeight:'',
                pixelRatio:1,
				gaugeWidth:15,
                SalesTarget:'',
                GaugeRate:'',
                Gauge: {
                    "categories": [{
                        "value": 0.2,
                        "color": "#1890ff"
                    }, {
                        "value": 0.8,
                        "color": "#2fc25b"
                    }, {
                        "value": 1,
                        "color": "#f04864"
                    }],
                    "series": [{
						"name": "销售额完成率",
						"data":''
                    }]
                }
			}
		},
		onLoad() {
            _self = this;
			this.cWidth=uni.upx2px(750);
			this.cHeight=uni.upx2px(500);
			this.getSalesVolumn();
		},
		methods: {
            getSalesVolumn(){
                this.request({
                    url:'http://localhost:8000/bi/api/gauge/?brand=chj'
				})
				.then(res=>{
					
					this.Gauge.series[0].data= res
					console.log(this.Gauge.series[0].data)
					this.showGauge("canvasGauge",this.Gauge)
					
				})
            },
			showGauge(canvasId,Gauge){
				canvaGauge = new uCharts({
					$this:_self,
					canvasId: canvasId,
					type: 'gauge',
					fontSize:11,
					legend:false,
					title: {
						name: Math.round(Gauge.series[0].data*100)+'%',
						color: Gauge.categories[1].color,
						fontSize: 25*_self.pixelRatio,
						offsetY:50*_self.pixelRatio,//新增参数，自定义调整Y轴文案距离
					},
					subtitle: {
						name: Gauge.series[0].name,
						color: '#666666',
						fontSize: 15*_self.pixelRatio,
						offsetY:-50*_self.pixelRatio,//新增参数，自定义调整Y轴文案距离
					},
					extra: {
						gauge:{
							type:'default',
							width: _self.gaugeWidth*_self.pixelRatio,//仪表盘背景的宽度
							startAngle:0.75,
							endAngle:0.25,
							startNumber:0,
							endNumber:100,
							splitLine:{
								fixRadius:0,
								splitNumber:10,
								width: _self.gaugeWidth*_self.pixelRatio,//仪表盘背景的宽度
								color:'#FFFFFF',
								childNumber:5,
								childWidth:_self.gaugeWidth*0.4*_self.pixelRatio,//仪表盘背景的宽度
							},
							pointer:{
								width: _self.gaugeWidth*0.8*_self.pixelRatio,//指针宽度
								color:'auto'
							}
						}
					},
					background:'#FFFFFF',
					pixelRatio:_self.pixelRatio,
					categories: Gauge.categories,
					series: Gauge.series,
					animation: true,
					width: _self.cWidth*_self.pixelRatio,
					height: _self.cHeight*_self.pixelRatio,
					dataLabel: true,
				});
			}
		}
	}
</script>

<style>
	/*样式的width和height一定要与定义的cWidth和cHeight相对应*/
	.qiun-charts {
		width: 750upx;
		height: 500upx;
		background-color: #FFFFFF;
	}
	
	.charts {
		width: 750upx;
		height: 500upx;
		background-color: #FFFFFF;
	}
</style>
