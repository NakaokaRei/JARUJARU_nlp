# JARUJARU_nlp
[ジャルジャルの動画](https://www.youtube.com/channel/UChwgNUWPM-ksOP3BbfQHS5Q)のタイトルから再生数を予測したい


## 開発環境
* Python
* Mecab
* gensim
* scikit-learn


## 使い方
次のコマンドを叩きます
```
$ python predict.py ここにジャルジャルのコントの名前
```
するとターミナル上に「見る価値なし」「まあまあ」「一見の価値あり」のどれかが出力されます。


## 注意事項
モデルがガバガバ判定です。過度に信用しすぎないようにしてください。

## 参考記事
* [ニュースの記事の分類を機械学習で予測する](https://qiita.com/hyo_07/items/ba3d53868b2f55ed9941)
