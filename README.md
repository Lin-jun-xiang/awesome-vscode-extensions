# vscode-extensions [Commented]
* [中文版README.md](README_中文.md)
* 中文版介紹較為完整，英文版持續更新中
* The Chinese version currently has a more complete introduction, while the English version is being continuously updated.

---

* Record and share vscode extensions, including those that enhance development efficiency, must-haves, theme beautification, etc.
* This project will provide detailed usage instructions for each extension, with the hope of helping coders all over the world to code happily together :sunglasses:
* Outline of extensions:
    - [Quickly download multiple extensions](#starquickly-download-multiple-extensions-please-read-this-first)
    - [Theme](#purple_hearttheme)
    - [Editor and environment beautification]
    - [Must-haves and highly recommended]
    - [Transparent editor]
    - [Big data and AI engineer - Jupyter(Python)]
    - [Git and Markdown assistants]
    - [Fixer]
---

## :star:Quickly download multiple extensions (please read this first)
Later, we will introduce a lot of vscode extensions. Here is a trick that can quickly download many extensions without having to look for them one by one.
(You can download the `.ps1` file attached to this project through the third step and exclude the extensions you don't need)
If you want to transfer extensions from an old computer to a new one in the future, you can also use this method ~:kissing:

> Method:
> 1. Access all the extensions of vscode on the current computer and output them as text. Enter the following command in terminal (`powershell`):
> `code --list-extensions | ForEach-Object {"code --install-extension $_"} > extensions.ps1`
> 2. After the command is executed, the `extensions.ps1` file (the filename is defined when executing the command) will be obtained in the current directory.
> 3. Enter the following command in terminal (`powershell`) on the new computer:
> `.\extensions.ps1`
> 4. Download completed
> <img src="img/2023-03-17-22-28-35.png" width="60%">

---

## :purple_heart:Theme

The biggest reason for using vscode is to have an `eye-catching`, `elegant`, `comfortable`, and `pleasant editing interface`. Only a good-looking editing environment can make coders willing to type on the keyboard ~:sunglasses:

Next, the author will share his favorite themes with you one by one (the following examples are based on Python, and there may be slight differences for different languages)

Oh! Wait a minute, here's a quick way to switch themes. After all, you may want to change your theme every day~~

> Quickly switch themes
> 1. "ctrl+shift+p": Open the vscode command input box
> 2. "Preferences: Color Theme": Enter and select the theme you want

### ButterTheme
* As its name suggests, it is a non-eye-straining *cream yellow* theme
* A very rare theme (to put it bluntly, not many people use it), but the author loves it
* In case you can't find this theme，<a href="https://marketplace.visualstudio.com/items?itemName=Levampire.Buttur" target="_blank">link</a>

<img src="img/2023-03-17-14-36-15.png" width="60%">

### Coder200
* 這次看名字，完全毫無想法了...
* 非常罕見的主題，充滿著*橘橙色*，so sexy~:flushed:

<img src="img/2023-03-17-14-44-30.png" width="60%">

### Dracula Official
* 非常知名，充滿著*粉色*與*紫色*的吸血鬼色

<img src="img/2023-03-17-14-51-36.png" width="60%">

### LaserWave
* 帶有夕陽感覺的*紫粉色*

<img src="img/2023-03-17-20-17-56.png" width="60%">

### Moegi Theme
* 溫和、不傷眼的主題

<img src="img/2023-03-17-20-20-13.png" width="60%">

### Panda Theme
* 具有*湖水綠* 的頂級主題:panda_face:
* 該主題真的很香

<img src="img/2023-03-17-20-21-23.png" width="60%">

### Simple Dark
* 背景非常黑，文字顏色也不會太刺眼

<img src="img/2023-03-17-20-23-37.png" width="60%">

### Skyline
* 喜歡藍色的朋友一定要用:blue_heart:

<img src="img/2023-03-17-20-25-15.png" width="60%">

### SynthWave '84
* 超級高科技、炫炮的螢光主題:sunglasses:
* 選完主題後，記得啟動螢光效果 (該效果也可以搭配其他主題色哦:fu:)

> 啟動螢光模式:
> 1. "ctrl+shift+p": 打開 vscode 命令輸入框
> 2. "Synthwave '84: Enable/Disable Neon Dreams": 開啟、關閉 (附圖)
> 3. "Restart": 重啟 vscode

<img src="img/2023-03-17-20-28-44.png" width="60%">

<img src="img/2023-03-17-20-27-06.png" width="60%">

### Tearz
* 與前面介紹的 Moegi 有點相似
* 但是這個*紫色*真的太吸引作者了~

<img src="img/2023-03-17-20-33-32.png" width="60%">

### Xcode Theme
* 經典主題之一，不敢忽略

<img src="img/2023-03-17-20-35-39.png" width="60%">

### One Dark Pro
* 經典主題之一，不敢忽略

<img src="img/2023-03-17-20-36-31.png" width="60%">

### Material Dark
* 經典主題之一，不敢忽略

<img src="img/2023-03-17-20-37-24.png" width="60%">

<a href="#top">Back to top</a>

---
## :yellow_heart:美化編輯器、編輯環境
裝潢好我們的編輯器之後，接下來要介紹的插件不僅可以增加美觀，還可以提升工作效率哦~

### Color Highlight
* 如果您是**前端工程師**或**數據分析師**，常常需要進行**視覺化**工作，您一定要下載這個 !
* 在編輯時，只要出現*十六進制*的顏色表達式，就可以清楚看到顏色囉 (再也不用執行完代碼，才知道顏色好不好看)

<img src="img/2023-03-17-20-48-11.png" width="60%">

### Material Theme Icons
* 不同附檔名，不同的 Icon
* 除了好看之外，還可以讓自己在找檔案時更快速

<img src="img/2023-03-17-20-51-07.png" width="60%">

### vscode-icons
* 與 Material Theme Icons 略為不同
* 作者偏好使用這個~

<img src="img/2023-03-17-20-53-26.png" width="60%">

<a href="#top">Back to top</a>

---
## :green_heart:不可不擁有的、非常大推
以下要介紹的插件，真的非常好用!
絕大部分都是可以提升開發效率的，走過路過千萬不要錯過:heart_eyes:

### Code Runner
* 相信使用 vscode 的大家，應該不會不熟悉這插件吧!?
* 可以讓 vscode 一鍵執行程式
* 支援大量語言，例如: C, C++, Java, JavaScript, PHP, Python, Perl...等 

<img src="img/2023-03-17-20-59-33.png" width="60%">

### Comment Divider
* 快捷鍵生成好看*註釋風格*
* 如下圖，可以看到 `Shift+Alt+x` 及 `Alt+x` 兩種風格 

<img src="img/2023-03-17-21-03-04.png" width="60%">

### autoDocstring - Python Docstring Generator
* 該插件是針對 `Python` 開發者所介紹
* 快解鍵生成 *Docstring* 風格的註釋
* 描述函式目的、參數、回傳值...等訊息
* 支援不同種 *Docstring*，例如 `google`, `sphinx`, `numpy`...等

> 使用方式，在要生成註釋的地方按:
Windows: `ctrl+shift+2`
Mac: `cmd+shift+2` 

<img src="img/2023-03-17-21-07-10.png" width="60%">

### Draw.io Integration
* 流程圖繪製工具
* 進行專案設計時，可以利用該插件規劃好可行性
* 可以做為筆記使用
* 支援許多常用圖案，例如 Google Cloud Platform 代表功能符 (如圖)

<img src="img/2023-03-17-21-14-00.png" width="60%">

### Path Intellisense
* 編碼時擁有這個插件，真是幸福:kissing_heart:
* 適合常常讀寫檔案的碼農使用
* 寫路徑時，會自動列出您尋找路徑下的檔案

<img src="img/2023-03-17-21-17-09.png" width="60%">

<a href="#top">Back to top</a>

---

## 透明化編輯器
透明化特效就是牛
可以成為工作偷懶神器 (邊看影片邊敲代碼~)
可以搭配自己的桌布，邊看自己老婆邊敲代碼

### GlassIt-VSC

> 使用方式:
`ctrl+alt+z`: 調低飽和度 (透明)
`ctrl+alt+c`: 調高飽和度 (不透明)

<img src="img/2023-03-17-21-25-27.png" width="60%">

<a href="#top">Back to top</a>

---

## 大數據、AI 工程師 - Jupyter (Python)
這邊要介紹的插件真的很屌!
作者認識很多玩 `Python` 的人不習慣使用 vscode，很多原因都是:
* Vscode 不像 Spyder, Pycharm 一樣，可以方便的察看數據表 (尤其很愛用 `DataFrame` 的人)
* 不習慣使用 Vscode 的 Debug 模式
* 希望以交互模式執行代碼

該插件提共了以下功能:
* **交互模式**
* 查看變數資料型態、變數值 (就如同 spyder, pycharm 一樣)
* **逐行執行程式**、**部分執行程式碼** (這個功能真的很實用，比Debug還好用~:heart_eyes:)

> 如果您聽得懂中文，建議可以花 5 分鐘快速了解 Jupyter 插件的用法 (觀看<a href="https://www.bilibili.com/video/BV1Bg411J78F/" target="_blank">連結</a>)

> 使用方法:
> * 下載以下插件 (有些應該不用，但小弟忘記啦~)
`Jupyter`, `Jupyter keymap`, `Jupyter slide show`, `Jupyter cell tag`, `Jupyter notebook renderes`, `vs code jupyter notebook previewer`
><img src="img/2023-03-17-21-50-07.png" width="60%">

> * **以交互模式執行代碼**
> 1. 於腳本中滑鼠右鍵
> 2. 選擇 `Run Current File in Interactive Window` (建議設置vscode快捷鍵，本人設置 `F10`)
> 3. 執行完時，會出現 `Interactive` 視窗:
><img src="img/2023-03-17-21-54-03.png" width="60%">
><img src="img/2023-03-17-21-57-03.png" width="60%">

> * **查看變數資料型態、變數值** (需處在交互模式中)
> 點選交互視窗中的 `Variables`
><img src="img/2023-03-17-22-01-55.png" width="60%">

> * **逐行執行、部分執行**
> 1. 選取要執行的程式碼 (可以是一行或多行)
> 2. 滑鼠右鍵
> 3. 選擇 `Run Selection/Line in Interactive Window`
><img src="img/2023-03-17-22-04-33.png" width="60%">

<a href="#top">Back to top</a>

---

## Git、Markdown 輔助
接下來介紹的插件，如果您也是個 Github, Gitlab 專案開發者，您一定要看~

### GitLens
* 可以看到下載完後，腳本中的代碼會顯示哪些是**改過的**、標註出**誰改的**、標註**何時改的**
* 注意看右半區塊的代碼，`170` 行有*綠色*的線，表示此地有*新增代碼*紀錄 (*紅色*則是有*刪減*)
* 記得專案要用 `git` 追蹤，該插件才有用哦

<img src="img/2023-03-17-22-08-15.png" width="60%">

### Markdown Preview Enhanced
* 編寫 `.md` 檔案時，可以預瀏覽結果
* `ctrl+k` 接著 `v`，打開預覽畫面
* 下圖中間是 `.md` 檔案，右邊則是預覽畫面

<img src="img/2023-03-17-22-15-20.png" width="60%">

<a href="#top">Back to top</a>

---

## 修復器 (如果卸載vscode插件發生損毀，請使用此插件修理)
有時候卸載插件時，vscode右下角會跳出錯誤，透過以下方法可以解決問題

> 使用方式:
> 1. 下載 `Fix VSCode Checksums` 插件
> 2. `ctrl+shift+p`: 打開命令
> 3. `Fix ChecksumS: Apply`: 執行修復
> 4. `ctrl+shift+p`: 打開命令
> 5. `Developer: Reload Window`: 重啟 vscode

<img src="img/2023-03-17-21-36-48.png" width="60%">

<a href="#top">Back to top</a>

 
