<template>
  <div class="hello">
    <div class="card" style="float:left">
      <h1>오늘의 날씨정보</h1>
      <h1><img v-if="this.weather==0" src="../assets/sun.png" width="50" height="50" >
        <img v-if="this.weather==1" src="../assets/cloud.png" width="50" height="50"> {{data[0]}} ºC</h1>
      {{data[1]}} <br/>
      {{data[2]}} <br/>
    </div>
    <br/>
    <div class="card" id="card2" style="float:left">
      <table style="font-size : 18px; font-weight : lighter ">
        <tr><th>{{data[3]}} :</th><th>{{data[4]}}</th></tr>
        <tr><th>{{data[5]}} :</th><th>{{data[6]}}</th></tr>
        <tr><th>{{data[7]}} :</th><th>{{data[8]}}</th></tr>
      </table>
      오늘 오전의 강수확률은 {{data[9]}} 입니다<br/>
      오늘 오후의 강수확률은 {{data[10]}} 입니다<br/>
    </div>
    <img id="photo" src="../../../img/download1.jpg" width="150" height="150">
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  sockets: {
    connect: function(){
      console.log('socket connected')
    },
    mise: function(a){
      console.log('get mise')
      console.log(a)
      this.data = a.data
    }
  },
  props: {
    msg: String
  },
  data () {
    return {
      data: null,
      weather: 0
    }
  },
  mounted: function() {
    console.log('in mounted')
    this.getInfo()
  },
  methods: {
    getInfo: function(){
      this.$socket.emit('mise')
      console.log('getMise called')
    },
    getImg: function(){
      if(this.data[1]=='흐림'){
        this.weather = 1
      }


    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.hello{
  font-weight: 300;
  padding-bottom: 700px;
}
#card2{
  padding-top: 50px;
  font-size: 15px;
}
#photo{
  left :0;
  padding-left: 10px;
  padding-bottom: 10px;

}
h1 {
  font-weight: 500;
}
h2{
  font-weight: 500;
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
a {
  color: #42b983;
}
</style>
