/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// plugins/index.js？を読み込んでいるためこのファイルで.use(vuetify)しなくていい？
import { registerPlugins } from '@/plugins'

// SFCをインポートしてViteがjsファイルに変換処理をしてくれている
import App from './App.vue'
import { createApp } from 'vue'

// UIを作成している。createAppにはインポートしたjsファイル（元SFC）を渡す。
const app = createApp(App)

registerPlugins(app)

// createAppで作成したUIを#app（index.html内のCSSセレクタ）に表示する
app.mount('#app')
