---
layout: post
tags: OSS
---
（加筆中）

> + 目的
>   自作「OSS」を公開するために必要な権利情報を知りたい．
> + 制約条件
>   1. 自作 OSS は Python パッケージである．
>   1. 自作 OSS の中で，既に他者が公開しているパッケージを「利用」したい．
>   1. 自作 OSS は自由に「使用」して貰いたいが，面倒事に巻き込まれたくない．
>   1. 他の OSS に「利用」する場合は，「利用」したことを明記してほしい．

前提として最小限知っておくべきことは，「OSS (Open Source Software)」の定義，「使用 (use)」と「利用 (exploit)」の違いである（他者作成のソフトウェアを自作 OSS の一部に組み込む場合，「利用」の理解は特に重要）．そして自分が「利用」するパッケージの「ライセンス」毎の利用制約を守る．

> 前提知識: OSS 定義と「利用」可能対象（参考情報[^1]）
> ソフトウェアは大きく有償ソフトウェアと無償ソフトウェアである「フリーウェア (freeware)」に分類される．freeware は，「プロプライエタリ・ソフトウェア (proprietary software)」と「オープンソース・ソフトウェア (OSS)」に分類される．そして「利用」できるのは OSS のみで，具体的な利用制約は OSS ライセンス毎に規定される．

では具体的に確認していく．

まず制約条件 1, 2 からライセンス確認対象は以下となる．

+ Python 本体 (OSS, 標準パッケージ含む)
PSF (Python Software Foundation) License = GNU GPL (GNU General Public License) compatible [^2]
+ import したサードパッケージ（具体化のため，networkx を利用しているとする）
networkx (OSS): BSD-3-Clause License

さらに参考情報[^1]の『4.「主要ライセンス」を理解する』の表から利用制約を抜粋すると次の通り．

| 種類 | 利用元のライセンス表示 | 類型 | 作成者名の無断使用 | 特許条項
| ---- | ---- | ---- | ---- | ---- | ----
| GNU GPL v3 | 必要 | コピーレフト | - | あり
| 3-Clause BSD | 必要 | 非コピーレフト | 禁止 | なし

「利用元のライセンス表示」が必要な場合，…

「コピーレフト」とは…

「作者名の無断使用」禁止となっているのは…

「特許条項」ありの場合…

[^1]: [Qiita; OSSのライセンスを理解する（「使用」と「利用」の違い、知っていますか？）](https://qiita.com/bremen/items/c5aa9446e73aa4bc1de0)
[^2]: [Wikipedia; Python Software Foundation License](https://ja.wikipedia.org/wiki/Python_Software_Foundation_License)