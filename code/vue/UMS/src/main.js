import { createApp } from 'vue'
import './style.css'

// viteが受け取ったSFCをjsファイルに変換してインポート
import App from './App.vue'

// router.jsでexportしたrouterをインポートする
import router from './router'

// vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'


// vuetify
const vuetify = createVuetify({
    components,
    directives,
})

// createAppで受け取ったjsを基にUIを作成
const app = createApp(App)

app.use(vuetify)
app.use(router)

// mountで指定したCSSセレクタの位置に表示（以下の場合index.htmlのid＝app）
app.mount('#app')
