# get_image_alt.py

## Overview
get_image_alt.py is a Python utility that provides ALT text descriptions for images according to WCAG Guideline H37, aiding in the creation of accessible web content for visually impaired users. The script interfaces with OpenAI's GPT-4 model to generate descriptions that fulfill web accessibility standards.

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
