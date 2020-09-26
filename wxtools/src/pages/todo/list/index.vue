<template>
	<view class="uni-flex nui-column">
		<!-- 列表标题 -->
		<view class="flex-item list-title"> 默认列表
		</view>
		<uni-segmented-control
		:current="current"
		:values="items.map(v=>v.title)"
		@clickItem="onClickItem"
		style-type="text"
		active-color="#4cd964">
		</uni-segmented-control>
		<!-- 待办事项 -->
		<view class="container todo-content">
			<view class="add-todo" v-if="current === 0">
				<input class="input-todo" type='text' placeholder="新建todo" v-model="inputValue"/>
				<button class='add-button' type='primary' @click="addTodo">新增TODO</button>
			</view>
			<view class="container todo-list" v-for="(item, index) in showList" :key="index">
				<view class="todo">{{item.todo}}</view>
				<view class="finish" @click="done(index, item)" v-if="current !== 2">√</view>
				<view class="unfinish" @click="remove(index, item)">×</view>
			</view>
			<!-- <view class='add-todo' v-show="current===0">
				+
			</view> -->
		</view>
	</view>
</template>

<script>
// 引用分段器
import {uniSegmentedControl} from '@dcloudio/uni-ui'

export default {
	data() {
		return {
			showList: [],
			todoList: [],
			finishedList: [],
			unfinishedList:[],
			items:[
				{title:'todo'},
				{title:'未完成'},
				{title:'已完成'}
			],
			current: 0,
			inputValue:"",
		}
	},
	onLoad() {

	},
	mounted(){
		this.getTodoList()
		this.getUnfinishedList()
		this.getFinishedList()
	},
	methods: {
		getTodoList(){
			this.request({
				url:'http://localhost:8000/todo/api/getTodo?user=sonny&todoType=0'
			})
			.then(res=>{
				
				if(this.current ===0){
					if(this.todoList.length===0){
						for(let i=0;i<res.length;i++){
							this.todoList.push({'id':res[i].id,'todo':res[i].todo})
						}
					}
					this.showList = this.todoList
				}
			})
		},
		getUnfinishedList(){
			this.request({
				url:'http://127.0.0.1:8000/todo/api/getTodo?user=sonny&todoType=1'
			})
			.then(res=>{
				if(this.current ===1){
					if(this.unfinishedList.length===0){
						for(let i=0;i<res.length;i++){
							this.unfinishedList.push({'id':res[i].id,'todo':res[i].todo})
						}
					}
					this.showList = this.unfinishedList
				}
			})
		},
		getFinishedList(){
			this.request({
				url:'http://127.0.0.1:8000/todo/api/getTodo?user=sonny&todoType=2'
			})
			.then(res=>{
				if(this.finishedList.length===0){
						for(let i=0;i<res.length;i++){
							this.finishedList.push({'id':res[i].id,'todo':res[i].todo})
						}
					}
					this.showList = this.finishedList
			})
		},
		onClickItem(e){
			if(this.current !== e.currentIndex){
				this.current = e.currentIndex
			}
			if(this.current===0){this.getTodoList()}
			if(this.current===1){this.getUnfinishedList()}
			if(this.current===2){this.getFinishedList()}
		},
		done(index,item){

			this.finishedList.push(this.todoList[index])
			this.todoList.splice(index,1)

			this.request({
				url:'http://127.0.0.1:8000/todo/api/getTodo/'+item.id,
				method:'put',
				data:{
					'user':'sonny',
					'todo':item.todo,
					'todoType':1
				}
			})
		},
		addTodo(){
			this.request({
				url:'http://localhost:8000/todo/api/getTodo',
				method:'post',
				data:{
					'user':'sonny',
					'todo':this.inputValue,
					'todoType':0
				}
			})
			.then(res=>{
				this.todoList.push({
					'id':res.id,
					'todo':res.todo
				})
			})
			this.inputValue=''
		}
	},
	components:{
		uniSegmentedControl
	}
}
</script>

<style>
.list-title{
	display: flex;
	height:10vh;
	background-color: 	#7FFFAA;
}
.todo-content{
	display: flex;
	height:80vh;
	background-color: #4169E1;
	padding: 12rpx;
}
.todo-list{
	list-style-type: none;
	margin:0;	
	padding:0;
}


.todo-list .finish{
	position: absolute;
	right: 100rpx;
}

.todo-list .unfinish{
	position: absolute;
	right: 30rpx;
}


.container{
	display:flex;
	flex-direction: column;
	justify-content: start;
}
.todo{
	display:flex;
	flex: 1;
	font-size: 24rpx;
	padding: 10rpx;
}


.add-todo{
	display: flex;
	flex-direction: row;

}

.add-todo .input-todo{
	display: flex;
	flex:8;
	position: relative;
	height: 50rpx;
	/* width: 200rpx; */
	font-size: 20rpx;
}

.add-todo .add-button{
	display: flex;
	flex:2;
	height: 50rpx;
	font-size: 20rpx;

}

</style>
