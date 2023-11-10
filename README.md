# get_image_alt.py

## Overview
get_image_alt.py is a Python utility that provides ALT text descriptions for images according to WCAG Guideline H37, aiding in the creation of accessible web content for visually impaired users. The script interfaces with OpenAI's GPT-4 model to generate descriptions that fulfill web accessibility standards.

```
$ python get_image_alt.py http://foo-bar.com/image/image1.jpg
ALT text for the image:
秋の紅葉が美しい森とその反射が見られる静かな湖の風景。

$ python get_image_alt.py https://foo-bar.com/image/image2.jpg
ALT text for the image:
スーツを着た男性と白いブラウスを着た女性が対話している様子。

$ python get_image_alt.py https://foo-bar.com/image/image3.jpg
ALT text for the image:
ノートパソコンが置かれたテーブルを挟んで笑顔で会話をしている男女３人の様子。
```
## Installation

```bash
git clone https://github.com/daishir0/get_image_alt
cd get_image_alt
pip install -r requirements.txt
export OPENAI_API_KEY='YOUR-OPENAI-API-KEY'
```

## Usage

After installation, run the script with the following command:

```bash
python get_image_alt.py <image-url>
```

Replace `<image-url>` with the URL of the image you want to describe.

## Notes
Ensure your OPENAI_API_KEY is set correctly as an environment variable. This script relies on the OpenAI GPT-4 API, which requires appropriate API credentials.

## License
This project is open-sourced under the MIT License.

---

# get_image_alt.py

## 概要
get_image_alt.pyは、WCAGガイドラインH37に従い画像のALTテキスト説明を提供するPythonユーティリティです。このスクリプトは、Webアクセシビリティ基準を満たす説明を生成するためにOpenAIのGPT-4モデルとインターフェースします。
```
$ python get_image_alt.py http://foo-bar.com/image/image1.jpg
ALT text for the image:
秋の紅葉が美しい森とその反射が見られる静かな湖の風景。

$ python get_image_alt.py https://foo-bar.com/image/image2.jpg
ALT text for the image:
スーツを着た男性と白いブラウスを着た女性が対話している様子。

$ python get_image_alt.py https://foo-bar.com/image/image3.jpg
ALT text for the image:
ノートパソコンが置かれたテーブルを挟んで笑顔で会話をしている男女３人の様子。
```
## インストール方法

```bash
git clone https://github.com/daishir0/get_image_alt
cd get_image_alt
pip install -r requirements.txt
export OPENAI_API_KEY='あなたのOPENAI-API-KEY'
```

## 使い方

インストール後、以下のコマンドでスクリプトを実行します：

```bash
python get_image_alt.py <image-url>
```

`<image-url>`を説明したい画像のURLに置き換えてください。

## 注意点
OPENAI_API_KEYが環境変数として正しく設定されていることを確認してください。このスクリプトはOpenAI GPT-4 APIに依存しており、適切なAPI認証情報が必要です。

## ライセンス
このプロジェクトはMITライセンスの下でオープンソース化されています。
