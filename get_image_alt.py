import openai
import sys

# OpenAIのAPIクライアントを初期化
client = openai.OpenAI()

def get_image_description(image_url):
    # gpt-4-vision-previewモデルを使用して、画像の内容についての問い合わせを行う
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Webアクセシビリティ観点でimageタグのALT属性にセットしますので、この画像はどういう画像か説明をするテキストを日本語で作ってください。文末は～の画像。～の様子。など体言止めをしてください。"},
                    {
                        "type": "image_url",
                        "image_url": {"url": image_url},
                    },
                ],
            }
        ],
        max_tokens=300,
    )

    # 応答からメッセージの内容を取得
    if not response.choices:
        raise ValueError("The API did not return a choice.")

    # 'content' が直接オブジェクトの属性として存在する場合
    message = response.choices[0].message.content

    return message

# コマンドラインから画像のURLを取得
if len(sys.argv) > 1:
    image_url = sys.argv[1]
    try:
        print("ALT text for the image:")
        print(get_image_description(image_url))
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print("Usage: python get_image_alt.py <image-url>")
