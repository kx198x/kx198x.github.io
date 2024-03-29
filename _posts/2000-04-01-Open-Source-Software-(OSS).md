---
layout: post
tags: OSS
---
（加筆中）


<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [概要](#概要)
- [PyPI 登録覚書](#pypi-登録覚書)
- [最初に知っておくべき前提](#最初に知っておくべき前提)
- [自分が守るべき事項](#自分が守るべき事項)
- [他人に守って貰いたい事項](#他人に守って貰いたい事項)
- [補足: PyPI へのパッケージ登録例](#補足-pypi-へのパッケージ登録例)

<!-- /code_chunk_output -->


##### 概要

> + 目的
>   +   自作「OSS」を公開する．
> + 制約条件
>   1. 自作 OSS は Python パッケージである．
>   1. 自作 OSS の中で，サードパーティを import している．
>   1. 自作 OSS は自由に「使用」して貰いたいが，面倒事に巻き込まれたくない．
>   1. 他の OSS に「利用」する場合は，「利用」したことを明記してほしい．

パッケージ作成や PyPI への登録方法の覚書，理解しにくい著作権関係についてまとめる．具体的には，まず最初に知っておくべき前提，自分が守るべき事項（制約 1, 2 からくる），他人に守って貰いたい事項（制約 3, 4 からくる），それらの事項をパッケージに反映するにはどうすればよいか順に述べる．

##### PyPI 登録覚書

パッケージ作成や PyPI 登録方法詳細 → [他記事](https://qiita.com/c60evaporator/items/e1ecccab07a607487dcf)参照．

1. required package

    ```shell
    pip install setuptools
    pip install twine
    pip install wheel
    ```

1. {dist, egg-info}, build from `setup.py`

    ```shell
    python setup.py sdist
    python setup.py bdist_wheel
    ```

1. pypi information for twin upload

    `.pypirc` 設定．

1. upload test

    ```shell
    twine upload --repository testpypi ./dist/*1.0.0a0*
    ```

1. upload 1st

    ```shell
    twine upload --repository pypi ./dist/*1.0.0a0*
    ```

1. upload 2nd~


1. version

    `major#.minor#.build#-alpha.#`
    + 大幅変更: major increment
    + 機能追加: minor increment
    + バグ修正: build increment

    ```text
    1.0.0-alpha.0
    1.0.0-alpha.1
    ‥‥
    1.0.0
    ```

##### 最初に知っておくべき前提

最初に知っておくべきは，「OSS (Open Source Software)」の定義，「利用 (exploit)」と「使用 (use)」の違い，「ライセンス (license)」である．われわれは他者が定めた「ライセンス」制約に従って他者の成果物を「利用」し，自身が定めた「ライセンス」制約に従って自身の成果物を他者に「利用」してもらう．

> 前提知識: OSS 定義と「利用」可能な対象（参考情報[^1]）
> ソフトウェアは大きく有償ソフトウェアと無償ソフトウェアである「フリーウェア (freeware)」に分類される．freeware は，「プロプライエタリ・ソフトウェア (proprietary software)」と「オープンソース・ソフトウェア (OSS)」に分類される．そして「利用」できるのは OSS のみで，具体的な利用制約は OSS ライセンス毎に規定される．

##### 自分が守るべき事項

他者が定めた「ライセンス」制約を守る必要がある．まずライセンスを識別して，各ライセンスの利用制約を確認する．具体的には制約条件 1, 2 から，確認対象のライセンスは以下 2 つ．

+ Python 本体 (OSS, 標準パッケージ含む)

> PSF (Python Software Foundation) License = GNU GPL (GNU General Public License) compatible [^2]（GPL 互換性があるがコピーレフトはないことに注意．）

+ import したサードパッケージ（具体化のため，networkx を利用しているとする）

> networkx (OSS): BSD-3-Clause License

続いて参考情報[^1]の『4.「主要ライセンス」を理解する』の表から利用制約を抜粋すると次の通り．

| 種類 | 利用元のライセンス表示 | ソースコード開示 | 作成者名の無断使用 | 特許条項
| ---- | ---- | ---- | ---- | ---- | ----
| GNU GPL v3 | 必要 | コピーレフト型 | - | あり
| 3-Clause BSD | 必要 | 非コピーレフト型 | 禁止 | なし

+ 利用元のライセンス表示

基本的にしなければならない．だがこれは，third package の制約というより，自分がライセンスを選ぶときに生じる制約．

+ ソースコード開示

類型毎にことなるが，いずれも第三者に「再頒布」（はんぷ）しない場合は考えなくてもよい．今回は OSS として頒布するが，OSS としてソースコードを公開するのだから，類型によらず，自分が守るべき制約を気にする必要はない．

ちなみに，Python が GNU GPL 相当なのは一考に値する．企業で Python を使うことは，自社内で開発したものを自社内で使用するか，開発したものをソースコード開示して売ることになる．

+ 作者名の無断使用

禁止となっているのは…

+ 特許条項

ありの場合…

##### 他人に守って貰いたい事項

制約条件 3, 4 から

だが，自分のライセンスが他者にどう使われるかという観点で指定する必要がある．

「コピーレフト」型の場合，改造部分以外のソースコードを含め開示要求する．

「準コピーレフト」型の場合，改造部分のみ開示を要求する．

「非コピーレフト」型の場合，開示要求はない．

##### 補足: PyPI へのパッケージ登録例

PyPI へのパッケージ登録について書かれた記事 [^3] を前提に，さらに具体的な記述をする．

ライセンス表示

```Text
LICENSE
```

あ

```Text
setup.py
```

[^1]: [Qiita; OSSのライセンスを理解する（「使用」と「利用」の違い、知っていますか？）](https://qiita.com/bremen/items/c5aa9446e73aa4bc1de0)
[^2]: [Wikipedia; Python Software Foundation License](https://ja.wikipedia.org/wiki/Python_Software_Foundation_License)
[^3]: [【PyPI 】Pythonの自作ライブラリをpipに公開する方法](https://qiita.com/c60evaporator/items/e1ecccab07a607487dcf)