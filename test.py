import re
text = """キリンは大昔から __複数名詞__ の興味の対象でした。キリンは __複数名詞__ の中で一番背が高いですが、科学者たちはそのような長い __体の一部__ をどうやって獲得したのか説明できません。キリンの身長は __数値__ __単位__ 近くあり、その高さのほとんどは脚と __体の一部__ によるものです。
"""

def mad_libs(mls):
    """
    :params mls: 文字列で、ユーザーに入力してもらいたい単語（＝ヒント）の部分は後を2つのアンダースコアで挟んでください。__hint_hint__はだめです。__hint__はOKです。
    """
    hints = re.findall("__.*?__", mls)
    if hints is not None:
        for word in hints:
            q = "{}を入力：".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
        print('\n')
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("引数mlsが無効です")

mad_libs(text)