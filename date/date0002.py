#日付の計算はtimedeltaを使用します。timedeltaは月の日数、うるう年なども気にしないでよいので、自分で計算するより多くの手間を省くことができます。

import datetime

today = datetime.datetime.today()

#今日の日付
print(today)

#明日の日付
print(today + datetime.timedelta(days=1))

newyear = datetime.datetime(2019,1,1)

#2019年1月1日の一週間後
print(newyear + datetime.timedelta(days=7))

#2019年10月22日の一週間後
calc = today -newyear

#計算結果の戻り値は「timedelta」
print(calc.days)