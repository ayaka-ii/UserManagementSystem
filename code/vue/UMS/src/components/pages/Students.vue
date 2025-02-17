<script setup>

// https://ja.vuejs.org/api/sfc-script-setup.html
// https://ja.vuejs.org/api/composition-api-setup.html

import axios from 'axios';
import {ref,onMounted} from 'vue';

const user_list = ref();
const getUsers = ()=>{
    // DjangoのWEBAPIのエンドポイントへリクエスト
    // resにはgetで返ってきたオブジェクトが入る
    // res.dataオブジェクト内のresultsの値（＝辞書）を取得してuser_list変数へ入れる
    axios.get('http://localhost:8888/api/users/').then((res) =>{
        user_list.value = res.data.results;
    })
}
onMounted(async()=>{
  await getUsers();
})

</script>

<template>
    <p>生徒一覧</p>
    <!-- データ辞書を回してnameキーの値を取得 -->
    <table>
        <thead>
            <tr>
                <th>氏名</th>
                <th>住所</th>
                <th>電話番号</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="user in user_list">
                <td>{{user.name}}</td>
                <td>{{user.address}}</td>
                <td>{{user.telephone}}</td>
            </tr>
        </tbody>
    </table>
</template>


