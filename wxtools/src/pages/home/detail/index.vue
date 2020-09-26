<template>
    <view class='container' style="margin: 50upx">
        <u-parse :content="content"></u-parse>
    </view>
</template>

<script>
import marked from 'marked'
import uParse from '@/components/u-parse/u-parse.vue'


export default {
    data(){
        return{
            blogId:'',
            content:'',
        }
    },
    methods:{
        getContent(){
            this.request({
                url:'http://localhost:8000/blog/api/getPost?id='+ this.blogId
            })
            .then(res=>{
                this.content = marked(res[0].body)
                console.log(this.content)
            })
        },
    },
    components:{
        uParse
    },
    onLoad(options){
        this.blogId = options.id
        this.getContent()
    }
}
</script>

<style>
@import url("@/components/u-parse/u-parse.css")
</style>
