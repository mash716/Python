#スライスは以下のような記述で開始、終了位置、ステップ幅を指定します。
# またこれらの指定は省略可能で、シーケンスの要素数に応じて適切に動作します。
# 書式
# sequence[<開始位置>:<終了位置>:<ステップ幅>]


test_list = ['https','www','python','izm','com']

print(test_list[:])
print(test_list[::])